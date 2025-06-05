# STREAMLIT_ENV_VALIDATOR — checks for required environment variables and warns if missing

import os
import streamlit as st

def validate_env():
    st.subheader("🔐 Environment Variable Check")

    key = os.getenv("OPENAI_API_KEY")
    if not key:
        st.error("❌ OPENAI_API_KEY is missing. Please set it in your .env file or deployment config.")
    else:
        st.success("✅ OPENAI_API_KEY is set and available.")

if __name__ == "__main__":
    validate_env()
