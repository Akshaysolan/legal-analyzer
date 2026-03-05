import streamlit as st
from auth import login

def show_login():

    st.set_page_config(page_title="AI Legal Analyzer", layout="wide")

    st.markdown("""
    <style>

    /* Hide the top blur header bar */
    [data-testid="stHeader"]{
        display:none;
    }

    /* Remove top padding */
    .block-container{
        padding-top:0rem;
    }

    /* Full-page background */
    .stApp{
        background-image: url("https://images.unsplash.com/photo-1589998059171-988d887df646");
        background-size: cover;
        background-position: center;
        height: 100vh;
        display: flex;
        justify-content: center;
        align-items: center;
    }

    /* Login box */
    .login-box{
        background: rgba(255,255,255,0.15);
        padding:50px;
        border-radius:20px;
        backdrop-filter: blur(15px);
        width:600px;
        text-align:center;
        box-shadow:0px 8px 30px rgba(0,0,0,0.3);
        margin:auto;
    }

    /* Title */
    .title{
        text-align:center;
        font-size:40px;
        font-weight:bold;
        color:white;
        margin-bottom:10px;
    }

    /* Subtitle */
    .subtitle{
        text-align:center;
        color:white;
        margin-bottom:35px;
        font-size:18px;
    }

    /* Input fields */
    .stTextInput>div>div>input {
        height:45px;
        font-size:16px;
        border-radius:10px;
    }

    /* Buttons */
    .stButton>button {
        width:100%;
        height:50px;
        font-size:18px;
        font-weight:bold;
        border-radius:10px;
        margin-top:10px;
        background-color:#4CAF50;
        color:white;
        border:none;
    }

    .stButton>button:hover {
        background-color:#45a049;
    }

    </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="login-box">', unsafe_allow_html=True)

    st.markdown('<div class="title">AI Legal Analyzer</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Login to continue</div>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1,2,1])

    with col2:
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")

        if st.button("Login"):
            user = login(email, password)
            if user:
                st.session_state.user = user[1]
                st.session_state.page = "analyzer"
                st.rerun()
            else:
                st.error("Invalid credentials")

        st.write("Don't have an account?")

        if st.button("Signup"):
            st.session_state.page = "signup"
            st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)