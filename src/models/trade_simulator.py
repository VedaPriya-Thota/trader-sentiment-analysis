def simulate_trade_profitability(
    size_usd,
    fee,
    hour,
    sentiment_value,
    is_buy,
    risk_score=0.5
):
    score = 0.5

    if sentiment_value >= 60:
        score += 0.08
    elif sentiment_value <= 30:
        score -= 0.05

    if size_usd > 5000:
        score -= 0.06
    elif size_usd < 1000:
        score += 0.03

    if fee > 5:
        score -= 0.04

    if 8 <= hour <= 20:
        score += 0.03

    if is_buy:
        score += 0.02

    if risk_score > 0.75:
        score -= 0.08
    elif risk_score < 0.35:
        score += 0.04

    probability = max(0.05, min(score, 0.95))

    if probability >= 0.7:
        label = "High Profitability Chance"
    elif probability >= 0.55:
        label = "Moderate Profitability Chance"
    else:
        label = "Low Profitability Chance"

    return {
        "profitability_probability": round(probability, 3),
        "prediction_label": label
    }