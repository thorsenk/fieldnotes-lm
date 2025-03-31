import streamlit as st
import google.generativeai as genai
from pymongo import MongoClient
import datetime

st.title("🔍 Connection Test")

# Test MongoDB Connection
st.subheader("MongoDB Connection Test")
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
        st.json({
            "database": st.secrets["MONGODB_DATABASE"],
            "collection": "test_collection",
            "document": {"test": found["test"], "timestamp": found["timestamp"]}
        })
        # Clean up test document
        test_collection.delete_one({"_id": result.inserted_id})
except Exception as e:
    st.error(f"❌ MongoDB Connection Failed: {str(e)}")
    st.info("Check your MongoDB connection string and database name in Streamlit secrets.")

# Test Gemini Connection
st.subheader("Gemini API Connection Test")
try:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content("Say hello!")

    if response:
        st.success("✅ Gemini API Connection Successful!")
        st.write("Test Response:", response.text)
except Exception as e:
    st.error(f"❌ Gemini API Connection Failed: {str(e)}")
    st.info("Check your Gemini API key in Streamlit secrets.")

# Show Configuration
st.subheader("Current Configuration")
config = {
    "mongodb_database": st.secrets["MONGODB_DATABASE"],
    "mongodb_connected": "Yes" if "client" in locals() else "No",
    "gemini_connected": "Yes" if "model" in locals() else "No"
}
st.json(config)