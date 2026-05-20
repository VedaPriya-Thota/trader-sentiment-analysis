import pandas as pd

from src.models.profitability_model import train_profitability_model


def test_train_profitability_model_outputs_metrics():
    df = pd.DataFrame({
        "size_usd": [100, 200, 300, 400, 500, 600],
        "fee": [1, 2, 1, 3, 2, 4],
        "hour": [1, 2, 3, 4, 5, 6],
        "value": [30, 40, 50, 60, 70, 80],
        "side": ["BUY", "SELL", "BUY", "SELL", "BUY", "SELL"],
        "is_profitable": [True, False, True, False, True, False]
    })

    metrics, feature_importance = train_profitability_model(df)

    assert "accuracy" in metrics
    assert "f1_score" in metrics
    assert "roc_auc" in metrics
    assert not feature_importance.empty