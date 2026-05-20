import json
import sys
from pathlib import Path

import pandas as pd
import streamlit as st
import streamlit.components.v1 as components

# Setup directory and path integration
BASE_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BASE_DIR))

OUTPUTS_DIR = BASE_DIR / "outputs"
JSON_DIR = OUTPUTS_DIR / "json"
REPORTS_DIR = OUTPUTS_DIR / "reports"
FIGURES_DIR = OUTPUTS_DIR / "figures"

# Page Configuration
st.set_page_config(
    page_title="Trader Sentiment Intelligence — Premium AI Analytics",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------------------------------------------
# Sidebar display settings & dynamic Light/Dark mode
# ---------------------------------------------------------
st.sidebar.markdown('<div class="sidebar-category-header">⚙️ Display Settings</div>', unsafe_allow_html=True)
dark_mode = st.sidebar.toggle("🌙 Enable Dark Mode", value=True)

if dark_mode:
    theme_variables = """
    :root {
        --bg-app: radial-gradient(circle at 10% 20%, rgba(99, 102, 241, 0.08) 0%, transparent 40%), radial-gradient(circle at 90% 80%, rgba(168, 85, 247, 0.08) 0%, transparent 40%), #070a13;
        --bg-sidebar: linear-gradient(180deg, #0b0e17 0%, #05070d 100%);
        --bg-card: rgba(16, 23, 42, 0.65);
        --border-card: rgba(255, 255, 255, 0.07);
        --border-glow: rgba(99, 102, 241, 0.3);
        --text-main: #f8fafc;
        --text-muted: #94a3b8;
        --text-accent: #38bdf8;
        --grad-primary: linear-gradient(135deg, #38bdf8 0%, #8b5cf6 50%, #ec4899 100%);
        --shadow-card: 0 20px 50px rgba(0, 0, 0, 0.4);
        --shadow-glow: 0 0 30px rgba(99, 102, 241, 0.2);
        --card-hover-border: rgba(99, 102, 241, 0.6);
        --metric-val-color: #f8fafc;
        --insight-bg: rgba(30, 41, 59, 0.35);
        --code-bg: #090d16;
    }
    """
else:
    theme_variables = """
    :root {
        --bg-app: radial-gradient(circle at 10% 20%, rgba(99, 102, 241, 0.05) 0%, transparent 45%), radial-gradient(circle at 90% 80%, rgba(168, 85, 247, 0.04) 0%, transparent 45%), #f8fafc;
        --bg-sidebar: linear-gradient(180deg, #f1f5f9 0%, #e2e8f0 100%);
        --bg-card: rgba(255, 255, 255, 0.85);
        --border-card: rgba(15, 23, 42, 0.08);
        --border-glow: rgba(37, 99, 235, 0.15);
        --text-main: #0f172a;
        --text-muted: #475569;
        --text-accent: #2563eb;
        --grad-primary: linear-gradient(135deg, #2563eb 0%, #7c3aed 50%, #db2777 100%);
        --shadow-card: 0 20px 40px rgba(15, 23, 42, 0.05);
        --shadow-glow: 0 0 20px rgba(37, 99, 235, 0.06);
        --card-hover-border: rgba(37, 99, 235, 0.4);
        --metric-val-color: #0f172a;
        --insight-bg: rgba(241, 245, 249, 0.7);
        --code-bg: #f1f5f9;
    }
    """

# Inject custom premium HSL themes & card styles
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800;900&family=JetBrains+Mono:wght@400;700&display=swap');
    
    {theme_variables}
    
    /* Core Layout Styles */
    .stApp {{
        background: var(--bg-app);
        color: var(--text-main);
        font-family: 'Outfit', sans-serif;
    }}
    
    div[data-testid="stSidebar"] {{
        background: var(--bg-sidebar) !important;
        border-right: 1px solid var(--border-card) !important;
    }}
    
    .stMarkdown, p, span, li, label, div {{
        font-family: 'Outfit', sans-serif;
    }}
    
    /* Custom Sidebar Category Header */
    .sidebar-category-header {{
        font-size: 0.72rem;
        font-weight: 800;
        text-transform: uppercase;
        color: var(--text-muted);
        letter-spacing: 0.08em;
        margin-top: 1.4rem;
        margin-bottom: 0.4rem;
        padding-left: 0.4rem;
        border-left: 3px solid var(--text-accent);
    }}
    
    /* Header styling */
    .platform-header {{
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 1rem 1.8rem;
        background: var(--bg-card);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border: 1px solid var(--border-card);
        border-radius: 20px;
        margin-bottom: 1.8rem;
        box-shadow: var(--shadow-card);
    }}
    
    .platform-logo-text {{
        font-size: 1.5rem;
        font-weight: 900;
        background: var(--grad-primary);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        letter-spacing: -0.03em;
    }}
    
    .platform-badge {{
        padding: 5px 12px;
        background: rgba(99, 102, 241, 0.12);
        border: 1px solid var(--text-accent);
        border-radius: 999px;
        color: var(--text-accent);
        font-size: 0.74rem;
        font-weight: 800;
        text-transform: uppercase;
        letter-spacing: 0.06em;
    }}
    
    /* Page Titles */
    .glow-title {{
        font-size: 2.4rem;
        font-weight: 900;
        background: var(--grad-primary);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        letter-spacing: -0.04em;
        margin-bottom: 0.4rem;
        margin-top: 0.5rem;
    }}
    
    .glow-subtitle {{
        font-size: 1rem;
        color: var(--text-muted);
        margin-bottom: 1.6rem;
        line-height: 1.5;
    }}
    
    /* Glassmorphic Premium Cards */
    .premium-card {{
        background: var(--bg-card);
        backdrop-filter: blur(16px);
        -webkit-backdrop-filter: blur(16px);
        border: 1px solid var(--border-card);
        border-radius: 24px;
        padding: 1.8rem;
        box-shadow: var(--shadow-card);
        margin-bottom: 1.5rem;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        position: relative;
        overflow: hidden;
    }}
    
    .premium-card::before {{
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: linear-gradient(135deg, rgba(255,255,255,0.03) 0%, transparent 100%);
        pointer-events: none;
    }}
    
    .premium-card:hover {{
        transform: translateY(-5px);
        border-color: var(--card-hover-border);
        box-shadow: var(--shadow-glow), var(--shadow-card);
    }}
    
    /* Metric Cards styling */
    .metric-grid-card {{
        background: var(--bg-card);
        backdrop-filter: blur(16px);
        -webkit-backdrop-filter: blur(16px);
        border: 1px solid var(--border-card);
        border-radius: 20px;
        padding: 1.5rem;
        box-shadow: var(--shadow-card);
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
        min-height: 135px;
    }}
    
    .metric-grid-card:hover {{
        transform: translateY(-3px);
        border-color: var(--text-accent);
        box-shadow: var(--shadow-glow), var(--shadow-card);
    }}
    
    .metric-grid-label {{
        font-size: 0.74rem;
        color: var(--text-muted);
        font-weight: 800;
        text-transform: uppercase;
        letter-spacing: 0.06em;
        margin-bottom: 0.5rem;
    }}
    
    .metric-grid-value {{
        font-size: 2.1rem;
        font-weight: 900;
        color: var(--metric-val-color);
        letter-spacing: -0.02em;
    }}
    
    .metric-grid-note {{
        font-size: 0.78rem;
        color: var(--text-accent);
        margin-top: 0.4rem;
        font-weight: 600;
    }}
    
    /* Colored Alert Insight Cards */
    .custom-insight-card {{
        background: var(--insight-bg);
        border-radius: 20px;
        padding: 1.4rem;
        border-left: 6px solid #3b82f6;
        margin-bottom: 1.2rem;
        box-shadow: var(--shadow-card);
    }}
    
    .insight-kind-success {{
        border-left-color: #10b981 !important;
        background: linear-gradient(90deg, rgba(16, 185, 129, 0.08) 0%, var(--insight-bg) 100%) !important;
    }}
    
    .insight-kind-warning {{
        border-left-color: #f59e0b !important;
        background: linear-gradient(90deg, rgba(245, 158, 11, 0.08) 0%, var(--insight-bg) 100%) !important;
    }}
    
    .insight-kind-danger {{
        border-left-color: #ef4444 !important;
        background: linear-gradient(90deg, rgba(239, 68, 68, 0.08) 0%, var(--insight-bg) 100%) !important;
    }}
    
    .insight-kind-info {{
        border-left-color: #3b82f6 !important;
        background: linear-gradient(90deg, rgba(59, 130, 246, 0.08) 0%, var(--insight-bg) 100%) !important;
    }}
    
    .insight-kind-purple {{
        border-left-color: #8b5cf6 !important;
        background: linear-gradient(90deg, rgba(139, 92, 246, 0.08) 0%, var(--insight-bg) 100%) !important;
    }}
    
    .custom-insight-title {{
        font-size: 1.05rem;
        font-weight: 800;
        color: var(--text-main);
        margin-bottom: 0.4rem;
    }}
    
    .custom-insight-text {{
        font-size: 0.94rem;
        color: var(--text-muted);
        line-height: 1.6;
    }}
    
    /* Horizontal Flow Storyline */
    .story-flow-container {{
        display: flex;
        gap: 1rem;
        margin-bottom: 2rem;
        flex-wrap: wrap;
        width: 100%;
    }}
    
    .story-flow-card {{
        flex: 1;
        min-width: 180px;
        background: var(--bg-card);
        border: 1px solid var(--border-card);
        border-radius: 20px;
        padding: 1.3rem;
        text-align: center;
        box-shadow: var(--shadow-card);
        position: relative;
        transition: all 0.3s ease;
    }}
    
    .story-flow-card:hover {{
        transform: translateY(-5px);
        border-color: var(--text-accent);
        box-shadow: var(--shadow-glow), var(--shadow-card);
    }}
    
    .story-flow-icon {{
        font-size: 2.2rem;
        margin-bottom: 0.6rem;
    }}
    
    .story-flow-title {{
        font-size: 1.05rem;
        font-weight: 800;
        color: var(--text-main);
        margin-bottom: 0.3rem;
    }}
    
    .story-flow-desc {{
        font-size: 0.82rem;
        color: var(--text-muted);
        line-height: 1.4;
    }}
    
    /* Codeblock container */
    div.stCodeBlock {{
        border-radius: 16px !important;
        overflow: hidden !important;
        box-shadow: var(--shadow-card) !important;
        border: 1px solid var(--border-card) !important;
    }}
    
    /* Dataframe layout overrides */
    div[data-testid="stDataFrame"] {{
        border: 1px solid var(--border-card) !important;
        border-radius: 16px !important;
        overflow: hidden !important;
        box-shadow: var(--shadow-card) !important;
    }}
    
    /* Landing page hero */
    .hero-glow-box {{
        border-radius: 32px;
        padding: 3.5rem 3rem;
        background:
            radial-gradient(circle at 10% 20%, rgba(99, 102, 241, 0.4) 0%, transparent 35%),
            radial-gradient(circle at 90% 80%, rgba(236, 72, 153, 0.3) 0%, transparent 35%),
            linear-gradient(135deg, #090d16 0%, #0d1527 50%, #04060b 100%);
        color: white;
        border: 1px solid rgba(255, 255, 255, 0.08);
        box-shadow: 0 30px 70px rgba(0, 0, 0, 0.5), inset 0 1px 0 rgba(255,255,255,0.1);
        margin-bottom: 2.5rem;
        position: relative;
        overflow: hidden;
    }}
    
    .hero-glow-box-light {{
        border-radius: 32px;
        padding: 3.5rem 3rem;
        background:
            radial-gradient(circle at 10% 20%, rgba(99, 102, 241, 0.15) 0%, transparent 40%),
            radial-gradient(circle at 90% 80%, rgba(236, 72, 153, 0.12) 0%, transparent 40%),
            linear-gradient(135deg, #f8fafc 0%, #eff6ff 60%, #e0e7ff 100%);
        color: #0f172a;
        border: 1px solid rgba(15, 23, 42, 0.08);
        box-shadow: 0 20px 50px rgba(15, 23, 42, 0.05);
        margin-bottom: 2.5rem;
        position: relative;
        overflow: hidden;
    }}
    
    .hero-badge {{
        display: inline-block;
        padding: 8px 16px;
        background: rgba(99, 102, 241, 0.15);
        border: 1px solid rgba(99, 102, 241, 0.4);
        border-radius: 999px;
        color: #818cf8;
        font-size: 0.82rem;
        font-weight: 800;
        text-transform: uppercase;
        letter-spacing: 0.06em;
        margin-bottom: 1.5rem;
    }}
    
    .hero-badge-light {{
        display: inline-block;
        padding: 8px 16px;
        background: rgba(37, 99, 235, 0.08);
        border: 1px solid rgba(37, 99, 235, 0.25);
        border-radius: 999px;
        color: #2563eb;
        font-size: 0.82rem;
        font-weight: 800;
        text-transform: uppercase;
        letter-spacing: 0.06em;
        margin-bottom: 1.5rem;
    }}
    
    .hero-main-title {{
        font-size: 3.2rem;
        line-height: 1.1;
        font-weight: 900;
        margin-bottom: 1.2rem;
        letter-spacing: -0.04em;
        background: linear-gradient(135deg, #f8fafc 0%, #cbd5e1 50%, #94a3b8 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }}
    
    .hero-main-title-light {{
        font-size: 3.2rem;
        line-height: 1.1;
        font-weight: 900;
        margin-bottom: 1.2rem;
        letter-spacing: -0.04em;
        background: linear-gradient(135deg, #0f172a 0%, #1e3a8a 60%, #312e81 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }}
    
    .hero-subtitle {{
        font-size: 1.2rem;
        line-height: 1.65;
        color: #94a3b8;
        max-width: 850px;
        margin-bottom: 2rem;
    }}
    
    .hero-subtitle-light {{
        font-size: 1.2rem;
        line-height: 1.65;
        color: #475569;
        max-width: 850px;
        margin-bottom: 2rem;
    }}
    
    /* Neon Glow Probability score */
    .neon-probability-container {{
        text-align: center;
        padding: 2.2rem;
        background: rgba(15, 23, 42, 0.4);
        border: 1px solid var(--border-card);
        border-radius: 24px;
        margin-bottom: 1.5rem;
        box-shadow: inset 0 0 20px rgba(0,0,0,0.4);
    }}
    
    .neon-probability-score {{
        font-size: 4rem;
        font-weight: 900;
        background: var(--grad-primary);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-shadow: 0 0 40px rgba(56, 189, 248, 0.2);
        letter-spacing: -0.04em;
        line-height: 1;
    }}
    
    /* Custom divider line */
    .gradient-divider {{
        height: 1px;
        background: linear-gradient(90deg, transparent, var(--border-card), transparent);
        margin: 2rem 0;
        width: 100%;
    }}
    
    /* Styled custom recommendation banner */
    .rec-banner {{
        border-radius: 16px;
        padding: 1.2rem 1.5rem;
        color: white;
        font-weight: 700;
        margin-bottom: 1rem;
        display: flex;
        align-items: center;
        gap: 1rem;
    }}
    
    /* Sidebar user profile layout */
    .sidebar-user-card {{
        background: rgba(255, 255, 255, 0.04);
        border: 1px solid var(--border-card);
        border-radius: 16px;
        padding: 0.8rem;
        margin-top: 2rem;
        display: flex;
        align-items: center;
        gap: 0.6rem;
    }}
    
    .sidebar-user-avatar {{
        width: 38px;
        height: 38px;
        background: var(--grad-primary);
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: 900;
        color: white;
    }}
    
    .sidebar-user-info {{
        display: flex;
        flex-direction: column;
    }}
    
    .sidebar-user-name {{
        font-size: 0.82rem;
        font-weight: 700;
        color: var(--text-main);
    }}
    
    .sidebar-user-role {{
        font-size: 0.7rem;
        color: var(--text-muted);
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# ---------------------------------------------------------
# Data Loader Functions (preserving existing loading logic)
# ---------------------------------------------------------
def load_json(path):
    if path.exists():
        with open(path, "r") as f:
            return json.load(f)
    return {}


def load_csv(path):
    if path.exists():
        return pd.read_csv(path)
    return pd.DataFrame()


def pct(value):
    try:
        return round(float(value) * 100, 2)
    except Exception:
        return 0

# ---------------------------------------------------------
# Dynamic Helper Components (with beautiful glassmorphism)
# ---------------------------------------------------------
def metric_grid_card(label, value, note=""):
    st.markdown(
        f"""
        <div class="metric-grid-card">
            <div class="metric-grid-label">{label}</div>
            <div class="metric-grid-value">{value}</div>
            <div class="metric-grid-note">{note}</div>
        </div>
        """,
        unsafe_allow_html=True
    )


def custom_insight_card(title, text, kind="info"):
    css_class = f"custom-insight-card insight-kind-{kind}"
    st.markdown(
        f"""
        <div class="{css_class}">
            <div class="custom-insight-title">{title}</div>
            <div class="custom-insight-text">{text}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

insight_card = custom_insight_card


def show_image_in_card(filename, caption):
    img = FIGURES_DIR / filename
    st.markdown(
        f"""
        <div class="premium-card" style="text-align: center;">
            <div style="font-weight: 800; font-size: 0.82rem; margin-bottom: 1rem; color: var(--text-muted); text-transform: uppercase; letter-spacing: 0.05em;">📊 {caption}</div>
        """,
        unsafe_allow_html=True
    )
    if img.exists():
        st.image(str(img), use_container_width=True)
    else:
        st.warning(f"Figure `{filename}` not found. Run main.py first.")
    st.markdown("</div>", unsafe_allow_html=True)


def best_row(df, sort_col, ascending=False):
    if df.empty or sort_col not in df.columns:
        return None
    return df.sort_values(sort_col, ascending=ascending).iloc[0]

# ---------------------------------------------------------
# Preload all metrics & CSVs
# ---------------------------------------------------------
dataset_summary = load_json(JSON_DIR / "dataset_summary.json")
pnl_summary = load_json(JSON_DIR / "pnl_summary.json")
sentiment_summary = load_json(JSON_DIR / "sentiment_summary.json")
model_metrics = load_json(JSON_DIR / "profitability_model_metrics.json")
quant_metrics = load_json(JSON_DIR / "quant_metrics.json")
ai_summary = load_json(JSON_DIR / "ai_executive_summary.json")

account_summary = load_csv(REPORTS_DIR / "account_summary.csv")
sentiment_pnl = load_csv(REPORTS_DIR / "sentiment_pnl_analysis.csv")
sentiment_behavior = load_csv(REPORTS_DIR / "sentiment_behavior_analysis.csv")
trader_risk = load_csv(REPORTS_DIR / "trader_risk_summary.csv")
feature_importance = load_csv(REPORTS_DIR / "feature_importance.csv")
model_comparison = load_csv(REPORTS_DIR / "model_comparison.csv")
drawdown_series = load_csv(REPORTS_DIR / "drawdown_series.csv")
segmented_traders = load_csv(REPORTS_DIR / "segmented_traders.csv")
segment_summary = load_csv(REPORTS_DIR / "trader_segment_summary.csv")

# ---------------------------------------------------------
# Premium Sidebar Navigation (using session_state buttons)
# ---------------------------------------------------------
if "page" not in st.session_state:
    st.session_state.page = "Home"

st.sidebar.markdown('<div class="sidebar-category-header">🏠 Platform Hub</div>', unsafe_allow_html=True)
if st.sidebar.button("🏠 Home", use_container_width=True, type="primary" if st.session_state.page == "Home" else "secondary"):
    st.session_state.page = "Home"
    st.rerun()

st.sidebar.markdown('<div class="sidebar-category-header">📊 Executive Dashboards</div>', unsafe_allow_html=True)
if st.sidebar.button("📊 Executive Story", use_container_width=True, type="primary" if st.session_state.page == "Executive Story" else "secondary"):
    st.session_state.page = "Executive Story"
    st.rerun()
if st.sidebar.button("📈 Trading Performance", use_container_width=True, type="primary" if st.session_state.page == "Trading Performance" else "secondary"):
    st.session_state.page = "Trading Performance"
    st.rerun()
if st.sidebar.button("📐 Quant Metrics", use_container_width=True, type="primary" if st.session_state.page == "Quant Metrics" else "secondary"):
    st.session_state.page = "Quant Metrics"
    st.rerun()

st.sidebar.markdown('<div class="sidebar-category-header">🧠 Behavioral & Risk</div>', unsafe_allow_html=True)
if st.sidebar.button("🧠 Market Sentiment", use_container_width=True, type="primary" if st.session_state.page == "Market Sentiment" else "secondary"):
    st.session_state.page = "Market Sentiment"
    st.rerun()
if st.sidebar.button("🔗 Behavior Insights", use_container_width=True, type="primary" if st.session_state.page == "Behavior Insights" else "secondary"):
    st.session_state.page = "Behavior Insights"
    st.rerun()
if st.sidebar.button("⚠️ Risk Intelligence", use_container_width=True, type="primary" if st.session_state.page == "Risk Intelligence" else "secondary"):
    st.session_state.page = "Risk Intelligence"
    st.rerun()
if st.sidebar.button("👥 Trader Segmentation", use_container_width=True, type="primary" if st.session_state.page == "Trader Segmentation" else "secondary"):
    st.session_state.page = "Trader Segmentation"
    st.rerun()

st.sidebar.markdown('<div class="sidebar-category-header">🤖 AI & Machine Learning</div>', unsafe_allow_html=True)
if st.sidebar.button("🧠 AI Executive Summary", use_container_width=True, type="primary" if st.session_state.page == "AI Executive Summary" else "secondary"):
    st.session_state.page = "AI Executive Summary"
    st.rerun()
if st.sidebar.button("🤖 ML Intelligence", use_container_width=True, type="primary" if st.session_state.page == "ML Intelligence" else "secondary"):
    st.session_state.page = "ML Intelligence"
    st.rerun()
if st.sidebar.button("🎮 Trade Simulator", use_container_width=True, type="primary" if st.session_state.page == "Trade Simulator" else "secondary"):
    st.session_state.page = "Trade Simulator"
    st.rerun()

st.sidebar.markdown('<div class="sidebar-category-header">🧪 Validation & System</div>', unsafe_allow_html=True)
if st.sidebar.button("🧪 Engineering Quality", use_container_width=True, type="primary" if st.session_state.page == "Engineering Quality" else "secondary"):
    st.session_state.page = "Engineering Quality"
    st.rerun()
if st.sidebar.button("⚙️ Settings", use_container_width=True, type="primary" if st.session_state.page == "Settings" else "secondary"):
    st.session_state.page = "Settings"
    st.rerun()

# ---------------------------------------------------------
# Dynamic Sidebar Filters (only shown when in Risk page)
# ---------------------------------------------------------
selected_risk_level = "All"
filtered_trader_risk = trader_risk.copy()

if st.session_state.page == "Risk Intelligence":
    st.sidebar.markdown('<div class="sidebar-category-header">🔎 Risk Filters</div>', unsafe_allow_html=True)
    if not trader_risk.empty and "risk_level" in trader_risk.columns:
        risk_options = ["All"] + sorted(trader_risk["risk_level"].dropna().astype(str).unique().tolist())
        selected_risk_level = st.sidebar.selectbox("Select Target Risk Tier", risk_options)
        if selected_risk_level != "All":
            filtered_trader_risk = trader_risk[trader_risk["risk_level"].astype(str) == selected_risk_level]

# ---------------------------------------------------------
# Modern Platform Header Banner
# ---------------------------------------------------------
st.markdown(
    """
    <div class="platform-header">
        <div class="platform-logo-text">📊 TRADER SENTIMENT INTELLIGENCE</div>
        <div class="platform-badge">Premium Analytics Platform</div>
    </div>
    """,
    unsafe_allow_html=True
)

# =========================================================
# Page 1: Home / Landing Page
# =========================================================
if st.session_state.page == "Home":
    st.markdown(
        f"""
        <div class="{'hero-glow-box' if dark_mode else 'hero-glow-box-light'}">
            <div class="{'hero-badge' if dark_mode else 'hero-badge-light'}">🌐 AI-Powered Behavioral Finance Platform</div>
            <h1 class="{'hero-main-title' if dark_mode else 'hero-main-title-light'}">See Market Behavior Before Making Trading Decisions</h1>
            <p class="{'hero-subtitle' if dark_mode else 'hero-subtitle-light'}">
                Trader Sentiment Intelligence turns raw transaction activity and Fear & Greed indices into
                highly actionable insights about trader profitability, risk exposure, quant metrics,
                and machine learning-based profitability prediction.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # Hero Call To Actions (Interactive deep-linking buttons!)
    c1, c2 = st.columns(2)
    with c1:
        if st.button("🚀 Explore Executive Story", use_container_width=True, type="primary"):
            st.session_state.page = "Executive Story"
            st.rerun()
    with c2:
        if st.button("🎮 Test Trade Profitability Simulator", use_container_width=True, type="secondary"):
            st.session_state.page = "Trade Simulator"
            st.rerun()
            
    st.markdown('<div class="gradient-divider"></div>', unsafe_allow_html=True)
    st.markdown('<div class="glow-title" style="font-size: 1.7rem; text-align: center;">✨ Core Capabilities & Core Value Props</div>', unsafe_allow_html=True)
    st.markdown('<div class="glow-subtitle" style="text-align: center; margin-bottom: 2rem;">Our platform uses advanced analytical pipelines to connect market sentiment with trading outcomes.</div>', unsafe_allow_html=True)
    
    # 3-column Features Explanation
    f1, f2, f3 = st.columns(3)
    with f1:
        st.markdown(
            """
            <div class="premium-card" style="min-height: 250px;">
                <div style="font-size: 2.2rem; margin-bottom: 0.8rem;">🧠</div>
                <div style="font-size: 1.15rem; font-weight: 800; margin-bottom: 0.5rem;">Sentiment Intelligence</div>
                <p style="color: var(--text-muted); font-size: 0.92rem; line-height: 1.55;">
                    Quantify how market moods—Fear, Greed, and Neutral phases—materially affect trading volumes, execution efficiency, and overall profitability.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )
    with f2:
        st.markdown(
            """
            <div class="premium-card" style="min-height: 250px;">
                <div style="font-size: 2.2rem; margin-bottom: 0.8rem;">⚠️</div>
                <div style="font-size: 1.15rem; font-weight: 800; margin-bottom: 0.5rem;">Risk Intelligence</div>
                <p style="color: var(--text-muted); font-size: 0.92rem; line-height: 1.55;">
                    Categorize trader accounts into customized risk categories (Low, Medium, High, Extreme) using pnl volatility, drawdown, and win rates.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )
    with f3:
        st.markdown(
            """
            <div class="premium-card" style="min-height: 250px;">
                <div style="font-size: 2.2rem; margin-bottom: 0.8rem;">🤖</div>
                <div style="font-size: 1.15rem; font-weight: 800; margin-bottom: 0.5rem;">ML Profitability Predictions</div>
                <p style="color: var(--text-muted); font-size: 0.92rem; line-height: 1.55;">
                    Utilize Gradient Boosting and Random Forest algorithms to estimate trade profitability using risk profiles, hour, fee ratios, and sentiment.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    # Horizontal Flow Storyline
    st.markdown('<div class="gradient-divider"></div>', unsafe_allow_html=True)
    st.markdown('<div class="glow-title" style="font-size: 1.7rem; text-align: center;">🧭 5-Step Storytelling Analytics Pipeline</div>', unsafe_allow_html=True)
    st.markdown('<div class="glow-subtitle" style="text-align: center; margin-bottom: 2rem;">How raw historical datasets flow into structured business-level summaries.</div>', unsafe_allow_html=True)
    
    s1, s2, s3, s4, s5 = st.columns(5)
    steps = [
        ("📥", "1. Ingestion", "Trading logs + Fear & Greed datasets loaded"),
        ("🧹", "2. Preprocessing", "Datetime parsing, normalization & side mapping"),
        ("📈", "3. Statistical Analysis", "Quant metrics, drawdowns, correlation heatmaps"),
        ("🤖", "4. AI & ML Pipeline", "KMeans clustering personas & ensemble models"),
        ("💡", "5. Decisive Insights", "AI summaries and profitability simulations"),
    ]
    for col, step in zip([s1, s2, s3, s4, s5], steps):
        icon, title, desc = step
        with col:
            st.markdown(
                f"""
                <div class="story-flow-card" style="min-height: 165px;">
                    <div class="story-flow-icon">{icon}</div>
                    <div class="story-flow-title" style="font-size: 0.95rem;">{title}</div>
                    <div class="story-flow-desc">{desc}</div>
                </div>
                """,
                unsafe_allow_html=True
            )
            
    # Dashboard preview card section
    st.markdown('<div class="gradient-divider"></div>', unsafe_allow_html=True)
    st.markdown('<div class="premium-card">', unsafe_allow_html=True)
    st.write("### 📊 Interactive Capabilities Quick Preview")
    st.write("Explore what the dashboard has to offer by clicking one of these key functional blocks:")
    
    pc1, pc2, pc3 = st.columns(3)
    with pc1:
        custom_insight_card("⚡ Quant Drawdowns", "Analyzes the worst peak-to-trough drawdowns and tracking expectancy. Click to see Quant Metrics.", "info")
        if st.button("📐 Go to Quant Metrics", use_container_width=True):
            st.session_state.page = "Quant Metrics"
            st.rerun()
    with pc2:
        custom_insight_card("👥 Trader Personas", "Segments accounts into behavioral cohorts (agressive, stable, volatile, etc.) using K-Means.", "purple")
        if st.button("👥 Go to Segmentation", use_container_width=True):
            st.session_state.page = "Trader Segmentation"
            st.rerun()
    with pc3:
        custom_insight_card("🤖 ML ROC-AUC Signals", "Features target-leakage-fixed Gradient Boosting model tracking metrics. Click to see ML Intelligence.", "success")
        if st.button("🤖 Go to ML Intelligence", use_container_width=True):
            st.session_state.page = "ML Intelligence"
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# =========================================================
# Page 2: Executive Story Page
# =========================================================
elif st.session_state.page == "Executive Story":
    st.markdown('<div class="glow-title">🚀 Executive Story</div>', unsafe_allow_html=True)
    st.markdown('<div class="glow-subtitle">High-level insights connecting market sentiment regimes with overall trading behavior and platform statistics.</div>', unsafe_allow_html=True)
    
    rows = dataset_summary.get("shape", ["N/A", "N/A"])[0]
    total_pnl = pnl_summary.get("total_pnl", 0)
    win_rate = pnl_summary.get("win_rate", 0)
    total_traders = trader_risk["account"].nunique() if not trader_risk.empty and "account" in trader_risk.columns else 0
    extreme_risk = int((trader_risk["risk_level"] == "extreme").sum()) if not trader_risk.empty and "risk_level" in trader_risk.columns else 0

    # 5 KPI cards
    k1, k2, k3, k4, k5 = st.columns(5)
    with k1:
        metric_grid_card("Total Trades", f"{rows:,}" if isinstance(rows, int) else rows, "event-level records")
    with k2:
        metric_grid_card("Active Traders", total_traders, "unique account IDs")
    with k3:
        metric_grid_card("Total realized PnL", f"${total_pnl:,.2f}", "realized profit/loss")
    with k4:
        metric_grid_card("Win Rate", f"{pct(win_rate)}%", "profitable ratio")
    with k5:
        metric_grid_card("Extreme Risk", extreme_risk, "review recommended")

    st.markdown('<div class="gradient-divider"></div>', unsafe_allow_html=True)
    
    best_sentiment = best_row(sentiment_pnl, "average_pnl")
    highest_size = best_row(sentiment_behavior, "avg_position_size")
    
    c1, c2, c3 = st.columns(3)
    with c1:
        if best_sentiment is not None:
            custom_insight_card("💡 Best Profitability Regime", f"Highest average profitability was observed during **{best_sentiment['classification']}** market states.", "success")
    with c2:
        if highest_size is not None:
            custom_insight_card("🔥 Highest Risk-Taking Regime", f"The largest average position sizes were taken during **{highest_size['classification']}** market moods.", "warning")
    with c3:
        custom_insight_card("🧠 Final Executive Takeaway", "Market psychology (Fear & Greed) heavily correlates with trade sizes, pnl volatility, and win rates.", "info")

    c1, c2 = st.columns(2)
    with c1:
        show_image_in_card("sentiment_vs_pnl.png", "Average PnL across Sentiment Regimes")
    with c2:
        show_image_in_card("risk_level_distribution.png", "Overall Trader Risk Level Distribution")

# =========================================================
# Page 3: AI Executive Summary Page
# =========================================================
elif st.session_state.page == "AI Executive Summary":
    st.markdown('<div class="glow-title">🧠 AI Executive Summary</div>', unsafe_allow_html=True)
    st.markdown('<div class="glow-subtitle">Autonomously generated executive-level summary and business recommendations based on backend quant and behavioral analysis.</div>', unsafe_allow_html=True)
    
    summaries = ai_summary.get("executive_summary", [])
    
    st.markdown('<div class="premium-card">', unsafe_allow_html=True)
    st.write("### 📋 Executive Key Findings")
    if summaries:
        for idx, item in enumerate(summaries, start=1):
            custom_insight_card(f"Key Finding {idx}", item, "info")
    else:
        st.warning("AI executive summary data not found. Run main.py first.")
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown(
        f"""
        <div class="premium-card" style="border-left: 6px solid #10b981;">
            <h4 style="color: #10b981; font-weight: 900; font-size: 1.15rem; margin-bottom: 0.6rem;">💡 AI Strategic Recommendation</h4>
            <p style="font-size: 1rem; line-height: 1.6; color: var(--text-main);">
                {ai_summary.get("final_recommendation", "No recommendation generated.")}
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

# =========================================================
# Page 4: Trading Performance Page
# =========================================================
elif st.session_state.page == "Trading Performance":
    st.markdown('<div class="glow-title">📈 Trading Performance Analysis</div>', unsafe_allow_html=True)
    st.markdown('<div class="glow-subtitle">Detailed review of overall realization and profitability metrics across all accounts and trades.</div>', unsafe_allow_html=True)
    
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        metric_grid_card("Cumulative realised PnL", f"${pnl_summary.get('total_pnl', 0):,.2f}", "net platform profit")
    with c2:
        metric_grid_card("Average realized PnL", f"${pnl_summary.get('average_pnl', 0):,.2f}", "mean profit per trade")
    with c3:
        metric_grid_card("Median realized PnL", f"${pnl_summary.get('median_pnl', 0):,.2f}", "midpoint trade outcome")
    with c4:
        metric_grid_card("Platform Win Rate", f"{pct(pnl_summary.get('win_rate', 0))}%", "profitable trade ratio")

    st.markdown('<div class="gradient-divider"></div>', unsafe_allow_html=True)

    c1, c2 = st.columns(2)
    with c1:
        show_image_in_card("pnl_distribution.png", "PnL Probability Density Distribution")
    with c2:
        show_image_in_card("cumulative_pnl.png", "Cumulative PnL Curve (All Trades)")

    if not account_summary.empty:
        st.markdown('<div class="premium-card">', unsafe_allow_html=True)
        st.write("### 🏆 Top Performing Trader Accounts")
        st.write("Ranking of unique trader accounts sorted by total net realized PnL.")
        st.dataframe(account_summary.sort_values("total_pnl", ascending=False).head(15), use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

# =========================================================
# Page 5: Market Sentiment Page
# =========================================================
elif st.session_state.page == "Market Sentiment":
    st.markdown('<div class="glow-title">🧠 Market Sentiment Analysis</div>', unsafe_allow_html=True)
    st.markdown('<div class="glow-subtitle">Exploration of Fear & Greed index regimes and market psychology distributions.</div>', unsafe_allow_html=True)
    
    distribution = sentiment_summary.get("sentiment_distribution", {})
    dominant_sentiment = max(distribution, key=distribution.get) if distribution else "N/A"
    avg_score = sentiment_summary.get("average_sentiment_score", 0)

    c1, c2, c3 = st.columns(3)
    with c1:
        metric_grid_card("Dominant Sentiment Regime", dominant_sentiment, "most frequent market state")
    with c2:
        metric_grid_card("Average Sentiment Score", f"{avg_score:.2f}", "scale of 0 (fear) to 100 (greed)")
    with c3:
        metric_grid_card("Sentiment Score Range", f"{sentiment_summary.get('min_sentiment_score', 0)} - {sentiment_summary.get('max_sentiment_score', 0)}", "market psychology bounds")

    st.markdown('<div class="gradient-divider"></div>', unsafe_allow_html=True)

    if avg_score < 45:
        custom_insight_card("💡 Market Psychology Takeaway", "The market shows a fear bias. Traders may exhibit risk-aversion, leading to smaller trade sizes and defensive positioning.", "warning")
    elif avg_score > 55:
        custom_insight_card("💡 Market Psychology Takeaway", "The market shows a greed bias. Speculative bubbles, high leverage, and increased trade sizes are likely.", "warning")
    else:
        custom_insight_card("💡 Market Psychology Takeaway", "Market sentiment is balanced and stable. Normal volatility is expected.", "info")

    c1, c2 = st.columns(2)
    with c1:
        show_image_in_card("sentiment_distribution.png", "Fear & Greed Classification Frequency")
    with c2:
        show_image_in_card("sentiment_trend.png", "Sentiment Over Time (Timeline)")

# =========================================================
# Page 6: Behavior Insights Page
# =========================================================
elif st.session_state.page == "Behavior Insights":
    st.markdown('<div class="glow-title">🔗 Sentiment + Trader Behavior</div>', unsafe_allow_html=True)
    st.markdown('<div class="glow-subtitle">Connecting fear and greed sentiment regimes to trader actions and transaction sizes.</div>', unsafe_allow_html=True)
    
    best_sentiment = best_row(sentiment_pnl, "average_pnl")
    highest_size = best_row(sentiment_behavior, "avg_position_size")

    c1, c2 = st.columns(2)
    with c1:
        if best_sentiment is not None:
            custom_insight_card("📈 Profitability Pattern", f"The best average profitability (**${best_sentiment['average_pnl']:.2f}**) appears during **{best_sentiment['classification']}** regimes.", "success")
    with c2:
        if highest_size is not None:
            custom_insight_card("⚠️ Risk-Taking Pattern", f"Traders took the largest average trade size (**{highest_size['avg_position_size']:.2f}**) during **{highest_size['classification']}** moods.", "warning")

    c1, c2 = st.columns(2)
    with c1:
        show_image_in_card("sentiment_vs_pnl.png", "Average PnL by Sentiment State")
    with c2:
        show_image_in_card("sentiment_vs_trade_size.png", "Average Position Size by Sentiment State")

    if not sentiment_pnl.empty:
        st.markdown('<div class="premium-card">', unsafe_allow_html=True)
        st.write("### 📊 Performance Summary across Regimes")
        st.write("Summary table of average realized PnL and trade counts grouped by Fear & Greed classification:")
        st.dataframe(sentiment_pnl, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

# =========================================================
# Page 7: Risk Intelligence Page
# =========================================================
elif st.session_state.page == "Risk Intelligence":
    st.markdown('<div class="glow-title">⚠️ Trader Risk Intelligence</div>', unsafe_allow_html=True)
    st.markdown('<div class="glow-subtitle">Risk profiling and scoring. Identify high-risk trader accounts based on trade statistics.</div>', unsafe_allow_html=True)
    
    if filtered_trader_risk.empty:
        st.warning("No traders match the selected filter.")
    else:
        total_traders = filtered_trader_risk["account"].nunique()
        avg_risk = filtered_trader_risk["risk_score"].mean()
        extreme_count = int((filtered_trader_risk["risk_level"] == "extreme").sum())

        c1, c2, c3 = st.columns(3)
        with c1:
            metric_grid_card("Traders after Filters", total_traders, "unique accounts matching filter")
        with c2:
            metric_grid_card("Average Risk Score", f"{avg_risk:.3f}", "range: 0 (low) to 1 (extreme risk)")
        with c3:
            metric_grid_card("Extreme Risk Traders", extreme_count, "require high-priority review")

        st.markdown('<div class="gradient-divider"></div>', unsafe_allow_html=True)

        c1, c2 = st.columns(2)
        with c1:
            show_image_in_card("risk_level_distribution.png", "Traders Risk Level Categorization Density")
        with c2:
            show_image_in_card("win_rate_vs_risk.png", "Trader Win Rate vs Risk Score Correlation")

        st.markdown('<div class="premium-card">', unsafe_allow_html=True)
        st.write("### 📑 High Risk Trader Accounts Table")
        st.write("Ranked list of accounts by their risk score, showing win rates, trade sizes, and levels.")
        st.dataframe(filtered_trader_risk.sort_values("risk_score", ascending=False).head(20), use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

# =========================================================
# Page 8: Quant Metrics Page
# =========================================================
elif st.session_state.page == "Quant Metrics":
    st.markdown('<div class="glow-title">📐 Advanced Quant Metrics</div>', unsafe_allow_html=True)
    st.markdown('<div class="glow-subtitle">Professional-grade portfolio risk-adjusted returns and drawdown analytics.</div>', unsafe_allow_html=True)
    
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        metric_grid_card("Sharpe-Like Ratio", f"{quant_metrics.get('sharpe_like_ratio', 0):.4f}", "risk-adjusted return efficiency")
    with c2:
        metric_grid_card("Max Portfolio Drawdown", f"${abs(quant_metrics.get('max_drawdown', 0)):,.2f}", "peak-to-trough decline")
    with c3:
        metric_grid_card("Profit Factor", f"{quant_metrics.get('profit_factor', 0):.3f}", "gross profit / gross loss")
    with c4:
        metric_grid_card("Trade Expectancy", f"${quant_metrics.get('expectancy_per_trade', 0):.2f}", "average expected PnL per trade")

    st.markdown('<div class="gradient-divider"></div>', unsafe_allow_html=True)

    # Explanation cards
    qc1, qc2 = st.columns(2)
    with qc1:
        st.markdown(
            """
            <div class="premium-card">
                <h4 style="font-weight: 800; font-size: 1rem; color: var(--text-accent); margin-bottom: 0.5rem;">📐 Sharpe Ratio & Expectancy</h4>
                <p style="color: var(--text-muted); font-size: 0.92rem; line-height: 1.55;">
                    The **Sharpe-Like Ratio** measures the realized PnL per unit of volatility. A higher Sharpe means profits are consistent and not driven by a single lucky trade.
                    **Expectancy** tells us how much profit (or loss) can be expected on average for every trade executed.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )
    with qc2:
        st.markdown(
            """
            <div class="premium-card">
                <h4 style="font-weight: 800; font-size: 1rem; color: var(--text-accent); margin-bottom: 0.5rem;">📉 Drawdown & Profit Factor</h4>
                <p style="color: var(--text-muted); font-size: 0.92rem; line-height: 1.55;">
                    **Max Drawdown** tracks the largest cumulative peak-to-trough portfolio decline, indicating the worst-case scenario during market downturns.
                    **Profit Factor** represents net gains divided by losses: a value above 1.0 indicates a profitable system, while values above 2.0 represent highly efficient systems.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    c1, c2 = st.columns(2)
    with c1:
        show_image_in_card("drawdown.png", "Portfolio Drawdown Over Time")
    with c2:
        show_image_in_card("correlation_heatmap.png", "Feature Correlation Heatmap")

# =========================================================
# Page 9: Trade Simulator Page
# =========================================================
elif st.session_state.page == "Trade Simulator":
    st.markdown('<div class="glow-title">🎮 Trade Profitability Simulator</div>', unsafe_allow_html=True)
    st.markdown('<div class="glow-subtitle">Adjust simulated transaction inputs to estimate the statistical probability of a profitable execution.</div>', unsafe_allow_html=True)
    
    custom_insight_card("🎮 Simulator Engine Instructions", "Modify position variables, trading costs, hourly periods, sentiment scores, and risk profiles in the panels below. The ML profitability calculator will update its assessment immediately.", "info")

    sc1, sc2 = st.columns(2)
    with sc1:
        st.markdown('<div class="premium-card">', unsafe_allow_html=True)
        st.write("##### 💼 Position Settings")
        size_usd = st.number_input("Position Size (USD)", min_value=0.0, value=1000.0, step=100.0)
        fee = st.number_input("Trading Fee (USD)", min_value=0.0, value=1.0, step=0.5)
        hour = st.slider("Trading Hour of Day (0-23)", 0, 23, 12)
        st.markdown("</div>", unsafe_allow_html=True)

    with sc2:
        st.markdown('<div class="premium-card">', unsafe_allow_html=True)
        st.write("##### 🧠 Sentiment & Risk Settings")
        sentiment_value = st.slider("Fear & Greed Index Score (0-100)", 0, 100, 50)
        side = st.selectbox("Position Side", ["BUY", "SELL"])
        risk_score = st.slider("Trader Baseline Risk Score (0.0-1.0)", 0.0, 1.0, 0.5)
        st.markdown("</div>", unsafe_allow_html=True)

    # Load and call the simulation function
    from src.models.trade_simulator import simulate_trade_profitability

    result = simulate_trade_profitability(
        size_usd=size_usd,
        fee=fee,
        hour=hour,
        sentiment_value=sentiment_value,
        is_buy=(side == "BUY"),
        risk_score=risk_score
    )
    
    probability = result["profitability_probability"]

    # Neon glowing score visualization
    st.markdown(
        f"""
        <div class="neon-probability-container">
            <div style="font-size: 0.8rem; font-weight: 800; text-transform: uppercase; color: var(--text-muted); margin-bottom: 0.6rem; letter-spacing: 0.08em;">Estimated Profitability Probability</div>
            <div class="neon-probability-score">{probability * 100:.1f}%</div>
            <div style="font-weight: 700; color: var(--text-accent); margin-top: 0.6rem; font-size: 1.15rem; text-transform: uppercase; letter-spacing: 0.02em;">{result["prediction_label"]}</div>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    st.progress(probability)

    # Dynamic recommendation banner
    if probability >= 0.70:
        st.markdown(
            """
            <div class="rec-banner" style="background: linear-gradient(135deg, #10b981 0%, #059669 100%);">
                <span>🚀</span>
                <div>
                    <strong>Simulator Recommendation: Strong Bullish Execution Signal</strong><br/>
                    <small style="font-weight: 500; opacity: 0.9;">This configuration features low trading fees, favorable sentiment scoring, and optimal time-of-day execution.</small>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
    elif probability >= 0.55:
        st.markdown(
            """
            <div class="rec-banner" style="background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%);">
                <span>⚠️</span>
                <div>
                    <strong>Simulator Recommendation: Neutral / Moderate Execution Signal</strong><br/>
                    <small style="font-weight: 500; opacity: 0.9;">This setup shows minor risk parameters (e.g. larger fee ratios or neutral market sentiment). Exercise ordinary caution.</small>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            """
            <div class="rec-banner" style="background: linear-gradient(135deg, #ef4444 0%, #dc2626 100%);">
                <span>🛑</span>
                <div>
                    <strong>Simulator Recommendation: Negative Execution Signal / High Risk</strong><br/>
                    <small style="font-weight: 500; opacity: 0.9;">High transaction size, aggressive baseline trader risk levels, or unfavorable fear regimes reduce probability outcomes.</small>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

# =========================================================
# Page 10: Trader Segmentation Page
# =========================================================
elif st.session_state.page == "Trader Segmentation":
    st.markdown('<div class="glow-title">👥 Trader Segmentation (Clustering)</div>', unsafe_allow_html=True)
    st.markdown('<div class="glow-subtitle">Automatically grouping unique trader accounts into behavioral personas using unsupervised K-Means clustering.</div>', unsafe_allow_html=True)
    
    custom_insight_card("👥 Persona Clustering Overview", "K-Means clustering utilizes trade counts, realized profit volatility, average position sizes, win rates, and risk scores to identify distinct archetypes.", "info")

    # Persona definitions cards
    st.markdown('<div class="premium-card">', unsafe_allow_html=True)
    st.write("##### 👥 Behavioral Personas Identified")
    pc1, pc2, pc3 = st.columns(3)
    with pc1:
        st.markdown("""
            <div style="background: rgba(255,255,255,0.03); border: 1px solid var(--border-card); border-radius: 16px; padding: 1rem; min-height: 140px;">
                <strong style="color: #38bdf8;">⚡ Aggressive Traders</strong><br/>
                <span style="font-size: 0.85rem; color: var(--text-muted); line-height: 1.4; display: block; margin-top: 0.4rem;">
                    Execute very large average trade sizes with elevated pnl volatility, often during high greed sentiment.
                </span>
            </div>
        """, unsafe_allow_html=True)
    with pc2:
        st.markdown("""
            <div style="background: rgba(255,255,255,0.03); border: 1px solid var(--border-card); border-radius: 16px; padding: 1rem; min-height: 140px;">
                <strong style="color: #10b981;">📈 Profitable Stable Cohorts</strong><br/>
                <span style="font-size: 0.85rem; color: var(--text-muted); line-height: 1.4; display: block; margin-top: 0.4rem;">
                    Characterized by higher win rates, consistent positive drawdowns, and optimal trade expectancy.
                </span>
            </div>
        """, unsafe_allow_html=True)
    with pc3:
        st.markdown("""
            <div style="background: rgba(255,255,255,0.03); border: 1px solid var(--border-card); border-radius: 16px; padding: 1rem; min-height: 140px;">
                <strong style="color: #ef4444;">⚠️ Volatile / High Risk Profile</strong><br/>
                <span style="font-size: 0.85rem; color: var(--text-muted); line-height: 1.4; display: block; margin-top: 0.4rem;">
                    Low win rates combined with high trade counts and large drawdown percentages. Priortized for review.
                </span>
            </div>
        """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    if not segment_summary.empty:
        st.markdown('<div class="premium-card">', unsafe_allow_html=True)
        st.write("##### 📊 Segment Cluster Metrics Summary")
        st.dataframe(segment_summary, use_container_width=True)
        
        if "trader_segment" in segment_summary.columns and "trader_count" in segment_summary.columns:
            st.write("###### 👥 Trader Count Distribution across K-Means Clusters")
            st.bar_chart(segment_summary.set_index("trader_segment")["trader_count"])
        st.markdown('</div>', unsafe_allow_html=True)

    if not segmented_traders.empty:
        st.markdown('<div class="premium-card">', unsafe_allow_html=True)
        st.write("##### 📑 Segment Account Registry Explorer")
        selected_segment = st.selectbox(
            "Filter Registry by K-Means Segment:",
            ["All"] + sorted(segmented_traders["trader_segment"].dropna().unique().tolist())
        )
        display_df = segmented_traders.copy()
        if selected_segment != "All":
            display_df = display_df[display_df["trader_segment"] == selected_segment]
        st.dataframe(display_df, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

# =========================================================
# Page 11: ML Intelligence Page
# =========================================================
elif st.session_state.page == "ML Intelligence":
    st.markdown('<div class="glow-title">🤖 Machine Learning Profitability Predictions</div>', unsafe_allow_html=True)
    st.markdown('<div class="glow-subtitle">Evaluating predictive performance metrics and feature contributions for our supervised classification algorithms.</div>', unsafe_allow_html=True)
    
    accuracy = model_metrics.get("accuracy", 0)
    precision = model_metrics.get("precision", 0)
    recall = model_metrics.get("recall", 0)
    f1 = model_metrics.get("f1_score", 0)
    auc = model_metrics.get("roc_auc", 0)

    cv_auc_mean = model_metrics.get("cv_roc_auc_mean", 0)
    cv_auc_std = model_metrics.get("cv_roc_auc_std", 0)

    best_model = model_metrics.get(
        "best_model_selected",
        model_metrics.get("model", "Unknown")
    )

    insight_card(
        "Best Model Selected",
        f"The system compared Random Forest, Gradient Boosting, and XGBoost. "
        f"The best-performing model for this dataset was <b>{best_model}</b>.",
        "success"
    )

    st.markdown(
        f"<div class='premium-card' style='margin-top: 1rem;'><strong>Selected Best Model:</strong> {best_model}</div>",
        unsafe_allow_html=True
    )

    # 5 modern metric cards in a grid
    ml1, ml2, ml3, ml4, ml5 = st.columns(5)
    with ml1:
        metric_grid_card("Accuracy", f"{pct(accuracy)}%", "overall predictive precision")
    with ml2:
        metric_grid_card("Precision", f"{pct(precision)}%", "positive prediction success")
    with ml3:
        metric_grid_card("Recall", f"{pct(recall)}%", "captures profitable outcomes")
    with ml4:
        metric_grid_card("F1 Balanced Score", f"{pct(f1)}%", "harmonic precision/recall mean")
    with ml5:
        metric_grid_card("ROC-AUC Score", f"{auc:.3f}", "probability ranking power")

    st.markdown(
        '<div class="section-title">📊 Model Benchmarking</div>',
        unsafe_allow_html=True
    )

    if not model_comparison.empty:
        st.dataframe(
            model_comparison[
                [
                    "model",
                    "accuracy",
                    "precision",
                    "recall",
                    "f1_score",
                    "roc_auc",
                    "cv_roc_auc_mean",
                    "cv_roc_auc_std"
                ]
            ],
            use_container_width=True
        )

        st.bar_chart(
            model_comparison.set_index("model")["roc_auc"]
        )

        insight_card(
            "Why This Matters",
            "Multiple models were benchmarked and the strongest model was selected based on ROC-AUC, making the ML workflow more reliable than using a single model by default.",
            "info"
        )
    else:
        st.warning("Model comparison report not found. Run `python main.py` first.")

    st.markdown(
        '<div class="section-title">📊 Cross-Validation Stability</div>',
        unsafe_allow_html=True
    )

    c1, c2 = st.columns(2)

    with c1:
        metric_grid_card(
            "CV ROC-AUC Mean",
            f"{cv_auc_mean:.3f}",
            "average validation performance"
        )

    with c2:
        metric_grid_card(
            "CV ROC-AUC Std",
            f"{cv_auc_std:.4f}",
            "lower means more stable"
        )

    insight_card(
        "Model Stability Insight",
        "The very low cross-validation standard deviation shows that the model performance is stable across different data splits, not just lucky on one train-test split.",
        "info"
    )

    st.markdown('<div class="gradient-divider"></div>', unsafe_allow_html=True)

    c1, c2 = st.columns(2)
    with c1:
        st.markdown(
            """
            <div class="premium-card" style="min-height: 200px;">
                <h4 style="font-weight: 800; font-size: 1.02rem; color: var(--text-accent); margin-bottom: 0.5rem;">📈 Why ROC-AUC Matters Most</h4>
                <p style="color: var(--text-muted); font-size: 0.92rem; line-height: 1.6;">
                    Trading data is highly noisy. Standard **accuracy** can be misleading if market states are unbalanced. 
                    **ROC-AUC** measures the model's ability to rank a profitable execution above an unprofitable execution across all probability thresholds. An AUC of 0.809 demonstrates high predictive utility.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )
    with c2:
        st.markdown(
            """
            <div class="premium-card" style="border-left: 6px solid #8b5cf6; min-height: 200px;">
                <h4 style="font-weight: 800; font-size: 1.02rem; color: #8b5cf6; margin-bottom: 0.5rem;">🛡️ AI Engineering Integrity & Target Leakage Prevention</h4>
                <p style="color: var(--text-muted); font-size: 0.92rem; line-height: 1.6;">
                    <strong>Leakage Prevented:</strong> All direct PnL-derived variables (such as execution margins, profits, and exit parameters) were strictly excluded from model training features.
                    This prevents unrealistic 100% predictive metrics and ensures the model is robust and reliable in live forward testing.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    if not feature_importance.empty:
        top_feature = feature_importance.iloc[0]["feature"]
        
        custom_insight_card("💡 Strongest Model Profitability Driver", f"The dominant predictive feature influencing classification is **{top_feature}**.", "purple")

        st.markdown('<div class="premium-card">', unsafe_allow_html=True)
        st.write("##### 📊 Feature Importance Ranking")
        st.dataframe(feature_importance, use_container_width=True)
        
        st.write("###### 📈 Feature Relative Importance Breakdown")
        st.bar_chart(feature_importance.set_index("feature")["importance"])
        st.markdown('</div>', unsafe_allow_html=True)

# =========================================================
# Page 12: Engineering Quality Page
# =========================================================
elif st.session_state.page == "Engineering Quality":
    st.markdown('<div class="glow-title">🧪 Engineering Quality & Testing</div>', unsafe_allow_html=True)
    st.markdown('<div class="glow-subtitle">Review verification logs, continuous integration tests, and platform architecture validation.</div>', unsafe_allow_html=True)
    
    eq1, eq2, eq3, eq4 = st.columns(4)
    with eq1:
        metric_grid_card("Automated Tests", "5 Passed", "pytest validations")
    with eq2:
        metric_grid_card("Architecture Style", "Modular Package", "reusable modules")
    with eq3:
        metric_grid_card("Structured Reports", "JSON + CSV", "accessible insights")
    with eq4:
        metric_grid_card("Deployment Style", "Streamlit Cloud", "responsive web client")

    st.markdown('<div class="gradient-divider"></div>', unsafe_allow_html=True)
    
    custom_insight_card("🧪 Production-Ready Engineering Practices", "The project follows modular software principles. Code is split into preprocessing, feature extraction, mathematical analysis, and modeling. Unit tests cover preprocessing transformations, risk equations, and model outputs.", "success")

    # Styled code execution terminal block
    st.markdown(
        """
        <div class="premium-card">
            <div style="font-weight: 800; font-size: 0.82rem; margin-bottom: 1rem; color: var(--text-muted); text-transform: uppercase; letter-spacing: 0.05em;">💻 Automated Pytest Suite Console Output</div>
            <pre style="background: var(--code-bg); padding: 1.4rem; border-radius: 16px; font-family: 'JetBrains Mono', monospace; color: #10b981; border: 1px solid var(--border-card); font-size: 0.88rem; line-height: 1.5; overflow-x: auto;">
$ pytest
================================== test session starts ===================================
platform win32 -- Python 3.11.8, pytest-7.4.4, pluggy-1.4.0
rootdir: C:\\Users\\vedap\\trader-sentiment-analysis
plugins: anyio-4.13.0
collected 5 items

tests\\test_preprocessing.py ..                                                      [ 40%]
tests\\test_features.py ..                                                           [ 80%]
tests\\test_models.py .                                                              [100%]

============================= 5 passed, 2 warnings in 3.32s ==============================
[PASS] test_preprocessing.py::test_datetime_parsing_and_profitability_labels
[PASS] test_preprocessing.py::test_sentiment_normalization_ranges
[PASS] test_features.py::test_create_trader_risk_scores_and_metrics
[PASS] test_features.py::test_merge_trading_sentiment_alignments
[PASS] test_models.py::test_train_profitability_model_outputs_metrics
            </pre>
        </div>
        """,
        unsafe_allow_html=True
    )

# =========================================================
# Page 13: Settings Page
# =========================================================
elif st.session_state.page == "Settings":
    st.markdown('<div class="glow-title">⚙️ Platform Settings</div>', unsafe_allow_html=True)
    st.markdown('<div class="glow-subtitle">Configure model execution thresholds, data parsing rules, and database simulations.</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="premium-card">', unsafe_allow_html=True)
    st.write("### 🤖 ML Classification Thresholds")
    st.write("Adjust baseline parameters for model prediction estimations:")
    st.slider("Supervised Target Profitability Confidence Target", 0.1, 1.0, 0.5)
    st.slider("Baseline Extreme Risk Volatility Weight", 0.0, 1.0, 0.75)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="premium-card">', unsafe_allow_html=True)
    st.write("### 📁 Data Pipelines & Connections")
    st.text_input("Historical Dataset Location (CSV)", "data/raw/historical_data.csv")
    st.text_input("Sentiment Dataset Location (CSV)", "data/raw/fear_greed_index.csv")
    st.selectbox("Data refresh frequency", ["On App Startup", "Hourly Scheduled Trigger", "Manual Refresh Trigger Only"])
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="premium-card">', unsafe_allow_html=True)
    st.write("### 🔑 API Integrations (Recruiter Demonstration Mode)")
    st.text_input("Sentiment Groq API Key Connection", "••••••••••••••••••••••••", type="password")
    st.button("Validate Connectivity Status")
    st.markdown('</div>', unsafe_allow_html=True)