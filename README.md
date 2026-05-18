
````md
# Trader Sentiment & Profitability Analysis

A professional AI/Data Science project that analyzes the relationship between market sentiment, trader behavior, profitability, risk-taking, and leverage-style exposure.

This project combines:

- Quant-style analytics
- Behavioral finance insights
- Statistical testing
- Machine learning
- Risk scoring
- Sentiment analysis
- Production-grade software engineering workflows

The project is designed to align with AI engineering and data science internship responsibilities including:

- AI prototyping
- structured JSON outputs
- evaluation workflows
- modular architecture
- logging
- testing
- CLI tooling
- reproducibility

---

# Project Objective

The objective is to study how market sentiment influences:

- trader profitability
- trading behavior
- risk-taking
- trade size
- volatility
- consistency
- leverage-like exposure

The project merges:

1. Historical trading activity
2. Fear & Greed market sentiment data

to generate behavioral finance and quant-style insights.

---

# Datasets

## 1. historical_data.csv

Contains historical trader transaction data.

### Main Columns

- Account
- Coin
- Execution Price
- Size Tokens
- Size USD
- Side
- Closed PnL
- Fee
- Timestamp

---

## 2. fear_greed_index.csv

Contains market sentiment data.

### Main Columns

- Date
- Sentiment Value
- Classification
- Timestamp

---

# Project Structure

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
├── config.yaml
├── README.md
└── .gitignore
````

---

# Features Implemented

# 1. Historical Trading Analysis

Analyzes:

* dataset shape
* missing values
* duplicates
* PnL distribution
* cumulative PnL
* account-level performance
* trade behavior
* profitability

Generated Outputs:

* dataset summary JSON
* pnl summary JSON
* account summary CSV
* cumulative PnL chart
* PnL distribution chart

---

# 2. Fear & Greed Sentiment Analysis

Analyzes:

* sentiment distribution
* sentiment trends
* rolling sentiment behavior
* market psychology regimes

Generated Outputs:

* sentiment summary JSON
* sentiment distribution chart
* sentiment trend chart

---

# 3. Merged Behavioral Finance Analysis

Merges sentiment data with trading data using date alignment.

Analyzes:

* sentiment vs pnl
* sentiment vs trade size
* sentiment vs trader behavior
* sentiment vs risk-taking

Generated Outputs:

* sentiment behavior CSV
* sentiment pnl analysis CSV
* sentiment vs pnl chart
* sentiment vs trade size chart

---

# 4. Statistical Testing

Implemented Tests:

* Pearson Correlation
* Spearman Correlation
* Welch T-Test

Relationships analyzed:

* trade size vs pnl
* fees vs pnl
* sentiment vs pnl
* sentiment vs trade size
* BUY vs SELL profitability

Generated Outputs:

* correlation analysis JSON
* long-short t-test JSON

---

# 5. Trader Risk Scoring

Created advanced trader-level metrics:

* total pnl
* pnl volatility
* average trade size
* max trade size
* consistency score
* fee efficiency
* risk score
* risk level

Risk Levels:

```text
low
medium
high
extreme
```

Generated Outputs:

* trader risk summary CSV
* risk level distribution chart
* win rate vs risk chart

---

# 6. Machine Learning Pipeline

Built a Random Forest profitability prediction model.

### Target

```text
is_profitable
```

### Features Used

```text
size_usd
fee
hour
sentiment value
```

### Metrics Generated

* Accuracy
* Precision
* Recall
* F1-score
* ROC-AUC

Generated Outputs:

* profitability model metrics JSON
* feature importance CSV

---

# 7. Automated Visualization System

The pipeline automatically generates charts and saves them inside:

```text
outputs/figures/
```

Visualizations include:

* PnL Distribution
* Cumulative PnL
* Sentiment Distribution
* Sentiment Trends
* Sentiment vs PnL
* Sentiment vs Trade Size
* Risk Distribution
* Win Rate vs Risk

Plots are also displayed automatically during execution using:

```python
plt.show()
```

---

# Quick Way To View All Generated Plots

Run:

```powershell
explorer outputs\figures
```

This opens all generated visualizations directly in Windows Explorer.

---

# Testing

Implemented automated testing using `pytest`.

### Test Files

```text
tests/test_preprocessing.py
tests/test_features.py
tests/test_models.py
```

### What Is Tested

* preprocessing correctness
* feature engineering
* dataset merging
* risk feature creation
* ML model output validation

### Run Tests

```bash
pytest
```

Expected Output:

```text
5 passed
```

This demonstrates:

* reliability
* reproducibility
* engineering maturity
* production-style validation

---

# Installation

## Create Virtual Environment

```bash
python -m venv venv
```

## Activate Environment

```bash
venv\Scripts\activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# How To Run

## Run Full Pipeline

```bash
python main.py
```

## Run Using CLI

```bash
python main.py --phase all
```

---

# Output Files

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

# Generated Figures

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

# Key Business Insights

This project helps answer:

* Are traders more profitable during fear or greed?
* Does greed increase trade size?
* Are high-risk traders truly profitable?
* Do BUY and SELL trades differ statistically?
* Does sentiment influence risk-taking?
* Can profitability be predicted using sentiment and behavioral data?

---

# AI Engineering Alignment

This project demonstrates:

* modular architecture
* clean preprocessing pipelines
* logging systems
* structured JSON outputs
* ML workflows
* evaluation pipelines
* statistical testing
* CLI support
* automated reporting
* testing with pytest
* reproducible engineering workflows

---

# Future Improvements

Planned improvements include:

* XGBoost model
* trader clustering
* anomaly detection
* Streamlit dashboard
* FastAPI backend
* Docker support
* PDF report generation
* RAG-based insight retrieval
* advanced quant metrics
* automated scheduled reporting

---

# Conclusion

This project is designed as a professional-grade AI and quant analytics system rather than a basic notebook-style EDA project.

It combines:

* behavioral finance
* quantitative analytics
* machine learning
* statistical validation
* risk scoring
* automated reporting
* software engineering best practices

to create a recruiter-grade data science and AI engineering portfolio project.

```
```

