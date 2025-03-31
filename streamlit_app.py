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

# Import app components
from open_notebook.app_home import setup_page

# Set up the main page
setup_page("📒 Fieldnotes LM", sidebar_state="expanded")

# Main app logic
if "object_id" not in st.query_params:
    st.switch_page("pages/2_📒_Notebooks.py")
    st.stop()