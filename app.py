import streamlit as st
st.title("Test Narrative Analysis")
st.write("App is running!")
api_key = os.getenv("XAI_API_KEY") or st.secrets.get("XAI_API_KEY")
if api_key:
    st.write("API key found")
else:
    st.error("XAI_API_KEY not found")
