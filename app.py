import streamlit as st
from database import create_table

create_table()

st.set_page_config(page_title="AI Legal Analyzer", layout="wide")

# Hide only sidebar
st.markdown("""
<style>
[data-testid="stSidebar"] {display: none;}
</style>
""", unsafe_allow_html=True)

if "page" not in st.session_state:
    st.session_state.page = "login"

if st.session_state.page == "login":
    from pages.login import show_login
    show_login()

elif st.session_state.page == "signup":
    from pages.signup import show_signup
    show_signup()

elif st.session_state.page == "analyzer":
    from pages.analyzer import show_analyzer
    show_analyzer()