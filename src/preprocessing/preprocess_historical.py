import pandas as pd

def preprocess_historical(df: pd.DataFrame) -> pd.DataFrame:

    df = df.copy()

    # Standardize columns
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

    # Convert timestamps
    if "timestamp" in df.columns:
        df["timestamp_dt"] = pd.to_datetime(
            df["timestamp"],
            unit="ms",
            errors="coerce"
        )

    # Convert IST timestamp
    if "timestamp_ist" in df.columns:
        df["timestamp_ist_dt"] = pd.to_datetime(
            df["timestamp_ist"],
            errors="coerce"
        )

    # Date features
    if "timestamp_dt" in df.columns:

        df["date"] = df["timestamp_dt"].dt.date
        df["hour"] = df["timestamp_dt"].dt.hour
        df["day"] = df["timestamp_dt"].dt.day
        df["month"] = df["timestamp_dt"].dt.month
        df["weekday"] = df["timestamp_dt"].dt.day_name()

    # Numeric columns
    numeric_cols = [
        "execution_price",
        "size_tokens",
        "size_usd",
        "start_position",
        "closed_pnl",
        "fee"
    ]

    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(
                df[col],
                errors="coerce"
            )

    # Remove duplicates
    df = df.drop_duplicates()

    # Feature Engineering
    if "closed_pnl" in df.columns and "fee" in df.columns:
        df["net_pnl"] = df["closed_pnl"] - df["fee"]

    if "closed_pnl" in df.columns:
        df["is_profitable"] = df["closed_pnl"] > 0

    if "closed_pnl" in df.columns and "size_usd" in df.columns:

        df["pnl_ratio"] = (
            df["closed_pnl"] /
            df["size_usd"].replace(0, pd.NA)
        )

    return df