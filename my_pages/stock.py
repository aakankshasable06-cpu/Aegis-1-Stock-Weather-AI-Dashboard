import streamlit as st
import stockapi as sa
from datetime import datetime


# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Stock Intelligence",
    page_icon="📊",
    layout="wide"
)


# ---------------- STOCK PAGE ----------------
def stock_page():

    # ---------------- HERO HEADER (TRADING STYLE) ----------------
    st.markdown("""
    <div style="
        background: linear-gradient(135deg,#00FFE0,#00BFFF);
        padding:30px;
        border-radius:20px;
        text-align:center;
        color:black;
        margin-bottom:25px;
    ">
        <h1> ◼ Stock Intelligence </h1>
        <p>Real-time market data • Company insights • Financial analytics</p>
    </div>
    """, unsafe_allow_html=True)

    # ---------------- INPUT ----------------
    col1, col2 = st.columns([3, 1])

    with col1:
        company = st.text_input(
            "Enter Company Name / Symbol",
            placeholder="AAPL, TSLA, NVDA, Microsoft..."
        )

    with col2:
        st.metric("⏱ Time", datetime.now().strftime("%H:%M:%S"))

    # ---------------- RUN ----------------
    if st.button("Analyze Stock", use_container_width=True):

        if not company:
            st.warning("Please enter a company name or symbol")
            st.stop()

        try:
         with st.spinner("Loading ..."):
            (
                name,
                symbol,
                industry,
                weburl,
                current,
                high,
                low,
                open_price,
                prev_close,
                status,
                percentage_change
            ) = sa.fetch(company)

            # ---------------- LAYOUT: LEFT / RIGHT ----------------
            left, right = st.columns([1.2, 2])

            # =====================================================
            # LEFT SIDE → COMPANY INFO
            # =====================================================
            with left:

                st.markdown("## 🏢 Company Info")

                st.markdown(f"""
                <div style="
                    background:#0f172a;
                    padding:20px;
                    border-radius:15px;
                    border:1px solid #1f2937;
                ">
                    <h3 style="color:#00FFE0;">{name}</h3>
                    <p><b>Symbol:</b> {symbol}</p>
                    <p><b>Industry:</b> {industry}</p>
                </div>
                """, unsafe_allow_html=True)

                st.write("")

                # Website
                st.markdown("## 🌐 Website")

                st.link_button(
                    "Visit Official Site",
                    weburl,
                    use_container_width=True
                )

                st.write("")

                # Quick Status
                st.markdown("## 📊 Status")

                if percentage_change > 0:
                    st.success("📈 Bullish Market")
                elif percentage_change < 0:
                    st.error("📉 Bearish Market")
                else:
                    st.warning("➖ Neutral Movement")

            # =====================================================
            # RIGHT SIDE → MARKET DATA
            # =====================================================
            with right:

                st.markdown("## 💹 Live Market Data")

                price_color = "📈" if percentage_change >= 0 else "📉"

                st.markdown(f"""
                <div style="
                    background:#0f172a;
                    padding:25px;
                    border-radius:15px;
                    border:1px solid #1f2937;
                    text-align:center;
                ">
                    <h2 style="color:#00FFE0;">{symbol}</h2>
                    <h1 style="font-size:45px;">
                        ${current} {price_color}
                    </h1>
                    <p>Change: {percentage_change:.2f}%</p>
                </div>
                """, unsafe_allow_html=True)

                st.write("")

                # Metrics Grid
                c1, c2, c3, c4 = st.columns(4)

                c1.metric("Open", f"${open_price}")
                c2.metric("High", f"${high}")
                c3.metric("Low", f"${low}")
                c4.metric("Prev Close", f"${prev_close}")

                st.divider()

                # Summary Panel
                st.markdown("## 🧾 Full Summary")

                st.info(f"""
                **{name} ({symbol})**

                • Industry: {industry}  
                • Current Price: ${current}  
                • Open: ${open_price}  
                • High: ${high}  
                • Low: ${low}  
                • Previous Close: ${prev_close}  
                • Change: {percentage_change:.2f}%  
                • Market Status: {status}  
                """)

        except Exception as e:
            st.error(f"Error: {e}")
            