def merge_trading_sentiment(
    historical_df,
    sentiment_df
):

    merged_df = historical_df.merge(
        sentiment_df,
        on="date",
        how="left"
    )

    return merged_df