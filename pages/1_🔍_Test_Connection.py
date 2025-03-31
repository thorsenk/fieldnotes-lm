import streamlit as st
import google.generativeai as genai
from pymongo import MongoClient
import datetime

st.title("Connection Test")

# Test MongoDB Connection
try:
    client = MongoClient(st.secrets["MONGODB_URI"])
    db = client[st.secrets["MONGODB_DATABASE"]]

    # Try to write and read a test document
    test_collection = db.test_collection
    test_doc = {
        "test": "connection",
        "timestamp": datetime.datetime.utcnow()
    }
    result = test_collection.insert_one(test_doc)
    found = test_collection.find_one({"_id": result.inserted_id})

    if found:
        st.success("✅ MongoDB Connection Successful!")
        # Clean up test document
        test_collection.delete_one({"_id": result.inserted_id})
except Exception as e:
    st.error(f"❌ MongoDB Connection Failed: {str(e)}")

# Test Gemini Connection
try:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content("Hello!")

    if response:
        st.success("✅ Gemini API Connection Successful!")
except Exception as e:
    st.error(f"❌ Gemini API Connection Failed: {str(e)}")

# Show current configuration
st.subheader("Current Configuration")
st.json({
    "mongodb_database": st.secrets["MONGODB_DATABASE"],
    "mongodb_connected": "Yes" if "client" in locals() else "No",
    "gemini_connected": "Yes" if "model" in locals() else "No",
    "model_language": st.secrets.get("MODEL_LANGUAGE", "gemini-1.5-pro"),
    "model_embedding": st.secrets.get("MODEL_EMBEDDING", "models/embedding-001")
})