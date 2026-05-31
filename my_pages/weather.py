import streamlit as st
import weather as wt
from datetime import datetime

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Weather Intelligence",
    page_icon="🌤",
    layout="centered"
)

# ---------------- CACHE API ----------------
@st.cache_data
def get_weather(city):
    return wt.fetch(city)


# ---------------- WEATHER PAGE ----------------
def weather_page():

    # ---------------- HERO ----------------
    st.markdown("""
    <div style="
        background: linear-gradient(135deg,#00FFE0,#00BFFF);
        padding:30px;
        border-radius:20px;
        text-align:center;
        color:black;
        margin-bottom:25px;
    ">
        <h1>🌤 Weather Intelligence</h1>
        <p>Get real-time weather updates from anywhere in the world</p>
    </div>
    """, unsafe_allow_html=True)

    # ---------------- INPUT ----------------
    city = st.text_input(
        "Enter City Name",
        placeholder="Example: London, New York, Bhopal"
    )

    if st.button("🔍 Get Weather", use_container_width=True):

        if not city:
            st.warning("⚠ Please enter a city name")
            st.stop()

        try:
            with st.spinner("Loading ..."):
                (
                    city_name,
                    country,
                    temp,
                    feels_like,
                    humidity,
                    pressure,
                    sunrise,
                    sunset,
                    wind_speed,
                    visibility,
                    condition
                ) = get_weather(city)

            st.success("Weather Data Loaded Successfully ✅")

            # ---------------- HEADER ----------------
            col1, col2 = st.columns([3, 1])

            with col1:
                st.subheader(f"📍 {city_name}, {country}")

            with col2:
                st.metric(
                    "Updated",
                    datetime.now().strftime("%d %b | %H:%M")
                )

            st.divider()

            # ---------------- WEATHER ICON ----------------
            condition_lower = condition.lower()

            if "rain" in condition_lower:
                emoji = "🌧"
            elif "cloud" in condition_lower:
                emoji = "☁"
            elif "snow" in condition_lower:
                emoji = "❄"
            elif "storm" in condition_lower:
                emoji = "⛈"
            elif "clear" in condition_lower:
                emoji = "☀"
            else:
                emoji = "🌤"

            st.markdown(
                f"<h1 style='text-align:center;color:#00FFE0;'>{emoji} {temp}°C</h1>",
                unsafe_allow_html=True
            )

            # ---------------- METRICS ----------------
            col1, col2, col3, col4 = st.columns(4)

            col1.metric("🌡 Temp", f"{temp} °C")
            col2.metric("Feels Like", f"{feels_like} °C")
            col3.metric("💧 Humidity", f"{humidity}%")
            col4.metric("🌬 Wind", f"{wind_speed} m/s")

            st.write("")

            col5, col6, col7 = st.columns(3)

            col5.metric("📊 Pressure", f"{pressure} hPa")
            col6.metric("👁 Visibility", f"{visibility:.1f} km")
            col7.metric("🌍 Country", country)

            st.divider()

            # ---------------- SUNRISE / SUNSET ----------------
            st.subheader("🌅 Sun Timing")

            col_s1, col_s2 = st.columns(2)

            col_s1.metric("🌅 Sunrise", sunrise)
            col_s2.metric("🌇 Sunset", sunset)

            st.divider()

            # ---------------- CONDITION ----------------
            st.subheader("☁ Current Condition")

            if "rain" in condition_lower:
                st.info("🌧 Rainy Weather")
            elif "cloud" in condition_lower:
                st.warning("☁ Cloudy Weather")
            elif "clear" in condition_lower:
                st.success("☀ Clear Sky")
            else:
                st.info(f"🌤 {condition.title()}")

            # ---------------- ANALYSIS ----------------
            st.subheader("📊 Weather Analysis")

            if temp > 35:
                st.error("🔥 Very Hot Weather")
            elif temp > 25:
                st.warning("☀ Warm Weather")
            elif temp > 15:
                st.success("🌤 Pleasant Weather")
            else:
                st.info("❄ Cold Weather")

            # ---------------- COMFORT SCORE ----------------
            st.subheader("⭐ Comfort Score")

            score = 100

            if temp > 35:
                score -= 25
            if humidity > 80:
                score -= 15
            if wind_speed > 15:
                score -= 10

            score = max(score, 0)

            st.progress(score)
            st.metric("Comfort Score", f"{score}/100")

            # ---------------- INSIGHTS ----------------
            st.subheader("🧠 Weather Insights")

            if humidity > 80:
                st.warning("High humidity may feel hotter than actual temperature.")
            elif humidity < 30:
                st.info("Low humidity detected. Air may feel dry.")
            else:
                st.success("Humidity levels are comfortable.")

        except Exception as e:
            st.error(f"Error: {e}")