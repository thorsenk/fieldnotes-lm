import streamlit as st
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set page config
st.set_page_config(
    page_title="Fieldnotes LM",
    page_icon="📝",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Main page content
st.title("📒 Fieldnotes LM")
st.write("Welcome to Fieldnotes LM - Your AI-powered research assistant!")

# Add sidebar
with st.sidebar:
    st.title("Navigation")
    st.page_link("pages/1_🔍_Test_Connection.py", label="Test Connections")
    st.page_link("pages/2_📒_Notebooks.py", label="Notebooks")

# Main app logic
if "object_id" not in st.query_params:
    st.switch_page("pages/2_📒_Notebooks.py")
    st.stop()