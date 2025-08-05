import streamlit as st
from streamlit import session_state as state
import os 
import requests 
BACKEND_URL = os.getenv("BACKEND_URL", "http://backend-service:8000")

def fetch_data():
    try:
        response = requests.get(f"{BACKEND_URL}/node")
        response.raise_for_status() # Ensure we raise an error for bad responses
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching data: {e}")
        return None

def main():
    st.title("Welcome to the Streamlit App")
    
    if 'initialized' not in state:
        state.initialized = True
        st.write("Session initialized.")
    
    st.write(f"Backend URL: {BACKEND_URL}")
    
    if st.button("Fetch Data"):
        response = fetch_data()
        st.write(response)