import pandas as pd


def calculate_quant_metrics(df: pd.DataFrame) -> dict:
    df = df.copy()

    df = df.sort_values("timestamp_dt")

    df["cumulative_pnl"] = df["closed_pnl"].cumsum()

    df["running_max"] = df["cumulative_pnl"].cummax()

    df["drawdown"] = df["cumulative_pnl"] - df["running_max"]

    total_pnl = df["closed_pnl"].sum()

    avg_pnl = df["closed_pnl"].mean()

    pnl_std = df["closed_pnl"].std()

    gross_profit = df[df["closed_pnl"] > 0]["closed_pnl"].sum()

    gross_loss = abs(df[df["closed_pnl"] < 0]["closed_pnl"].sum())

    profit_factor = (
        gross_profit / gross_loss
        if gross_loss != 0
        else None
    )

    sharpe_like_ratio = (
        avg_pnl / pnl_std
        if pnl_std != 0
        else None
    )

    max_drawdown = df["drawdown"].min()

    expectancy = avg_pnl

    win_rate = (df["closed_pnl"] > 0).mean()

    loss_rate = (df["closed_pnl"] < 0).mean()

    avg_win = df[df["closed_pnl"] > 0]["closed_pnl"].mean()

    avg_loss = abs(df[df["closed_pnl"] < 0]["closed_pnl"].mean())

    payoff_ratio = (
        avg_win / avg_loss
        if avg_loss != 0
        else None
    )

    return {
        "total_pnl": float(total_pnl),
        "average_pnl": float(avg_pnl),
        "pnl_volatility": float(pnl_std),
        "sharpe_like_ratio": float(sharpe_like_ratio) if sharpe_like_ratio is not None else None,
        "max_drawdown": float(max_drawdown),
        "profit_factor": float(profit_factor) if profit_factor is not None else None,
        "expectancy_per_trade": float(expectancy),
        "win_rate": float(win_rate),
        "loss_rate": float(loss_rate),
        "average_win": float(avg_win),
        "average_loss": float(avg_loss),
        "payoff_ratio": float(payoff_ratio) if payoff_ratio is not None else None
    }


def create_drawdown_series(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df = df.sort_values("timestamp_dt")

    df["cumulative_pnl"] = df["closed_pnl"].cumsum()

    df["running_max"] = df["cumulative_pnl"].cummax()

    df["drawdown"] = df["cumulative_pnl"] - df["running_max"]

    return df[[
        "timestamp_dt",
        "cumulative_pnl",
        "running_max",
        "drawdown"
    ]]