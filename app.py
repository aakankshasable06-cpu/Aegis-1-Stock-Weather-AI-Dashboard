import streamlit as st
import os
from dotenv import load_dotenv
from streamlit_option_menu import option_menu

# ---------------- LOAD ENV (API KEYS SAFE) ----------------
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
STOCK_API_KEY = os.getenv("STOCK_API_KEY")


# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Aegis-1",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>

.stApp{
    background-color:#0E1117;
    color:white;
}

.main-title{
    font-size:50px;
    font-weight:bold;
    text-align:center;
    color:#00FFE0;
}

.sub-title{
    font-size:22px;
    text-align:center;
    color:#CFCFCF;
}

.feature-box{
    background-color:#1E1E2F;
    padding:20px;
    border-radius:15px;
    margin-top:20px;
    box-shadow: 0px 0px 10px rgba(0,255,224,0.2);
}

.footer{
    text-align:center;
    margin-top:40px;
    color:gray;
    font-size:14px;
}

</style>
""", unsafe_allow_html=True)


# ---------------- SAFE PAGE IMPORTS ----------------
try:
    from my_pages.home import home_page
    from my_pages.stock import stock_page
    from my_pages.weather import weather_page
    from my_pages.voice import voice_page
    from my_pages.ai_chat import ai_chat_page
    from my_pages.about import about_page

except Exception as e:
    st.error(f"❌ Page import error: {e}")


# ---------------- NAVBAR ----------------
menu = option_menu(
    menu_title=None,
    options=["Home", "Weather", "Stocks", "Voice Assistant", "AI Chat", "About"],
    orientation="horizontal",
    styles={
        "container": {
            "padding": "0!important",
            "background-color": "#0E1517"
        },
        "nav-link": {
            "font-size": "18px",
            "text-align": "center",
            "margin": "0px",
            "--hover-color": "#0A0A0A",
        },
        "nav-link-selected": {
            "background-color": "#00FFE0",
            "color": "black",
            "border-radius": "10px"
        }
    }
)


# ---------------- PAGE ROUTING (CLEAN VERSION) ----------------
pages = {
    "Home": home_page,
    "Weather": weather_page,
    "Stocks": stock_page,
    "Voice Assistant": voice_page,
    "AI Chat": ai_chat_page,
    "About": about_page
}

if menu in pages:
    pages[menu]()
else:
    st.error("Page not found!")


# ---------------- FOOTER ----------------
st.markdown("""
<div class='footer'>
    Made with ❤️ using Streamlit | Aegis-1
</div>
""", unsafe_allow_html=True)