import pandas as pd

from sklearn.model_selection import (
    train_test_split,
    StratifiedKFold,
    cross_val_score
)

from sklearn.ensemble import (
    RandomForestClassifier,
    GradientBoostingClassifier
)

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score
)

from xgboost import XGBClassifier


def train_profitability_model(df: pd.DataFrame):

    model_df = df.copy()

    model_df["fee_ratio"] = (
        model_df["fee"] /
        model_df["size_usd"].replace(0, 1)
    )

    model_df["fee_ratio"] = pd.to_numeric(
        model_df["fee_ratio"],
        errors="coerce"
    )

    model_df["is_buy"] = (
        model_df["side"]
        .str.lower()
        .eq("buy")
        .astype(int)
    )

    if "classification" in model_df.columns:
        model_df = pd.get_dummies(
            model_df,
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
        col for col in model_df.columns
        if col.startswith("classification_")
    ]

    features = base_features + sentiment_features

    target = "is_profitable"

    for col in features:
        model_df[col] = pd.to_numeric(
            model_df[col],
            errors="coerce"
        )

    model_df = (
        model_df[features + [target]]
        .replace([float("inf"), float("-inf")], pd.NA)
        .dropna()
    )

    X = model_df[features]
    y = model_df[target].astype(int)

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    models = {
        "RandomForestClassifier": RandomForestClassifier(
            n_estimators=150,
            max_depth=12,
            random_state=42,
            class_weight="balanced"
        ),

        "GradientBoostingClassifier": GradientBoostingClassifier(
            n_estimators=150,
            learning_rate=0.05,
            max_depth=3,
            random_state=42
        ),

        "XGBClassifier": XGBClassifier(
            n_estimators=250,
            learning_rate=0.05,
            max_depth=5,
            subsample=0.85,
            colsample_bytree=0.85,
            eval_metric="logloss",
            random_state=42,
            n_jobs=-1
        )
    }

    best_model_name = None
    best_model = None
    best_metrics = None
    best_auc = -1

    cv = StratifiedKFold(
        n_splits=5,
        shuffle=True,
        random_state=42
    )

    for name, model in models.items():

        model.fit(X_train, y_train)

        y_pred = model.predict(X_test)
        y_prob = model.predict_proba(X_test)[:, 1]

        cv_auc_scores = cross_val_score(
            model,
            X,
            y,
            cv=cv,
            scoring="roc_auc",
            n_jobs=-1
        )

        metrics = {
            "model": name,
            "target": target,
            "features": features,
            "accuracy": float(accuracy_score(y_test, y_pred)),
            "precision": float(precision_score(y_test, y_pred)),
            "recall": float(recall_score(y_test, y_pred)),
            "f1_score": float(f1_score(y_test, y_pred)),
            "roc_auc": float(roc_auc_score(y_test, y_prob)),
            "cv_roc_auc_mean": float(cv_auc_scores.mean()),
            "cv_roc_auc_std": float(cv_auc_scores.std()),
            "train_rows": int(len(X_train)),
            "test_rows": int(len(X_test)),
            "note": (
                "PnL-derived features were excluded to prevent data leakage. "
                "Cross-validation was added for more reliable model evaluation."
            )
        }

        if metrics["roc_auc"] > best_auc:
            best_auc = metrics["roc_auc"]
            best_model_name = name
            best_model = model
            best_metrics = metrics

    feature_importance = pd.DataFrame({
        "feature": features,
        "importance": best_model.feature_importances_
    }).sort_values(
        by="importance",
        ascending=False
    )

    best_metrics["best_model_selected"] = best_model_name

    return best_metrics, feature_importance