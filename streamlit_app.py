import streamlit as st
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Redirect to app_home.py
st.switch_page("app_home.py")