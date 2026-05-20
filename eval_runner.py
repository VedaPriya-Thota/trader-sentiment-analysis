import argparse
import json
import logging
import time
from datetime import datetime
from pathlib import Path

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score

from xgboost import XGBClassifier

from src.utils.data_loader import load_csv
from src.preprocessing.preprocess_historical import preprocess_historical
from src.preprocessing.preprocess_sentiment import preprocess_sentiment
from src.features.merge_features import merge_trading_sentiment


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

BASE_DIR = Path(__file__).resolve().parent
OUTPUT_JSON_DIR = BASE_DIR / "outputs" / "json"


def prepare_model_data():
    historical_df = load_csv("data/raw/historical_data.csv")
    sentiment_df = load_csv("data/raw/fear_greed_index.csv")

    historical_df = preprocess_historical(historical_df)
    sentiment_df = preprocess_sentiment(sentiment_df)

    df = merge_trading_sentiment(historical_df, sentiment_df)

    df["fee_ratio"] = df["fee"] / df["size_usd"].replace(0, 1)
    df["fee_ratio"] = pd.to_numeric(df["fee_ratio"], errors="coerce")

    df["is_buy"] = (
        df["side"]
        .str.lower()
        .eq("buy")
        .astype(int)
    )

    if "classification" in df.columns:
        df = pd.get_dummies(
            df,
            columns=["classification"],
            drop_first=True
        )

    base_features = [
        "size_usd",
        "fee",
        "fee_ratio",
        "hour",
        "value",
        "is_buy"
    ]

    sentiment_features = [
        col for col in df.columns
        if col.startswith("classification_")
    ]

    features = base_features + sentiment_features

    target = "is_profitable"

    for col in features:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    df = (
        df[features + [target]]
        .replace([float("inf"), float("-inf")], pd.NA)
        .dropna()
    )

    X = df[features]
    y = df[target].astype(int)

    return X, y, features


def get_model(model_name):
    if model_name == "random_forest":
        return RandomForestClassifier(
            n_estimators=150,
            max_depth=12,
            random_state=42,
            class_weight="balanced"
        )

    if model_name == "gradient_boosting":
        return GradientBoostingClassifier(
            n_estimators=150,
            learning_rate=0.05,
            max_depth=3,
            random_state=42
        )

    if model_name == "xgboost":
        return XGBClassifier(
            n_estimators=250,
            learning_rate=0.05,
            max_depth=5,
            subsample=0.85,
            colsample_bytree=0.85,
            eval_metric="logloss",
            random_state=42,
            n_jobs=-1
        )

    raise ValueError(
        "Unsupported model. Use random_forest, gradient_boosting, or xgboost."
    )


def run_eval(model_name):
    logging.info(f"Preparing evaluation data for model: {model_name}")

    X, y, features = prepare_model_data()

    X_train, X_eval, y_train, y_eval = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    model = get_model(model_name)

    logging.info("Training model")
    train_start = time.perf_counter()
    model.fit(X_train, y_train)
    train_time = time.perf_counter() - train_start

    logging.info("Running inference on held-out evaluation set")
    inference_start = time.perf_counter()
    y_pred = model.predict(X_eval)
    y_prob = model.predict_proba(X_eval)[:, 1]
    inference_time = time.perf_counter() - inference_start

    batch_size = len(X_eval)

    results = {
        "timestamp": datetime.utcnow().isoformat(),
        "model": model_name,
        "features": features,
        "eval_rows": int(batch_size),
        "accuracy": float(accuracy_score(y_eval, y_pred)),
        "precision": float(precision_score(y_eval, y_pred)),
        "recall": float(recall_score(y_eval, y_pred)),
        "f1_score": float(f1_score(y_eval, y_pred)),
        "roc_auc": float(roc_auc_score(y_eval, y_prob)),
        "train_time_seconds": round(train_time, 4),
        "inference_time_seconds": round(inference_time, 4),
        "latency_per_row_ms": round((inference_time / batch_size) * 1000, 6),
        "status": "success"
    }

    return results


def main():
    parser = argparse.ArgumentParser(
        description="Evaluation runner for profitability prediction models"
    )

    parser.add_argument(
        "--model",
        type=str,
        default="random_forest",
        choices=["random_forest", "gradient_boosting", "xgboost"],
        help="Model to evaluate"
    )

    args = parser.parse_args()

    try:
        results = run_eval(args.model)

        print(json.dumps(results, indent=4, default=str))

        OUTPUT_JSON_DIR.mkdir(parents=True, exist_ok=True)

        output_path = OUTPUT_JSON_DIR / "eval_results.json"

        with open(output_path, "w") as f:
            json.dump(results, f, indent=4, default=str)

        logging.info(f"Saved eval results to {output_path}")

    except Exception as e:
        logging.error(f"Evaluation failed: {e}")

        error_output = {
            "timestamp": datetime.utcnow().isoformat(),
            "status": "error",
            "message": str(e)
        }

        print(json.dumps(error_output, indent=4))


if __name__ == "__main__":
    main()