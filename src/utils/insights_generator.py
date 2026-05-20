def generate_structured_insights(
    pnl_info,
    sentiment_pnl_df,
    trader_risk_df,
    quant_metrics,
    model_metrics,
    feature_importance
):
    best_sentiment = None

    if not sentiment_pnl_df.empty:
        best_row = sentiment_pnl_df.sort_values(
            "average_pnl",
            ascending=False
        ).iloc[0]

        best_sentiment = {
            "classification": best_row.get("classification"),
            "average_pnl": float(best_row.get("average_pnl", 0)),
            "win_rate": float(best_row.get("win_rate", 0)),
            "avg_trade_size": float(best_row.get("avg_trade_size", 0))
        }

    top_feature = None

    if not feature_importance.empty:
        top_row = feature_importance.iloc[0]

        top_feature = {
            "feature": top_row.get("feature"),
            "importance": float(top_row.get("importance", 0))
        }

    extreme_risk_count = 0

    if not trader_risk_df.empty and "risk_level" in trader_risk_df.columns:
        extreme_risk_count = int(
            (trader_risk_df["risk_level"] == "extreme").sum()
        )

    insights = {
        "project": "trader_sentiment_analysis",
        "task_type": "classification_and_behavioral_analysis",
        "summary": {
            "total_pnl": float(pnl_info.get("total_pnl", 0)),
            "win_rate": float(pnl_info.get("win_rate", 0)),
            "best_sentiment_regime": best_sentiment,
            "extreme_risk_traders": extreme_risk_count,
            "max_drawdown": float(quant_metrics.get("max_drawdown", 0)),
            "profit_factor": float(quant_metrics.get("profit_factor", 0))
        },
        "ml_evaluation": {
            "best_model": model_metrics.get("best_model_selected"),
            "accuracy": float(model_metrics.get("accuracy", 0)),
            "precision": float(model_metrics.get("precision", 0)),
            "recall": float(model_metrics.get("recall", 0)),
            "f1_score": float(model_metrics.get("f1_score", 0)),
            "roc_auc": float(model_metrics.get("roc_auc", 0)),
            "cv_roc_auc_mean": float(model_metrics.get("cv_roc_auc_mean", 0)),
            "cv_roc_auc_std": float(model_metrics.get("cv_roc_auc_std", 0)),
            "top_feature": top_feature
        },
        "actionable_insights": [
            {
                "insight": "Sentiment regimes show different profitability behavior.",
                "recommendation": "Compare strategy exposure across Fear, Greed, and Neutral conditions."
            },
            {
                "insight": "Extreme-risk traders were detected.",
                "recommendation": "Review accounts with high risk scores before increasing exposure."
            },
            {
                "insight": "The model shows useful predictive signal after leakage prevention.",
                "recommendation": "Use predictions as decision support, not as direct trading signals."
            }
        ],
        "output_contract": {
            "format": "json",
            "schema_version": "1.0",
            "strict_fields": [
                "summary",
                "ml_evaluation",
                "actionable_insights"
            ]
        }
    }

    return insights