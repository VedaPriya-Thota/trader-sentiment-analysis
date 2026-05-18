import pandas as pd

def preprocess_sentiment(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df.columns = df.columns.str.strip().str.lower()

    df["date"] = pd.to_datetime(df["date"], errors="coerce").dt.date
    df["value"] = pd.to_numeric(df["value"], errors="coerce")

    df["sentiment_change"] = df["value"].diff()
    df["rolling_sentiment_7d"] = df["value"].rolling(7).mean()
    df["rolling_sentiment_30d"] = df["value"].rolling(30).mean()

    return df