import streamlit as st

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+Thai:wght@400;500;600;700&display=swap');

html, body, [class*="css"], .stApp, h1, h2, h3, p, div, span, input {
    font-family: 'IBM Plex Sans Thai', sans-serif !important;
}
</style>
""", unsafe_allow_html=True)

st.title("แอปพลิเคชั่นแปลงปี พ.ศ. เป็น ค.ศ.")

bh_year = st.number_input("กรอกปี พ.ศ. ที่ต้องการแปลง",
