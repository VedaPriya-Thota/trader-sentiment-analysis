# 📊 Trader Sentiment & Profitability Analysis

<div align="center">

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge\&logo=python)
![Machine Learning](https://img.shields.io/badge/Machine-Learning-green?style=for-the-badge)
![Pytest](https://img.shields.io/badge/Tested%20With-Pytest-orange?style=for-the-badge)
![Status](https://img.shields.io/badge/Project-Production%20Style-success?style=for-the-badge)

### 🚀 Quantitative Trading • Behavioral Finance • AI Engineering • Sentiment Analytics

</div>

---

# 📌 Project Overview

This project is a **professional AI/Data Science pipeline** designed to analyze the relationship between:

* 📈 Market Sentiment
* 💰 Trader Profitability
* ⚠️ Risk-Taking Behavior
* 🧠 Behavioral Finance Patterns
* 📊 Trade Size & Volatility
* 🤖 Machine Learning Profitability Prediction

The system combines:

1. Historical trading activity
2. Fear & Greed sentiment data

to generate:

* quant-style insights
* behavioral analytics
* trader risk scoring
* statistical testing
* machine learning predictions
* automated visualizations
* production-grade JSON reports

---

# 🎯 Project Objectives

The primary goal is to understand:

✅ How sentiment affects trader behavior
✅ Whether greed increases risk-taking
✅ Whether fear reduces trade exposure
✅ Which traders are consistently profitable
✅ Whether profitability can be predicted using behavioral features

This project was built with a strong focus on:

* AI engineering workflows
* modular architecture
* reproducibility
* structured outputs
* recruiter-grade implementation

---

# 🗂️ Datasets Used

## 1️⃣ historical_data.csv

Contains trader transaction-level data.

### Main Fields

| Column          | Description           |
| --------------- | --------------------- |
| Account         | Trader wallet/account |
| Coin            | Traded asset          |
| Execution Price | Trade execution price |
| Size USD        | Trade exposure        |
| Side            | BUY/SELL direction    |
| Closed PnL      | Realized profit/loss  |
| Fee             | Trading fee           |
| Timestamp       | Trade timestamp       |

---

## 2️⃣ fear_greed_index.csv

Contains market sentiment data.

### Main Fields

| Column         | Description       |
| -------------- | ----------------- |
| Date           | Daily timestamp   |
| Value          | Sentiment score   |
| Classification | Fear/Greed regime |
| Timestamp      | Epoch timestamp   |

---
# 📥 Dataset Access

The datasets are not uploaded to GitHub because:

- file sizes may be large
- repositories should remain lightweight
- raw datasets may contain external/private data

You can download the datasets here:

## Google Drive Link

https://drive.google.com/file/d/1IAfLZwu6rJzyWKgBToqwSmmVYU6VbjVs/view?usp=sharing
https://drive.google.com/file/d/1PgQC0tO8XN-wqkNyghWc_-mnrYv_nhSf/view?usp=sharing

After downloading, place the CSV files inside:

```text
data/raw/

# 🏗️ Project Architecture

```text
trader-sentiment-analysis/
│
├── assets/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── outputs/
│   ├── figures/
│   ├── reports/
│   └── json/
│
├── src/
│   ├── preprocessing/
│   ├── eda/
│   ├── features/
│   ├── models/
│   ├── visualization/
│   └── utils/
│
├── tests/
│   ├── conftest.py
│   ├── test_preprocessing.py
│   ├── test_features.py
│   └── test_models.py
│
├── main.py
├── requirements.txt
├── README.md
├── config.yaml
└── .gitignore
```

---

# ⚙️ Features Implemented

# 1️⃣ Historical Trading Analysis

Analyzes:

* dataset structure
* missing values
* duplicates
* pnl distributions
* cumulative pnl
* account-level profitability
* trader performance behavior

### Generated Outputs

✅ Dataset summary JSON
✅ PnL summary JSON
✅ Account-level CSV reports
✅ PnL distribution chart
✅ Cumulative PnL chart

---

# 2️⃣ Fear & Greed Sentiment Analysis

Analyzes:

* sentiment distribution
* sentiment trends
* rolling sentiment behavior
* market psychology regimes

### Generated Outputs

✅ Sentiment summary JSON
✅ Sentiment distribution chart
✅ Sentiment trend chart

---

# 3️⃣ Behavioral Finance Analysis

Trading data is merged with market sentiment data.

### Key Questions Analyzed

* Does greed increase trade size?
* Are traders more profitable during fear?
* Does sentiment affect risk-taking?
* Do traders behave differently in different sentiment regimes?

### Generated Outputs

✅ Sentiment vs PnL analysis
✅ Sentiment vs trade size analysis
✅ Behavioral CSV reports
✅ Behavioral visualizations

---

# 4️⃣ Statistical Testing

Implemented professional statistical testing:

| Test                 | Purpose                              |
| -------------------- | ------------------------------------ |
| Pearson Correlation  | Linear relationships                 |
| Spearman Correlation | Rank/monotonic relationships         |
| Welch T-Test         | BUY vs SELL profitability comparison |

### Relationships Studied

* trade size vs pnl
* fees vs pnl
* sentiment vs pnl
* sentiment vs trade size
* BUY vs SELL profitability

---

# 5️⃣ Trader Risk Scoring

Created advanced trader-level risk metrics.

### Risk Features

* pnl volatility
* average trade size
* max trade size
* fee efficiency
* consistency score
* risk score
* risk level

### Risk Levels

```text
low
medium
high
extreme
```

### Generated Outputs

✅ Trader risk summary CSV
✅ Risk distribution chart
✅ Win rate vs risk chart

---

# 6️⃣ Machine Learning Pipeline

Implemented a Random Forest classifier to predict whether a trade is profitable.

## 🎯 Target

```text
is_profitable
```

## 📌 Features Used

```text
size_usd
fee
hour
sentiment value
```

## 📊 Metrics Generated

* Accuracy
* Precision
* Recall
* F1-Score
* ROC-AUC

### Generated Outputs

✅ Model evaluation JSON
✅ Feature importance CSV

---

# 7️⃣ Automated Visualization System

The pipeline automatically:

* generates charts
* saves figures
* displays plots during execution

### Visualizations Included

📈 PnL Distribution
📈 Cumulative PnL
📈 Sentiment Distribution
📈 Sentiment Trends
📈 Sentiment vs PnL
📈 Sentiment vs Trade Size
📈 Risk Distribution
📈 Win Rate vs Risk

Plots are displayed automatically using:

```python
plt.show()
```

---

# 🧪 Testing

Implemented automated testing using `pytest`.

## Test Files

```text
tests/test_preprocessing.py
tests/test_features.py
tests/test_models.py
```

## What Is Tested

✅ preprocessing correctness
✅ feature engineering
✅ dataset merging
✅ risk scoring
✅ ML model outputs

## Run Tests

```bash
pytest
```

### Expected Output

```text
5 passed
```

This demonstrates:

* reproducibility
* engineering reliability
* production-style validation
* software testing discipline

---

# 🚀 Installation

## 1️⃣ Clone Repository

```bash
git clone YOUR_REPOSITORY_LINK
```

---

## 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

---

## 3️⃣ Activate Environment

```bash
venv\Scripts\activate
```

---

## 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ How To Run

## Run Full Pipeline

```bash
python main.py
```

## Run Using CLI

```bash
python main.py --phase all
```

---

# 🖼️ View Generated Plots

All visualizations are saved inside:

```text
outputs/figures/
```

## Quick Way To Open All Plots

```powershell
explorer outputs\figures
```

This opens all generated figures directly in Windows Explorer.

---

# 📁 Output Files

# JSON Outputs

```text
outputs/json/dataset_summary.json
outputs/json/pnl_summary.json
outputs/json/sentiment_summary.json
outputs/json/correlation_analysis.json
outputs/json/long_short_ttest.json
outputs/json/profitability_model_metrics.json
```

---

# CSV Reports

```text
outputs/reports/account_summary.csv
outputs/reports/sentiment_pnl_analysis.csv
outputs/reports/sentiment_behavior_analysis.csv
outputs/reports/trader_risk_summary.csv
outputs/reports/feature_importance.csv
```

---

# 📊 Generated Figures

```text
outputs/figures/pnl_distribution.png
outputs/figures/cumulative_pnl.png
outputs/figures/sentiment_distribution.png
outputs/figures/sentiment_trend.png
outputs/figures/sentiment_vs_pnl.png
outputs/figures/sentiment_vs_trade_size.png
outputs/figures/risk_level_distribution.png
outputs/figures/win_rate_vs_risk.png
```

---

# ⚠️ Important Note About Datasets

The following folders are intentionally excluded from GitHub using `.gitignore`:

```text
data/raw/
data/processed/
```

Reason:

* datasets may be large
* datasets may contain private data
* repositories remain lightweight
* improves Git performance

To run the project locally, place the CSV files inside:

```text
data/raw/
```

Required files:

```text
historical_data.csv
fear_greed_index.csv
```

---

# 📈 Key Business Insights

This project helps answer:

✅ Are traders more profitable during fear or greed?
✅ Does greed increase trade size?
✅ Are high-risk traders consistently profitable?
✅ Does sentiment influence trading behavior?
✅ Can profitability be predicted using sentiment data?

---

# 🤖 AI Engineering Alignment

This project demonstrates:

* modular architecture
* preprocessing pipelines
* logging systems
* structured JSON outputs
* machine learning workflows
* statistical evaluation
* CLI tooling
* automated visualizations
* testing with pytest
* reproducible engineering workflows

---

# 🔮 Future Improvements

Planned upgrades:

* XGBoost model
* trader clustering
* anomaly detection
* Streamlit dashboard
* FastAPI backend
* Docker deployment
* automated PDF reports
* RAG-based insight retrieval
* advanced quant metrics
* scheduled reporting system

---

# 🏁 Conclusion

This project was designed as a **professional-grade AI & quantitative analytics system** rather than a simple notebook-style EDA project.

It combines:

* 📊 Quantitative Finance
* 🧠 Behavioral Finance
* 🤖 Machine Learning
* 📈 Statistical Analysis
* ⚙️ Software Engineering
* 🧪 Automated Testing
* 📂 Structured Reporting

into a recruiter-grade portfolio project suitable for:

* AI Engineering roles
* Data Science internships
* Quantitative Research internships
* ML Engineering opportunities



