import pandas as pd

from src.preprocessing.preprocess_historical import preprocess_historical
from src.preprocessing.preprocess_sentiment import preprocess_sentiment


def test_preprocess_historical_creates_required_columns():
    df = pd.DataFrame({
        "Timestamp": [1710000000000],
        "Timestamp IST": ["2024-03-09 10:00:00"],
        "Execution Price": [100],
        "Size Tokens": [2],
        "Size USD": [200],
        "Start Position": [0],
        "Closed PnL": [20],
        "Fee": [1]
    })

    processed = preprocess_historical(df)

    assert "timestamp_dt" in processed.columns
    assert "date" in processed.columns
    assert "hour" in processed.columns
    assert "net_pnl" in processed.columns
    assert "is_profitable" in processed.columns
    assert processed["net_pnl"].iloc[0] == 19
    assert bool(processed["is_profitable"].iloc[0]) is True


def test_preprocess_sentiment_creates_rolling_columns():
    df = pd.DataFrame({
        "date": ["2024-01-01", "2024-01-02"],
        "value": [40, 50],
        "classification": ["Fear", "Neutral"],
        "timestamp": [1, 2]
    })

    processed = preprocess_sentiment(df)

    assert "sentiment_change" in processed.columns
    assert "rolling_sentiment_7d" in processed.columns
    assert processed["sentiment_change"].iloc[1] == 10