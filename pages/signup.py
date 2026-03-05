import streamlit as st
from auth import signup

def show_signup():

    st.set_page_config(page_title="AI Legal Analyzer - Signup", layout="wide")

    st.markdown("""
    <style>

    /* Hide Streamlit top blur header */
    [data-testid="stHeader"]{
        display:none;
    }

    /* Remove top spacing */
    .block-container{
        padding-top:0rem;
    }

    /* Full-page background */
    .stApp{
        background-image: url("https://images.unsplash.com/photo-1506744038136-46273834b3fb");
        background-size: cover;
        background-position: center;
        height: 100vh;
        display: flex;
        justify-content: center;
        align-items: center;
    }

    /* Signup box */
    .signup-box{
        background: rgba(0,0,0,0.4);
        padding:50px;
        border-radius:20px;
        backdrop-filter: blur(15px);
        width:600px;
        text-align:center;
        box-shadow:0px 8px 30px rgba(0,0,0,0.6);
        color:white;
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

    st.markdown('<div class="signup-box">', unsafe_allow_html=True)

    st.markdown('<div class="title">AI Legal Analyzer</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Create your account</div>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1,2,1])

    with col2:
        name = st.text_input("Name")
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")

        if st.button("Signup"):
            if signup(name,email,password):
                st.success("Account created successfully")
                st.session_state.page="login"
                st.rerun()
            else:
                st.error("User already exists")

        st.write("Already have an account?")

        if st.button("Go to Login"):
            st.session_state.page="login"
            st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)

