import streamlit as st 
def about_page():
    

    st.markdown("""
<div style="
background: linear-gradient(135deg,#00FFE0,#00BFFF);
padding:30px;
border-radius:20px;
text-align:center;
color:black;
margin-bottom:25px;">
<h1>◈ About Aegis-1</h1>
<p>Project information, technologies used, and developer details.</p>
</div>
""", unsafe_allow_html=True)

    st.subheader("🛠 Technologies Used")

    st.write("""
    • Python
    • Streamlit
    • Finnhub API
    • OpenWeather API
    • AI Integration (Future)
    • Voice Assistant (Future)
    """)

    st.subheader("Contact")

    st.markdown("""
    📧 Email: aakankshasable06@gmail.com

    💼 LinkedIn:
    https://www.linkedin.com/in/aakanksha-sable-52433b335/

    🐙 GitHub:
    https://github.com/aakankshasable06-cpu
    """)
