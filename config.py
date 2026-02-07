"""
Configuration and page setup for Exam Twin application.
"""

import streamlit as st


def setup_page():
    """Configure Streamlit page settings."""
    st.set_page_config(
        page_title="Exam Twin",
        layout="wide"
    )


def display_hero():
    """Display hero section and divider."""
    st.markdown("""
## 🚀 Exam Twin — IELTS Readiness Intelligence  
Predict your exam readiness, detect risks early, and take the next best action.
""")
    st.divider()
