def sentiment_pnl_analysis(df):

    analysis = (
        df.groupby("classification")
        .agg(
            total_trades=("closed_pnl", "count"),

            total_pnl=("closed_pnl", "sum"),

            average_pnl=("closed_pnl", "mean"),

            median_pnl=("closed_pnl", "median"),

            win_rate=("is_profitable", "mean"),

            avg_trade_size=("size_usd", "mean"),

            pnl_volatility=("closed_pnl", "std")
        )
        .reset_index()
    )

    return analysis


def sentiment_behavior_analysis(df):

    behavior = (
        df.groupby("classification")
        .agg(
            avg_fee=("fee", "mean"),

            avg_position_size=("size_usd", "mean"),

            profitable_trades=("is_profitable", "sum"),

            losing_trades=("is_profitable",
                            lambda x: (~x).sum())
        )
        .reset_index()
    )

    return behavior