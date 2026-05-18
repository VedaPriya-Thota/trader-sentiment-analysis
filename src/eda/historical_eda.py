def dataset_summary(df):

    return {
        "shape": df.shape,
        "columns": list(df.columns),
        "missing_values": (
            df.isnull().sum().to_dict()
        ),
        "duplicates": int(df.duplicated().sum())
    }


def pnl_summary(df):

    return {

        "total_pnl": float(df["closed_pnl"].sum()),
        "average_pnl": float(df["closed_pnl"].mean()),
        "median_pnl": float(df["closed_pnl"].median()),
        "max_profit": float(df["closed_pnl"].max()),
        "max_loss": float(df["closed_pnl"].min()),

        "win_rate": float(
            (df["closed_pnl"] > 0).mean()
        )
    }


def account_summary(df):

    account_df = (
        df.groupby("account")
        .agg(
            total_trades=("closed_pnl", "count"),
            total_pnl=("closed_pnl", "sum"),
            average_pnl=("closed_pnl", "mean"),
            win_rate=("is_profitable", "mean"),
            avg_trade_size=("size_usd", "mean"),
            pnl_volatility=("closed_pnl", "std")
        )
        .reset_index()
    )

    return account_df