import sys
import os

import streamlit as st
import pandas as pd
import plotly.express as px

# Add project root to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.digital_twin import create_student_twin
from src.recommendation import generate_recommendations


# Page configuration
st.set_page_config(
    page_title="Personalized Learning Digital Twin",
    page_icon="🎓",
    layout="wide"
)


# Title
st.title("🎓 Personalized Learning Digital Twin")

st.write(
    "AI-powered system for analyzing student performance "
    "and generating personalized learning recommendations."
)


# Load student data
data = pd.read_csv("data/student_data.csv")


# Student selection
student_id = st.selectbox(
    "Select a Student",
    data["student_id"].tolist()
)


# Get selected student
student = data[data["student_id"] == student_id].iloc[0]


# Create Digital Twin
twin = create_student_twin(student)


# Generate recommendations
recommendations = generate_recommendations(student)


st.divider()


# -----------------------------
# Student Overview
# -----------------------------

st.subheader("👤 Student Digital Twin")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Overall Score",
        f"{twin['overall_score']:.1f}"
    )

with col2:
    st.metric(
        "Academic Average",
        f"{twin['academic_average']:.1f}"
    )

with col3:
    st.metric(
        "Attendance",
        f"{student['attendance']}%"
    )

with col4:
    st.metric(
        "Study Hours",
        f"{student['study_hours']} hrs/day"
    )


st.divider()


# -----------------------------
# Student Status
# -----------------------------

col1, col2 = st.columns(2)

with col1:
    st.subheader("📊 Learning Status")
    st.info(twin["status"])

with col2:
    st.subheader("🤖 AI Prediction")
    if twin["ai_prediction"] == "Needs Learning Support":
        st.warning(twin["ai_prediction"])
    else:
        st.success(twin["ai_prediction"])


# -----------------------------
# Subject Performance
# -----------------------------

st.subheader("📚 Subject Performance")

subject_data = pd.DataFrame({
    "Subject": ["Math", "Python", "English"],
    "Score": [
        student["math_score"],
        student["python_score"],
        student["english_score"]
    ]
})

fig = px.bar(
    subject_data,
    x="Subject",
    y="Score",
    title="Subject-wise Performance",
    range_y=[0, 100]
)

st.plotly_chart(fig, use_container_width=True)


# -----------------------------
# Strength & Weakness
# -----------------------------

col1, col2 = st.columns(2)

with col1:
    st.subheader("💪 Strongest Subject")
    st.success(twin["strongest_subject"])

with col2:
    st.subheader("⚠️ Weakest Subject")
    st.warning(twin["weakest_subject"])


# -----------------------------
# Other Performance Data
# -----------------------------

st.subheader("📈 Learning Metrics")

metrics_data = pd.DataFrame({
    "Metric": [
        "Attendance",
        "Quiz Score",
        "Assignments Completed"
    ],
    "Value": [
        student["attendance"],
        student["quiz_score"],
        student["assignments_completed"] * 10
    ]
})

fig2 = px.bar(
    metrics_data,
    x="Metric",
    y="Value",
    title="Additional Learning Metrics"
)

st.plotly_chart(fig2, use_container_width=True)


# -----------------------------
# Recommendations
# -----------------------------

st.subheader("💡 Personalized Recommendations")

for recommendation in recommendations:
    st.write("👉", recommendation)


st.divider()

st.caption(
    "AI-Powered Personalized Learning Digital Twin"
)