import argparse
import json
import logging
from pathlib import Path

import pandas as pd


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

BASE_DIR = Path(__file__).resolve().parent
REPORTS_DIR = BASE_DIR / "outputs" / "reports"
JSON_DIR = BASE_DIR / "outputs" / "json"


def load_csv(path: Path) -> pd.DataFrame:
    if not path.exists():
        raise FileNotFoundError(f"Required file not found: {path}")

    return pd.read_csv(path)


def build_summary(sentiment=None, account=None):
    sentiment_pnl_path = REPORTS_DIR / "sentiment_pnl_analysis.csv"
    trader_risk_path = REPORTS_DIR / "trader_risk_summary.csv"
    model_metrics_path = JSON_DIR / "profitability_model_metrics.json"

    sentiment_df = load_csv(sentiment_pnl_path)
    trader_df = load_csv(trader_risk_path)

    if model_metrics_path.exists():
        with open(model_metrics_path, "r") as f:
            model_metrics = json.load(f)
    else:
        model_metrics = {}

    result = {
        "filters": {
            "sentiment": sentiment,
            "account": account
        },
        "sentiment_summary": {},
        "account_summary": {},
        "model_summary": {
            "best_model": model_metrics.get("best_model_selected"),
            "roc_auc": model_metrics.get("roc_auc"),
            "cv_roc_auc_mean": model_metrics.get("cv_roc_auc_mean"),
            "cv_roc_auc_std": model_metrics.get("cv_roc_auc_std")
        }
    }

    if sentiment:
        filtered_sentiment = sentiment_df[
            sentiment_df["classification"].str.lower() == sentiment.lower()
        ]

        if filtered_sentiment.empty:
            result["sentiment_summary"] = {
                "message": f"No records found for sentiment: {sentiment}"
            }
        else:
            row = filtered_sentiment.iloc[0]

            result["sentiment_summary"] = {
                "classification": row.get("classification"),
                "total_trades": int(row.get("total_trades", 0)),
                "total_pnl": float(row.get("total_pnl", 0)),
                "average_pnl": float(row.get("average_pnl", 0)),
                "win_rate": float(row.get("win_rate", 0)),
                "avg_trade_size": float(row.get("avg_trade_size", 0)),
                "pnl_volatility": float(row.get("pnl_volatility", 0))
            }

    if account:
        filtered_account = trader_df[
            trader_df["account"].astype(str).str.lower() == account.lower()
        ]

        if filtered_account.empty:
            result["account_summary"] = {
                "message": f"No records found for account: {account}"
            }
        else:
            row = filtered_account.iloc[0]

            result["account_summary"] = {
                "account": str(row.get("account")),
                "total_trades": int(row.get("total_trades", 0)),
                "total_pnl": float(row.get("total_pnl", 0)),
                "avg_pnl": float(row.get("avg_pnl", 0)),
                "win_rate": float(row.get("win_rate", 0)),
                "risk_score": float(row.get("risk_score", 0)),
                "risk_level": str(row.get("risk_level"))
            }

    if not sentiment and not account:
        result["message"] = (
            "No filter provided. Use --sentiment or --account "
            "to generate a focused JSON summary."
        )

    return result


def main():
    parser = argparse.ArgumentParser(
        description="CLI tool for trader sentiment analysis summaries"
    )

    parser.add_argument(
        "--sentiment",
        type=str,
        required=False,
        help='Filter by sentiment classification, e.g. "Fear", "Greed", "Extreme Fear"'
    )

    parser.add_argument(
        "--account",
        type=str,
        required=False,
        help="Filter by trader account"
    )

    parser.add_argument(
        "--export",
        action="store_true",
        help="Export result to outputs/json/analyze_result.json"
    )

    args = parser.parse_args()

    try:
        logging.info("Starting CLI analysis")

        result = build_summary(
            sentiment=args.sentiment,
            account=args.account
        )

        output_json = json.dumps(
            result,
            indent=4,
            default=str
        )

        print(output_json)

        if args.export:
            export_path = JSON_DIR / "analyze_result.json"

            with open(export_path, "w") as f:
                json.dump(result, f, indent=4, default=str)

            logging.info(f"Exported analysis result to {export_path}")

        logging.info("CLI analysis completed successfully")

    except Exception as e:
        logging.error(f"CLI analysis failed: {e}")

        error_output = {
            "status": "error",
            "message": str(e)
        }

        print(json.dumps(error_output, indent=4))


if __name__ == "__main__":
    main()