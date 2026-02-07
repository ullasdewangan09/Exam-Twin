"""
Exam Twin - IELTS Readiness Intelligence Dashboard Main application entry point.
"""

import streamlit as st
from config import setup_page, display_hero
from ui_components import get_sidebar_inputs, display_key_metrics
from calculations import (
    calculate_projected_band,
    calculate_readiness,
    determine_zone,
    get_next_action,
    get_risk_assessment,
    get_confidence_level
)
from visualizations import create_readiness_gauge, create_momentum_chart


#Setup
setup_page()
display_hero()


# SIDEBAR & INPUTS 
inputs = get_sidebar_inputs()

target_band = inputs["target_band"]
exam_days = inputs["exam_days"]
listening = inputs["listening"]
reading = inputs["reading"]
writing = inputs["writing"]
speaking = inputs["speaking"]
accuracy = inputs["accuracy"]
consistency = inputs["consistency"]
mocks = inputs["mocks"]


# CALCULATIONS 
projected_band, average, weakest, sections = calculate_projected_band(
    listening, reading, writing, speaking
)
readiness = calculate_readiness(accuracy, consistency, mocks, average)
zone = determine_zone(readiness)
band_gap = round(target_band - projected_band, 1)


# KEY METRICS 
display_key_metrics(readiness, projected_band, band_gap, zone)


# READINESS GAUGE 
gauge_fig = create_readiness_gauge(readiness)
st.plotly_chart(gauge_fig, use_container_width=True)

st.divider()


# DASHBOARD INSIGHTS

# Row 1: Weak Section & Next Action
col1, col2 = st.columns(2)

with col1:
    with st.container(border=True):
        st.subheader("📉 What's Holding You Back?")
        section_names = ["Listening", "Reading", "Writing", "Speaking"]
        weak_section = section_names[sections.index(weakest)]

        st.warning(
            f"Your projected band is constrained by **{weak_section}**. "
            f"Improving this section by 1 band could significantly raise your overall score."
        )

with col2:
    with st.container(border=True):
        st.subheader("🚀 Next Best Action")
        action_type, message = get_next_action(readiness)
        
        if action_type == "error":
            st.error(message)
        elif action_type == "info":
            st.info(message)
        else:
            st.success(message)


# Row 2: Risk Detection & Exam Countdown
col3, col4 = st.columns(2)

with col3:
    with st.container(border=True):
        st.subheader("⚠️ Risk Detection")
        risk_level, risk_message = get_risk_assessment(band_gap, exam_days)
        
        if risk_level == "error":
            st.error(risk_message)
        else:
            st.success(risk_message)

with col4:
    with st.container(border=True):
        st.subheader("⏳ Exam Countdown")
        st.metric("Days Remaining", exam_days)

        if exam_days < 20:
            st.warning("High urgency period. Daily preparation strongly recommended.")


st.divider()


# MOMENTUM & CONFIDENCE

# Momentum Section
with st.container(border=True):
    st.subheader("📊 Preparation Momentum")
    momentum_fig = create_momentum_chart(readiness)
    st.plotly_chart(momentum_fig, use_container_width=True)


# Confidence Section
with st.container(border=True):
    st.subheader("🔍 Prediction Confidence")
    confidence = get_confidence_level(mocks, consistency)
    st.metric("Confidence Level", confidence)
    st.caption("Directional readiness indicator — not a guaranteed score.")
