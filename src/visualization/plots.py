import matplotlib.pyplot as plt


def plot_pnl_distribution(df, save_path):
    plt.figure(figsize=(10, 6))

    df["closed_pnl"].hist(bins=100)

    plt.title("PnL Distribution")
    plt.xlabel("Closed PnL")
    plt.ylabel("Frequency")

    plt.tight_layout()
    plt.savefig(save_path)
    plt.show()
    plt.close()


def plot_cumulative_pnl(df, save_path):
    df = df.sort_values("timestamp_dt").copy()

    df["cumulative_pnl"] = df["closed_pnl"].cumsum()

    plt.figure(figsize=(12, 6))

    plt.plot(df["timestamp_dt"], df["cumulative_pnl"])

    plt.title("Cumulative PnL")
    plt.xlabel("Time")
    plt.ylabel("Cumulative PnL")

    plt.tight_layout()
    plt.savefig(save_path)
    plt.show()
    plt.close()


def plot_sentiment_distribution(df, save_path):
    plt.figure(figsize=(10, 6))

    df["classification"].value_counts().plot(kind="bar")

    plt.title("Fear & Greed Sentiment Distribution")
    plt.xlabel("Sentiment Classification")
    plt.ylabel("Count")

    plt.tight_layout()
    plt.savefig(save_path)
    plt.show()
    plt.close()


def plot_sentiment_trend(df, save_path):
    df = df.sort_values("date").copy()

    plt.figure(figsize=(12, 6))

    plt.plot(df["date"], df["value"])

    plt.title("Fear & Greed Index Over Time")
    plt.xlabel("Date")
    plt.ylabel("Sentiment Score")

    plt.tight_layout()
    plt.savefig(save_path)
    plt.show()
    plt.close()

def plot_sentiment_vs_pnl(df, save_path):

    sentiment_pnl = (
        df.groupby("classification")["closed_pnl"]
        .mean()
    )

    plt.figure(figsize=(10, 6))

    sentiment_pnl.plot(kind="bar")

    plt.title("Average PnL by Sentiment")
    plt.xlabel("Sentiment")
    plt.ylabel("Average PnL")

    plt.tight_layout()
    plt.savefig(save_path)
    plt.show()
    plt.close()


def plot_sentiment_vs_trade_size(df, save_path):

    sentiment_size = (
        df.groupby("classification")["size_usd"]
        .mean()
    )

    plt.figure(figsize=(10, 6))

    sentiment_size.plot(kind="bar")

    plt.title("Average Trade Size by Sentiment")
    plt.xlabel("Sentiment")
    plt.ylabel("Average Trade Size")

    plt.tight_layout()
    plt.savefig(save_path)
    plt.show()
    plt.close()

def plot_risk_level_distribution(df, save_path):
    plt.figure(figsize=(10, 6))

    df["risk_level"].value_counts().plot(kind="bar")

    plt.title("Trader Risk Level Distribution")
    plt.xlabel("Risk Level")
    plt.ylabel("Number of Traders")

    plt.tight_layout()
    plt.savefig(save_path)
    plt.show()
    plt.close()


def plot_win_rate_vs_risk(df, save_path):
    plt.figure(figsize=(10, 6))

    plt.scatter(
        df["risk_score"],
        df["win_rate"]
    )

    plt.title("Trader Win Rate vs Risk Score")
    plt.xlabel("Risk Score")
    plt.ylabel("Win Rate")

    plt.tight_layout()
    plt.savefig(save_path)
    plt.show()
    plt.close()