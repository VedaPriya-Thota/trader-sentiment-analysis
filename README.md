````md
# Trader Sentiment Analysis

<div align="center">

![Python](https://img.shields.io/badge/Python-3.11-blue.svg?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red.svg?style=for-the-badge&logo=streamlit)
![Machine Learning](https://img.shields.io/badge/Machine_Learning-scikit--learn-green.svg?style=for-the-badge&logo=scikitlearn)
![Random Forest](https://img.shields.io/badge/Best_Model-RandomForest-success.svg?style=for-the-badge)
![ROC-AUC](https://img.shields.io/badge/ROC--AUC-0.812-orange.svg?style=for-the-badge)
![Tests](https://img.shields.io/badge/Tests-Passing-brightgreen.svg?style=for-the-badge)

[![Live Demo](https://img.shields.io/badge/Live_Demo-Streamlit_Cloud-purple.svg?style=for-the-badge)](YOUR_STREAMLIT_LINK_HERE)

</div>

---

## Overview

Analysis pipeline for studying how Bitcoin market sentiment correlates with trader profitability, risk behavior, and trading performance using the Bitcoin Fear & Greed Index and Hyperliquid historical trading data.

The project combines:

- sentiment analysis
- trader behavior analysis
- profitability prediction
- risk scoring
- quantitative trading metrics
- model benchmarking
- evaluation tracking
- structured JSON outputs
- interactive Streamlit dashboarding

---

# Problem Statement

This project explores whether trader profitability and trading behavior change across different Bitcoin market sentiment regimes.

The analysis combines:

- Bitcoin Fear & Greed sentiment data
- Hyperliquid historical trader activity

to uncover patterns in:

- profitability
- trade sizing
- trader risk behavior
- market psychology
- predictive ML signals

---

# Key Findings

- RandomForestClassifier achieved the strongest predictive performance with ROC-AUC of **0.812** and CV ROC-AUC mean of **0.813**.
- The model achieved **79.55% recall**, meaning it captured most profitable trade cases.
- Cross-validation standard deviation was only **0.0025**, showing highly stable performance across folds.
- Sentiment regimes showed measurable differences in average trade size, profitability, and risk behavior.
- High-risk trader groups demonstrated lower win rates and higher pnl volatility.
- Leakage prevention significantly reduced unrealistic evaluation scores and improved model reliability.
- Quantitative metrics such as drawdown and profit factor exposed periods of elevated trading risk.

---

# Dataset Information

## Dataset 1 — Bitcoin Fear & Greed Index

Fields:
- date
- value
- classification

Used for:
- sentiment regime analysis
- sentiment trend analysis
- profitability correlation

---

## Dataset 2 — Hyperliquid Historical Trader Data

Fields include:
- account
- symbol
- execution price
- leverage
- side
- size
- time
- closedPnL
- start position

Used for:
- trader profitability analysis
- behavioral analytics
- ML prediction
- risk scoring

---

# Implemented Components

## 1. Data Preprocessing

Implemented:
- datetime parsing
- missing value handling
- feature normalization
- type conversion
- sentiment alignment

---

## 2. Feature Engineering

Engineered features:
- fee_ratio
- trade hour
- trade direction
- sentiment categories
- trader risk score
- pnl volatility
- drawdown metrics

---

## 3. Exploratory Data Analysis

Generated:
- pnl distributions
- cumulative pnl curves
- sentiment distributions
- sentiment vs pnl analysis
- sentiment vs trade size analysis

---

## 4. Machine Learning Classification

Goal:
Predict whether a trade is profitable.

### Models Compared

- RandomForestClassifier
- GradientBoostingClassifier
- XGBoost

---

# ML Results

## Best Model Selected

🏆 **RandomForestClassifier**

| Metric | Score |
|---|---|
| Accuracy | 71.57% |
| Precision | 62.77% |
| Recall | 79.55% |
| F1 Score | 70.17% |
| ROC-AUC | 0.812 |
| CV ROC-AUC Mean | 0.813 |
| CV ROC-AUC Std | 0.0025 |

---

# Baseline Comparison

| Model | Accuracy | ROC-AUC |
|---|---|---|
| Majority Class Baseline | 54% | 0.50 |
| Gradient Boosting | 70% | 0.79 |
| XGBoost | 70% | 0.80 |
| Random Forest | 71.57% | 0.812 |

---

# Cross Validation

Implemented:
- StratifiedKFold cross-validation
- stability analysis
- model benchmarking

This prevents overestimating model performance and improves evaluation reliability.

---

# Data Leakage Prevention

The ML pipeline intentionally excludes:
- direct pnl-derived features
- future information leakage

This ensures:
- realistic evaluation
- trustworthy metrics
- production-style validation

---

# Quantitative Trading Metrics

Implemented metrics:
- Sharpe-like Ratio
- Maximum Drawdown
- Profit Factor
- Trade Expectancy

Generated visualizations:
- drawdown curves
- correlation heatmaps
- cumulative pnl charts

---

# Trader Segmentation

Implemented KMeans clustering to group traders into behavioral segments.

Detected groups include:
- high-risk traders
- stable traders
- aggressive traders
- profitable traders
- volatile traders

---

# Interactive Trade Simulator

Built an interactive profitability simulator using:
- trade size
- fee
- trade side
- sentiment score
- risk score
- trading hour

Outputs:
- profitability probability
- prediction interpretation
- recommendation insight

---

# Dashboard

Interactive Streamlit dashboard for:
- sentiment analysis
- ML insights
- quant analytics
- trader risk intelligence
- segmentation analysis
- profitability simulation

Dashboard Sections:
- Home
- Executive Summary
- Trading Analytics
- Sentiment Intelligence
- Risk Analytics
- Quant Metrics
- Trader Segmentation
- ML Intelligence
- Trade Simulator

---

# Strict JSON Outputs

The pipeline generates machine-readable JSON outputs for downstream analytics workflows.

Generated JSON files:

```text
outputs/json/insights.json
outputs/json/profitability_model_metrics.json
outputs/json/eval_results.json
outputs/json/analyze_result.json
````

---

# Sample JSON Output

```json
{
    "project": "trader_sentiment_analysis",
    "task_type": "classification_and_behavioral_analysis",
    "summary": {
        "total_pnl": 123456.78,
        "win_rate": 0.42,
        "extreme_risk_traders": 5
    },
    "ml_evaluation": {
        "best_model": "RandomForestClassifier",
        "roc_auc": 0.812,
        "cv_roc_auc_mean": 0.813
    },
    "actionable_insights": [
        {
            "insight": "Sentiment regimes show different profitability behavior.",
            "recommendation": "Compare exposure across Fear and Greed periods."
        }
    ]
}
```

---

# CLI Usage

Run focused analysis directly from terminal:

```bash
python analyze.py --sentiment Fear
python analyze.py --sentiment Greed --export
python analyze.py --account <ACCOUNT_ID>
python analyze.py --sentiment Fear --account <ACCOUNT_ID> --export
```

The CLI:

* prints structured JSON
* supports export functionality
* includes logging
* includes error handling

Export path:

```text
outputs/json/analyze_result.json
```

---

# Evaluation Runner

Run held-out evaluation with quality and latency tracking:

```bash
python eval_runner.py --model random_forest
python eval_runner.py --model gradient_boosting
python eval_runner.py --model xgboost
```

Tracked metrics:

* accuracy
* precision
* recall
* F1 score
* ROC-AUC
* training time
* inference latency

Saved output:

```text
outputs/json/eval_results.json
```

---

# JD Alignment

| Job Description Requirement    | Project Implementation                                       |
| ------------------------------ | ------------------------------------------------------------ |
| Prototype AI features          | Built ML profitability classification and sentiment analysis |
| Strict JSON outputs            | Generated structured JSON reports and insight files          |
| Build evaluation sets          | Added held-out evaluation runner                             |
| Track quality metrics          | Tracks ROC-AUC, F1, precision, recall, CV metrics            |
| Track latency                  | Eval runner records inference latency                        |
| CLI tools                      | Added analyze.py with argparse                               |
| Logging/error handling         | Added logging + try/except handling                          |
| Python ML pipeline             | Built modular preprocessing and ML pipeline                  |
| GitHub collaboration readiness | Clean repo structure and reproducible commands               |
| AI/ML implementation           | Random Forest, XGBoost, clustering, risk analytics           |

---

# Tech Stack

## Backend / Analytics

* Python
* Pandas
* NumPy
* SciPy

## Machine Learning

* Scikit-learn
* XGBoost

## Visualization

* Matplotlib
* Seaborn

## Dashboard

* Streamlit

## Testing

* Pytest

---

# Project Structure

```text
trader-sentiment-analysis/
│
├── dashboard/
│   └── app.py
│
├── data/
│   ├── raw/
│   └── processed/
│
├── outputs/
│   ├── figures/
│   ├── json/
│   └── reports/
│
├── src/
│   ├── eda/
│   ├── features/
│   ├── models/
│   ├── preprocessing/
│   ├── utils/
│   └── visualization/
│
├── tests/
│   ├── test_features.py
│   ├── test_models.py
│   └── test_preprocessing.py
│
├── analyze.py
├── eval_runner.py
├── main.py
├── requirements.txt
└── README.md
```

---

# Setup

## 1. Clone Repository

```bash
git clone https://github.com/VedaPriya-Thota/trader-sentiment-analysis
cd trader-sentiment-analysis
```

---

## 2. Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

---

## 3. Install Requirements

```bash
pip install -r requirements.txt
```

---

## 4. Add Datasets

Place datasets inside:

```text
data/raw/
```

Required files:

* historical_data.csv
* fear_greed_index.csv

Dataset Links:

* [https://drive.google.com/file/d/1IAfLZwu6rJzyWKgBToqwSmmVYU6VbjVs/view?usp=drive_link](https://drive.google.com/file/d/1IAfLZwu6rJzyWKgBToqwSmmVYU6VbjVs/view?usp=drive_link)
* [https://drive.google.com/file/d/1PgQC0tO8XN-wqkNyghWc_-mnrYv_nhSf/view?usp=drive_link](https://drive.google.com/file/d/1PgQC0tO8XN-wqkNyghWc_-mnrYv_nhSf/view?usp=drive_link)

---

# Run Pipeline

```bash
python main.py
```

Generated outputs:

* reports
* figures
* json summaries
* model metrics
* quant metrics
* segmentation reports

---

# Launch Dashboard

```bash
streamlit run dashboard/app.py
```

---

# Run Tests

```bash
pytest
```

✅ All tests currently passing.

---

# Quick View of Generated Plots

```bash
explorer outputs\figures
```

---

# Engineering Challenges Solved

* Prevented ML data leakage.
* Added cross-validation for stable evaluation.
* Benchmarked multiple ML models.
* Added CLI tooling with structured JSON outputs.
* Added held-out evaluation runner with latency tracking.
* Built modular preprocessing, modeling, and analytics pipeline.
* Handled noisy financial trading data.

---

# Future Improvements

Planned improvements:

* SHAP explainability
* Time-series validation
* LightGBM / CatBoost benchmarking
* Improved feature engineering
* Real-time market data ingestion
* FastAPI inference endpoints

---

# What I Would Do Next

If given more time, I would:

1. Add SHAP explainability to interpret individual profitability predictions.
2. Replace random train-test split with time-series validation for more realistic financial evaluation.
3. Add real-time streaming market data and deploy the inference pipeline using FastAPI.


```


