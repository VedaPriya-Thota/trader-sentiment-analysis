import pandas as pd

from src.features.merge_features import merge_trading_sentiment
from src.features.risk_features import create_trader_risk_features


def test_merge_trading_sentiment():
    historical_df = pd.DataFrame({
        "date": [pd.to_datetime("2024-01-01").date()],
        "closed_pnl": [100]
    })

    sentiment_df = pd.DataFrame({
        "date": [pd.to_datetime("2024-01-01").date()],
        "value": [70],
        "classification": ["Greed"]
    })

    merged = merge_trading_sentiment(historical_df, sentiment_df)

    assert "value" in merged.columns
    assert "classification" in merged.columns
    assert merged["classification"].iloc[0] == "Greed"


def test_create_trader_risk_features():
    df = pd.DataFrame({
        "account": ["A", "A", "B"],
        "closed_pnl": [100, -50, 20],
        "is_profitable": [True, False, True],
        "size_usd": [1000, 1500, 500],
        "fee": [2, 3, 1],
        "value": [60, 65, 40]
    })

    risk_df = create_trader_risk_features(df)

    assert "risk_score" in risk_df.columns
    assert "risk_level" in risk_df.columns
    assert "consistency_score" in risk_df.columns