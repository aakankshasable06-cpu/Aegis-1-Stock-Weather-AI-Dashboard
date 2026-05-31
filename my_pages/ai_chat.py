import streamlit as st
def ai_chat_page():
     
    st.markdown("""
<div style="
background: linear-gradient(135deg,#00FFE0,#00BFFF);
padding:30px;
border-radius:20px;
text-align:center;
color:black;
margin-bottom:25px;">
<h1> ◆ AI Chat Assistant</h1>
<p>Ask questions and interact with AI-powered conversations.</p>
</div>
""", unsafe_allow_html=True)

    st.subheader("🎤 Command Simulation")

    command = st.text_input(
        "Enter Command",
        placeholder="Example: Show Apple stock"
    )

    if st.button("Run Command"):

        cmd = command.lower()

        # -------- STOCK COMMAND --------
        if "apple" in cmd:

            st.success("Fetching Apple stock data...")

        elif "tesla" in cmd:

            st.success("Fetching Tesla stock data...")

        # -------- WEATHER COMMAND --------
        elif "weather" in cmd:

            st.success("Fetching weather data...")

        else:

            st.warning("Command not recognized.")

    st.write("")

    st.markdown("""
    <div class='feature-box'>
    <h2>🚀 Future Features</h2>
    <p>
    Real microphone input, speech recognition,
    text-to-speech, AI integration, and smart task execution.
    </p>
    </div>
    """, unsafe_allow_html=True)   