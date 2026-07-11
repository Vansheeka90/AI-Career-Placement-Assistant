import streamlit as st
from predict import predict_placement
import pandas as pd
import os

st.set_page_config(
    page_title="Placement Prediction",
    page_icon="🎯",
    layout="wide"
)

st.markdown("""
<style>

.main{
    background:#050816;
}

.card{
    background:rgba(255,255,255,0.06);
    padding:20px;
    border-radius:18px;
    border:1px solid rgba(0,245,255,.25);
}

h1,h2,h3{
    color:#00F5FF;
}

.stButton>button{
    width:100%;
    height:50px;
    border-radius:12px;
    background:#00F5FF;
    color:black;
    font-size:18px;
    font-weight:bold;
}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="card">

<h1 align="center">🎯 AI Placement Prediction</h1>

<p align="center">
Enter your academic profile and technical skills to predict your placement chances.
</p>

</div>
""", unsafe_allow_html=True)

st.write("")

st.write("Enter your details below")

name = st.text_input("👤 Student Name")

st.subheader("🎓 Academic Profile")

col1, col2 = st.columns(2)

with col1:

    branch = st.selectbox(
        "Branch",
        ["CSE","IT","ECE","EE","ME","Civil"]
    )

    cgpa = st.number_input(
        "CGPA",
        0.0,
        10.0,
        8.0
    )

with col2:

    college_tier = st.selectbox(
        "College Tier",
        ["Tier-1","Tier-2","Tier-3"]
    )

    backlogs = st.number_input(
        "Backlogs",
        0,
        10,
        0
    )

st.write("")

st.subheader("💻 Technical Skills")

col1, col2 = st.columns(2)

with col1:

    coding_skills = st.slider(
        "Coding Skills",
        0,
        10,
        7
    )

    dsa_score = st.slider(
        "DSA Score",
        0,
        100,
        70
    )

    ml_knowledge = st.slider(
        "ML Knowledge",
        0,
        10,
        6
    )

with col2:

    aptitude_score = st.slider(
        "Aptitude Score",
        0,
        100,
        70
    )

    system_design = st.slider(
        "System Design",
        0,
        10,
        5
    )

    communication_skills = st.slider(
        "Communication Skills",
        0,
        10,
        7
    )
    
st.write("")

st.subheader("🚀 Experience & Achievements")

col1, col2 = st.columns(2)

with col1:

    internships = st.number_input(
        "Internships",
        0,
        10,
        1
    )

    projects_count = st.number_input(
        "Projects",
        0,
        20,
        3
    )

    certifications = st.number_input(
        "Certifications",
        0,
        20,
        2
    )

with col2:

    hackathons = st.number_input(
        "Hackathons",
        0,
        20,
        1
    )

    open_source_contributions = st.number_input(
        "Open Source Contributions",
        0,
        20,
        0
    )

    extracurriculars = st.slider(
        "Extracurricular Activities",
        0,
        10,
        5
    )

st.write("")
st.divider()

if st.button("🚀 Predict Placement"):

    prediction, probability = predict_placement(

        branch,
        college_tier,
        cgpa,
        backlogs,
        coding_skills,
        dsa_score,
        aptitude_score,
        communication_skills,
        ml_knowledge,
        system_design,
        internships,
        projects_count,
        certifications,
        hackathons,
        open_source_contributions,
        extracurriculars

    )

    percentage = probability * 100

    st.subheader("🎯 Prediction Result")

    if prediction == 1:
        st.success("🟢 High Placement Chance")
    else:
        st.error("🔴 Low Placement Chance")

    st.metric(
        "Placement Probability",
        f"{percentage:.2f}%"
    )

    st.progress(probability)
      # ================= Save Prediction History =================

    result = {
        "Name": name,
        "Branch": branch,
        "College Tier": college_tier,
        "CGPA": cgpa,
        "Prediction": "Placed" if prediction == 1 else "Not Placed",
        "Probability": f"{percentage:.2f}%"
    }

    if os.path.exists("prediction_history.csv"):
        df = pd.read_csv("prediction_history.csv")
        df = pd.concat([df, pd.DataFrame([result])], ignore_index=True)
    else:
        df = pd.DataFrame([result])

    df.to_csv("prediction_history.csv", index=False)