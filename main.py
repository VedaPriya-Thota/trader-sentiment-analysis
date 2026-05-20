import json
import logging
import argparse

from src.utils.data_loader import load_csv

from src.preprocessing.preprocess_historical import preprocess_historical
from src.preprocessing.preprocess_sentiment import preprocess_sentiment

from src.eda.historical_eda import (
    dataset_summary,
    pnl_summary,
    account_summary
)

from src.eda.sentiment_eda import sentiment_summary

from src.features.merge_features import merge_trading_sentiment
from src.features.risk_features import create_trader_risk_features

from src.eda.merged_eda import (
    sentiment_pnl_analysis,
    sentiment_behavior_analysis
)

from src.eda.statistical_tests import (
    correlation_analysis,
    long_short_ttest
)

from src.eda.quant_metrics import (
    calculate_quant_metrics,
    create_drawdown_series
)

from src.models.profitability_model import train_profitability_model
from src.models.trader_segmentation import segment_traders

from src.utils.ai_summary import generate_ai_summary

from src.visualization.plots import (
    plot_pnl_distribution,
    plot_cumulative_pnl,
    plot_sentiment_distribution,
    plot_sentiment_trend,
    plot_sentiment_vs_pnl,
    plot_sentiment_vs_trade_size,
    plot_risk_level_distribution,
    plot_win_rate_vs_risk,
    plot_drawdown,
    plot_correlation_heatmap
)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def save_json(data, path):
    with open(path, "w") as f:
        json.dump(data, f, indent=4, default=str)


def main():

    historical_path = "data/raw/historical_data.csv"
    sentiment_path = "data/raw/fear_greed_index.csv"

    # Historical analysis
    historical_df = load_csv(historical_path)
    historical_df = preprocess_historical(historical_df)

    dataset_info = dataset_summary(historical_df)
    pnl_info = pnl_summary(historical_df)
    account_info = account_summary(historical_df)

    save_json(
        dataset_info,
        "outputs/json/dataset_summary.json"
    )

    save_json(
        pnl_info,
        "outputs/json/pnl_summary.json"
    )

    account_info.to_csv(
        "outputs/reports/account_summary.csv",
        index=False
    )

    plot_pnl_distribution(
        historical_df,
        "outputs/figures/pnl_distribution.png"
    )

    plot_cumulative_pnl(
        historical_df,
        "outputs/figures/cumulative_pnl.png"
    )

    # Sentiment analysis
    sentiment_df = load_csv(sentiment_path)
    sentiment_df = preprocess_sentiment(sentiment_df)

    sentiment_info = sentiment_summary(sentiment_df)

    save_json(
        sentiment_info,
        "outputs/json/sentiment_summary.json"
    )

    plot_sentiment_distribution(
        sentiment_df,
        "outputs/figures/sentiment_distribution.png"
    )

    plot_sentiment_trend(
        sentiment_df,
        "outputs/figures/sentiment_trend.png"
    )

    # Merged analysis
    merged_df = merge_trading_sentiment(
        historical_df,
        sentiment_df
    )

    sentiment_pnl_df = sentiment_pnl_analysis(merged_df)

    sentiment_behavior_df = sentiment_behavior_analysis(merged_df)

    sentiment_pnl_df.to_csv(
        "outputs/reports/sentiment_pnl_analysis.csv",
        index=False
    )

    sentiment_behavior_df.to_csv(
        "outputs/reports/sentiment_behavior_analysis.csv",
        index=False
    )

    plot_sentiment_vs_pnl(
        merged_df,
        "outputs/figures/sentiment_vs_pnl.png"
    )

    plot_sentiment_vs_trade_size(
        merged_df,
        "outputs/figures/sentiment_vs_trade_size.png"
    )

    # Statistical analysis
    correlation_results = correlation_analysis(merged_df)

    ttest_results = long_short_ttest(merged_df)

    save_json(
        correlation_results,
        "outputs/json/correlation_analysis.json"
    )

    save_json(
        ttest_results,
        "outputs/json/long_short_ttest.json"
    )

    # Trader risk scoring
    trader_risk_df = create_trader_risk_features(merged_df)

    trader_risk_df.to_csv(
        "outputs/reports/trader_risk_summary.csv",
        index=False
    )

    plot_risk_level_distribution(
        trader_risk_df,
        "outputs/figures/risk_level_distribution.png"
    )

    plot_win_rate_vs_risk(
        trader_risk_df,
        "outputs/figures/win_rate_vs_risk.png"
    )

    # ML profitability prediction
    model_metrics, feature_importance = train_profitability_model(
        merged_df
    )

    save_json(
        model_metrics,
        "outputs/json/profitability_model_metrics.json"
    )

    feature_importance.to_csv(
        "outputs/reports/feature_importance.csv",
        index=False
    )

    # Advanced quant metrics
    quant_metrics = calculate_quant_metrics(merged_df)

    drawdown_df = create_drawdown_series(merged_df)

    save_json(
        quant_metrics,
        "outputs/json/quant_metrics.json"
    )

    drawdown_df.to_csv(
        "outputs/reports/drawdown_series.csv",
        index=False
    )

    plot_drawdown(
        drawdown_df,
        "outputs/figures/drawdown.png"
    )

    plot_correlation_heatmap(
        merged_df,
        "outputs/figures/correlation_heatmap.png"
    )

    # Trader segmentation
    segmented_traders, segment_summary = segment_traders(
        trader_risk_df
    )

    segmented_traders.to_csv(
        "outputs/reports/segmented_traders.csv",
        index=False
    )

    segment_summary.to_csv(
        "outputs/reports/trader_segment_summary.csv",
        index=False
    )

    # AI executive summary
    ai_summary = generate_ai_summary(
        pnl_info,
        sentiment_pnl_df,
        trader_risk_df,
        quant_metrics,
        model_metrics
    )

    save_json(
        ai_summary,
        "outputs/json/ai_executive_summary.json"
    )

    print(
        "Full AI trader intelligence pipeline completed successfully."
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Trader Sentiment Analysis CLI"
    )

    parser.add_argument(
        "--phase",
        type=str,
        default="all",
        choices=["all"],
        help="Pipeline phase to run"
    )

    args = parser.parse_args()

    if args.phase == "all":
        main()