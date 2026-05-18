def sentiment_summary(df):
    return {
        "shape": df.shape,
        "columns": list(df.columns),
        "missing_values": df.isnull().sum().to_dict(),
        "sentiment_distribution": df["classification"].value_counts().to_dict(),
        "average_sentiment_score": float(df["value"].mean()),
        "min_sentiment_score": float(df["value"].min()),
        "max_sentiment_score": float(df["value"].max())
    }