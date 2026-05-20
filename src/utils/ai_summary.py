def generate_ai_summary(
    pnl_summary,
    sentiment_pnl_df,
    trader_risk_df,
    quant_metrics,
    model_metrics
):
    insights = []

    total_pnl = pnl_summary.get("total_pnl", 0)
    win_rate = pnl_summary.get("win_rate", 0)

    insights.append(
        f"The dataset generated total realized PnL of {total_pnl:,.2f} "
        f"with an overall win rate of {win_rate * 100:.2f}%."
    )

    if not sentiment_pnl_df.empty:
        best_sentiment = sentiment_pnl_df.sort_values(
            "average_pnl",
            ascending=False
        ).iloc[0]

        insights.append(
            f"The strongest profitability regime was {best_sentiment['classification']}, "
            f"with average PnL of {best_sentiment['average_pnl']:.2f}."
        )

    if not trader_risk_df.empty:
        extreme_count = int(
            (trader_risk_df["risk_level"] == "extreme").sum()
        )

        insights.append(
            f"{extreme_count} traders were classified as extreme-risk, "
            f"meaning they should be prioritized for deeper risk review."
        )

    profit_factor = quant_metrics.get("profit_factor", 0)
    max_drawdown = quant_metrics.get("max_drawdown", 0)

    insights.append(
        f"The profit factor is {profit_factor:.3f}, while maximum drawdown is {max_drawdown:,.2f}, "
        f"showing the balance between profitability and downside risk."
    )

    auc = model_metrics.get("roc_auc", 0)

    insights.append(
        f"The ML model achieved ROC-AUC of {auc:.3f}, indicating its ability "
        f"to rank profitable and non-profitable trades."
    )

    return {
        "executive_summary": insights,
        "final_recommendation": (
            "Monitor extreme-risk traders, evaluate sentiment-driven trade behavior, "
            "and use ML predictions as decision-support rather than absolute trading signals."
        )
    }