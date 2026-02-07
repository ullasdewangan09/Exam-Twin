"""
UI components for sidebar and metrics display.
"""

import streamlit as st


def get_sidebar_inputs():
    """
    Get all user inputs from the sidebar.
    
    Returns:
        dict: All user input values
    """
    st.sidebar.header("Enter Preparation Details")

    target_band = st.sidebar.slider("Target IELTS Band", 5.0, 9.0, 7.5, 0.5)
    exam_days = st.sidebar.slider("Days Until Exam", 7, 180, 45)

    st.sidebar.subheader("Section Scores")
    listening = st.sidebar.slider("Listening", 0.0, 9.0, 6.5, 0.5)
    reading = st.sidebar.slider("Reading", 0.0, 9.0, 6.5, 0.5)
    writing = st.sidebar.slider("Writing", 0.0, 9.0, 6.0, 0.5)
    speaking = st.sidebar.slider("Speaking", 0.0, 9.0, 6.0, 0.5)

    st.sidebar.subheader("Preparation Metrics")
    accuracy = st.sidebar.slider("Practice Accuracy (%)", 0, 100, 65)
    consistency = st.sidebar.slider("Study Days per Week", 0, 7, 4)
    mocks = st.sidebar.slider("Mock Tests Taken", 0, 10, 3)

    return {
        "target_band": target_band,
        "exam_days": exam_days,
        "listening": listening,
        "reading": reading,
        "writing": writing,
        "speaking": speaking,
        "accuracy": accuracy,
        "consistency": consistency,
        "mocks": mocks
    }


def display_key_metrics(readiness, projected_band, band_gap, zone):
    """
    Display key metrics in a 4-column layout.
    
    Args:
        readiness: Readiness percentage
        projected_band: Projected IELTS band
        band_gap: Gap to target band
        zone: Current readiness zone
    """
    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Twin Readiness", f"{readiness}%")
    col2.metric("Projected Band", projected_band)
    col3.metric("Gap to Target", band_gap if band_gap > 0 else "Achieved")
    col4.metric("Current Zone", zone)

    st.progress(readiness)
