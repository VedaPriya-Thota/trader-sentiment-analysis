from scipy.stats import pearsonr, spearmanr, ttest_ind


def correlation_analysis(df):
    results = {}

    numeric_pairs = [
        ("size_usd", "closed_pnl"),
        ("fee", "closed_pnl"),
        ("value", "closed_pnl"),
        ("value", "size_usd"),
    ]

    for x, y in numeric_pairs:
        clean_df = df[[x, y]].dropna()

        if len(clean_df) > 2:
            pearson_corr, pearson_p = pearsonr(clean_df[x], clean_df[y])
            spearman_corr, spearman_p = spearmanr(clean_df[x], clean_df[y])

            results[f"{x}_vs_{y}"] = {
                "pearson_correlation": pearson_corr,
                "pearson_p_value": pearson_p,
                "spearman_correlation": spearman_corr,
                "spearman_p_value": spearman_p
            }

    return results


def long_short_ttest(df):
    buy_pnl = df[df["side"].str.lower() == "buy"]["closed_pnl"].dropna()
    sell_pnl = df[df["side"].str.lower() == "sell"]["closed_pnl"].dropna()

    t_stat, p_value = ttest_ind(
        buy_pnl,
        sell_pnl,
        equal_var=False
    )

    return {
        "test": "Welch t-test",
        "comparison": "BUY trades vs SELL trades",
        "buy_avg_pnl": float(buy_pnl.mean()),
        "sell_avg_pnl": float(sell_pnl.mean()),
        "t_statistic": float(t_stat),
        "p_value": float(p_value),
        "interpretation": (
            "If p_value < 0.05, BUY and SELL trades have statistically "
            "different average pnl."
        )
    }