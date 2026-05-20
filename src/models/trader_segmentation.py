import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler


def segment_traders(trader_risk_df: pd.DataFrame):
    df = trader_risk_df.copy()

    features = [
        "total_trades",
        "total_pnl",
        "avg_pnl",
        "pnl_volatility",
        "win_rate",
        "avg_trade_size",
        "risk_score"
    ]

    df = df.dropna(subset=features)

    X = df[features]

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    kmeans = KMeans(
        n_clusters=4,
        random_state=42,
        n_init=10
    )

    df["cluster"] = kmeans.fit_predict(X_scaled)

    cluster_names = {
        0: "Balanced Traders",
        1: "High-Risk Traders",
        2: "Consistent Performers",
        3: "Low-Activity Traders"
    }

    df["trader_segment"] = df["cluster"].map(cluster_names)

    segment_summary = (
        df.groupby("trader_segment")
        .agg(
            trader_count=("account", "count"),
            avg_total_pnl=("total_pnl", "mean"),
            avg_win_rate=("win_rate", "mean"),
            avg_risk_score=("risk_score", "mean"),
            avg_trade_size=("avg_trade_size", "mean")
        )
        .reset_index()
    )

    return df, segment_summary