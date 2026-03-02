import streamlit as st
import base64

st.set_page_config(
    page_title="TOH Technologies Trading Suite",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

def get_logo_base64():
    try:
        with open("attached_assets/logo.png", "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except:
        return None

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;500;600;700;800;900&family=Roboto:wght@300;400;500;700;900&display=swap');

    .stApp, [data-testid="stAppViewContainer"], 
    section[data-testid="stMain"], .main, 
    [data-testid="stMainBlockContainer"], 
    header[data-testid="stHeader"] {
        background: #000000 !important;
    }

    * {
        font-family: 'Roboto', sans-serif !important;
    }

    [data-testid="stSidebar"] {
        display: none !important;
    }

    .header-container {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 20px 0;
        margin-bottom: 60px;
    }

    .header-left {
        display: flex;
        align-items: center;
        gap: 20px;
    }

    .header-title {
        font-family: 'Orbitron', sans-serif !important;
        font-size: 24px;
        font-weight: 500;
        color: #ffffff;
        letter-spacing: 4px;
        text-transform: uppercase;
        margin: 0;
    }

    .header-motto {
        font-family: 'Roboto', sans-serif !important;
        font-size: 9px;
        color: #555555;
        letter-spacing: 2px;
        text-transform: uppercase;
        font-style: italic;
        margin-top: 4px;
    }

    .card-container .stButton > button {
        background: #0a0a0a !important;
        border: 1px solid #222222 !important;
        border-radius: 8px !important;
        padding: 40px 30px !important;
        min-height: 180px !important;
        cursor: pointer !important;
        transition: all 0.3s ease !important;
        position: relative !important;
        overflow: hidden !important;
        color: #ffffff !important;
        text-align: center !important;
        width: 100% !important;
        font-family: 'Orbitron', sans-serif !important;
        font-size: 20px !important;
        font-weight: 500 !important;
        letter-spacing: 3px !important;
        text-transform: uppercase !important;
        display: flex !important;
        flex-direction: column !important;
        justify-content: center !important;
        align-items: center !important;
    }

    .card-container .stButton > button:hover {
        border-color: #ffffff !important;
        transform: translateY(-5px) !important;
        box-shadow: 0 10px 30px rgba(255, 255, 255, 0.1) !important;
        background: #0a0a0a !important;
        color: #ffffff !important;
    }

    .card-description {
        color: #888888;
        font-size: 13px;
        line-height: 1.6;
        letter-spacing: 0.5px;
        text-align: center;
        margin-top: 15px;
        font-family: 'Roboto', sans-serif !important;
    }
</style>
""", unsafe_allow_html=True)

# Header
logo_base64 = get_logo_base64()
if logo_base64:
    logo_html = f'<img src="data:image/png;base64,{logo_base64}" style="width: 50px; height: 50px;">'
else:
    logo_html = '<div style="width: 50px; height: 50px; background: #222; border-radius: 4px;"></div>'

st.markdown(f"""
<div class="header-container">
    <div class="header-left">
        {logo_html}
        <div>
            <div class="header-title">TOH TECHNOLOGIES</div>
            <div class="header-motto">Innovate and Dominate</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# Cards
col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="card-container">', unsafe_allow_html=True)
    if st.button("BACKTESTER", key="btn_backtest", use_container_width=True):
        st.switch_page("pages/1_Backtester.py")
    st.markdown('<p class="card-description">Advanced DI-based backtesting engine with ATR stop loss, entry/exit variations, trade evolution analysis, and comprehensive performance analytics</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="card-container">', unsafe_allow_html=True)
    if st.button("MONITOR", key="btn_monitor", use_container_width=True):
        st.switch_page("pages/2_Monitor.py")
    st.markdown('<p class="card-description">Real-time market monitoring with DI indicators, multi-instrument tracking, and automated alert system</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
