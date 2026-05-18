import pandas as pd


def create_trader_risk_features(df: pd.DataFrame) -> pd.DataFrame:
    trader_df = (
        df.groupby("account")
        .agg(
            total_trades=("closed_pnl", "count"),
            total_pnl=("closed_pnl", "sum"),
            avg_pnl=("closed_pnl", "mean"),
            pnl_volatility=("closed_pnl", "std"),
            win_rate=("is_profitable", "mean"),
            avg_trade_size=("size_usd", "mean"),
            max_trade_size=("size_usd", "max"),
            total_fees=("fee", "sum"),
            avg_sentiment=("value", "mean")
        )
        .reset_index()
    )

    trader_df["pnl_volatility"] = trader_df["pnl_volatility"].fillna(0)

    trader_df["consistency_score"] = (
        trader_df["avg_pnl"] /
        trader_df["pnl_volatility"].replace(0, pd.NA)
    ).fillna(0)

    trader_df["fee_efficiency"] = (
        trader_df["total_pnl"] /
        trader_df["total_fees"].replace(0, pd.NA)
    ).fillna(0)

    trader_df["risk_score"] = (
        trader_df["pnl_volatility"].rank(pct=True) * 0.4 +
        trader_df["avg_trade_size"].rank(pct=True) * 0.3 +
        trader_df["max_trade_size"].rank(pct=True) * 0.3
    )

    trader_df["risk_level"] = pd.cut(
        trader_df["risk_score"],
        bins=[0, 0.25, 0.5, 0.75, 1.0],
        labels=["low", "medium", "high", "extreme"],
        include_lowest=True
    )

    return trader_df