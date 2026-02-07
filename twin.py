import streamlit as st
import random
import plotly.graph_objects as go

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Exam Twin",
    layout="wide"
)

# ---------------- HERO ----------------
st.markdown("""
## 🚀 Exam Twin — IELTS Readiness Intelligence  
Predict your exam readiness, detect risks early, and take the next best action.
""")

st.divider()

# ---------------- SIDEBAR ----------------
st.sidebar.header("Enter Preparation Details")

target_band = st.sidebar.slider("Target IELTS Band", 5.0, 9.0, 7.5, 0.5)
exam_days = st.sidebar.slider("Days Until Exam", 7, 180, 45)

st.sidebar.subheader("Section Scores")

listening = st.sidebar.slider("Listening", 0.0, 9.0, 6.5, 0.5)
reading = st.sidebar.slider("Reading", 0.0, 9.0, 6.5, 0.5)
writing = st.sidebar.slider("Writing", 0.0, 9.0, 6.0, 0.5)
speaking = st.sidebar.slider("Speaking", 0.0, 9.0, 6.0, 0.5)

accuracy = st.sidebar.slider("Practice Accuracy (%)", 0, 100, 65)
consistency = st.sidebar.slider("Study Days per Week", 0, 7, 4)
mocks = st.sidebar.slider("Mock Tests Taken", 0, 10, 3)

sections = [listening, reading, writing, speaking]
weakest = min(sections)
average = sum(sections) / 4

# ---------------- BAND CEILING ----------------
projected_band = min(average, weakest + 0.5)
projected_band = round(projected_band, 1)

# ---------------- READINESS ----------------
readiness = (
    accuracy * 0.35 +
    (consistency / 7) * 100 * 0.25 +
    (mocks / 10) * 100 * 0.2 +
    (average / 9) * 100 * 0.2
)

readiness = int(min(100, readiness))
band_gap = round(target_band - projected_band, 1)

# ---------------- ZONE ----------------
if readiness < 50:
    zone = "🔴 Risk Zone"
elif readiness < 75:
    zone = "🟡 Momentum Zone"
else:
    zone = "🟢 Safe Zone"

# ---------------- METRICS ----------------
col1, col2, col3, col4 = st.columns(4)

col1.metric("Twin Readiness", f"{readiness}%")
col2.metric("Projected Band", projected_band)
col3.metric("Gap to Target", band_gap if band_gap > 0 else "Achieved")
col4.metric("Current Zone", zone)

st.progress(readiness)

# ---------------- GAUGE ----------------
fig = go.Figure(go.Indicator(
    mode="gauge+number",
    value=readiness,
    title={'text': "Exam Readiness"},
    gauge={
        'axis': {'range': [0, 100]},
        'bar': {'color': "#4f46e5"},
        'steps': [
            {'range': [0, 50], 'color': '#fee2e2'},
            {'range': [50, 75], 'color': '#fef3c7'},
            {'range': [75, 100], 'color': '#dcfce7'}
        ],
    }
))

st.plotly_chart(fig, use_container_width=True)

st.divider()

# ================= DASHBOARD INSIGHTS =================

# ---------- ROW 1 ----------
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

        if readiness < 50:
            st.error("Increase study consistency to at least 4 days/week and take a mock test immediately.")
        elif readiness < 75:
            st.info("Focus on your weakest section and increase accuracy by ~10% to enter the safe zone.")
        else:
            st.success("Maintain momentum and focus on advanced practice.")

# ---------- ROW 2 ----------
col3, col4 = st.columns(2)

with col3:
    with st.container(border=True):
        st.subheader("⚠️ Risk Detection")

        if band_gap > 0 and exam_days < 30:
            st.error(f"At current pace, you may miss your target by ~{band_gap} band.")
        else:
            st.success("You are currently on track based on preparation velocity.")

with col4:
    with st.container(border=True):
        st.subheader("⏳ Exam Countdown")
        st.metric("Days Remaining", exam_days)

        if exam_days < 20:
            st.warning("High urgency period. Daily preparation strongly recommended.")

st.divider()

# ---------- MOMENTUM ----------
with st.container(border=True):

    st.subheader("📊 Preparation Momentum")

    weeks = ["Week 1", "Week 2", "Week 3", "Current"]
    trend = [
        max(20, readiness - random.randint(10,20)),
        max(30, readiness - random.randint(5,15)),
        max(40, readiness - random.randint(0,10)),
        readiness
    ]

    trend_fig = go.Figure()
    trend_fig.add_trace(go.Scatter(
        x=weeks,
        y=trend,
        mode='lines+markers',
        line=dict(width=4)
    ))

    trend_fig.update_layout(
        yaxis_title="Readiness %",
        template="simple_white"
    )

    st.plotly_chart(trend_fig, use_container_width=True)

# ---------- CONFIDENCE ----------
with st.container(border=True):

    st.subheader("🔍 Prediction Confidence")

    if mocks >= 5 and consistency >= 4:
        confidence = "High"
    elif mocks >= 2:
        confidence = "Medium"
    else:
        confidence = "Low"

    st.metric("Confidence Level", confidence)

    st.caption("Directional readiness indicator — not a guaranteed score.")
