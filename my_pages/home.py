

import streamlit as st

def home_page():
    # ---------------- CUSTOM CSS FOR HOME PAGE ----------------
    st.markdown("""
    <style>
    /* Hero Subtitle Styling */
    .hero-subtitle {
        text-align: center; 
        color: #CFCFCF; 
        font-size: 24px; 
        margin-bottom: 5px;
    }
    .hero-pipeline {
        text-align: center; 
        color: #8A99AD; 
        font-size: 16px; 
        letter-spacing: 1px;
        margin-bottom: 30px;
    }
    
    /* KPI Metric Cards */
    .kpi-container {
        display: flex;
        justify-content: space-between;
        gap: 15px;
        margin-bottom: 25px;
    }
    .kpi-card {
        flex: 1;
        background: linear-gradient(145deg, #1e222b, #151820);
        border: 1px solid #2d313f;
        padding: 20px;
        border-radius: 12px;
        text-align: center;
        transition: transform 0.3s ease, border-color 0.3s ease;
    }
    .kpi-card:hover {
        transform: translateY(-3px);
        border-color: #00FFE0;
    }
    .kpi-value {
        font-size: 32px;
        font-weight: bold;
        color: #00FFE0;
        margin-bottom: 5px;
    }
    .kpi-label {
        font-size: 14px;
        color: #A0AABF;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }

    /* Core Feature Cards */
    .grid-container {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 20px;
        margin-top: 15px;
    }
    .feature-card {
        background: rgba(30, 30, 47, 0.6);
        border: 1px solid rgba(255, 255, 255, 0.05);
        padding: 25px;
        border-radius: 16px;
        backdrop-filter: blur(10px);
        transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
    }
    .feature-card:hover {
        transform: translateY(-5px);
        background: rgba(30, 30, 47, 0.85);
        border-color: rgba(0, 255, 224, 0.3);
        box-shadow: 0 10px 20px rgba(0, 255, 224, 0.05);
    }
    .feature-header {
        font-size: 22px;
        font-weight: 600;
        color: #00FFE0;
        margin-bottom: 12px;
        display: flex;
        align-items: center;
        gap: 10px;
    }
    .feature-text {
        color: #CFCFCF;
        font-size: 15px;
        line-height: 1.6;
    }

    /* Roadmap Checklist */
    .roadmap-item {
        display: flex;
        align-items: center;
        gap: 12px;
        background: #161922;
        padding: 12px 18px;
        border-radius: 8px;
        margin-bottom: 10px;
        border-left: 4px solid #333;
    }
    .roadmap-completed {
        border-left-color: #00FFE0;
        color: #E2E8F0;
    }
    .roadmap-pending {
        border-left-color: #4A5568;
        color: #718096;
    }
    .status-badge {
        font-size: 11px;
        padding: 2px 8px;
        border-radius: 20px;
        font-weight: bold;
    }
    .badge-done { background: rgba(0, 255, 224, 0.15); color: #00FFE0; }
    .badge-next { background: rgba(237, 137, 54, 0.15); color: #ED8936; }
    .badge-future { background: rgba(113, 128, 150, 0.15); color: #A0AABF; }
    </style>
    """, unsafe_allow_html=True)

    # ---------------- HERO SECTION ----------------
    st.markdown("""
<div style="
background: linear-gradient(135deg,#00FFE0,#00BFFF);
padding:30px;
border-radius:20px;
text-align:center;
color:black;
margin-bottom:25px;">
<h1>🤖 Aegis-1</h1>
<p>Your Real-Time AI Assistant Platform</p>
</div>
""", unsafe_allow_html=True)

    # ---------------- STATISTICS (KPI CARDS) ----------------
    st.markdown("""
    <div class='kpi-container'>
        <div class='kpi-card'><div class='kpi-value'>05</div><div class='kpi-label'>Core Modules</div></div>
        <div class='kpi-card'><div class='kpi-value'>02</div><div class='kpi-label'>Live APIs Integrated</div></div>
        <div class='kpi-card'><div class='kpi-value'>v1.0</div><div class='kpi-label'>Engine Version</div></div>
        <div class='kpi-card'><div class='kpi-value' style='color:#00FFE0;'>Active</div><div class='kpi-label'>System Status</div></div>
    </div>
    """, unsafe_allow_html=True)

    st.write("")

    # ---------------- CORE FEATURES (GRID) ----------------
    st.subheader("🚀 Operational Modules")
    st.markdown("""
    <div class='grid-container'>
        <div class='feature-card'>
            <div class='feature-header'>🌤 Weather Intelligence</div>
            <div class='feature-text'>
                Engineered with live third-party environmental APIs to request, process, and analyze hyper-local weather parameters, humidity thresholds, and live atmospheric variations.
            </div>
        </div>
        <div class='feature-card'>
            <div class='feature-header'>📈 Financial Analytics</div>
            <div class='feature-text'>
                Real-time market assessment engine parsing company profiles, historical baseline drift, percentage shifts, and structural bullish/bearish indicators.
            </div>
        </div>
        <div class='feature-card'>
            <div class='feature-header'>🎙 Voice Assistant Architecture</div>
            <div class='feature-text'>
                Local control topology mimicking modular operational shells. Designed for continuous microphone stream pipeline processing and rapid contextual query execution.
            </div>
        </div>
        <div class='feature-card'>
            <div class='feature-header'>🤖 AI Chat Engine</div>
            <div class='feature-text'>
                A natural language sandbox crafted for modern LLM integrations (Gemini/GPT models) to execute general inference and architectural diagnostics.
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.write("")
    st.write("")

    st.subheader("📌 System Architecture")

    st.write("""
**Aegis-1** is a unified, multi-threaded workspace designed to orchestrate asynchronous APIs,
voice telemetry, and cognitive machine learning workflows inside a clean, production-ready interface.

The framework prioritizes lightning-fast context switching, low rendering overhead, and crisp metrics handling
to demonstrate real-world full-stack asset integrations.
""")

    st.info("💡 Developer Note: Navigate across infrastructure layers seamlessly using the top horizontal dashboard controller.")

    st.write("")
    st.write("")
    st.divider()

        

    # ---------------- FOOTER ----------------
    st.markdown("""
    <div style='text-align:center; color:#5A6578; font-size: 13px; margin-top:10px;'>
        Aegis-1 Control Dashboard • Framework compiled via Python & Streamlit
    </div>
    """, unsafe_allow_html=True)