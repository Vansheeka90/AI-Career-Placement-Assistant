# 🤖 AI Career & Placement Assistant

## 👨‍💻 Team Members

- Harmanjot Singh
- Vansheeka

---

# 📌 Project Overview

AI Career & Placement Assistant is a Machine Learning based web application that predicts a student's placement chances based on academic performance, technical skills, projects, internships, and other parameters. The application also provides career guidance, skill gap analysis, and job recommendations.

---

# 🎯 Objectives

- Predict placement chances using Machine Learning.
- Help students identify skill gaps.
- Recommend suitable career paths.
- Suggest companies based on student profile.
- Provide an easy-to-use AI dashboard.

---

# 🚀 Features

- 🏠 Interactive Home Dashboard
- 🎯 AI Placement Prediction
- 💼 Career Guidance
- 📊 Skill Gap Analysis
- 💻 Job Recommendations
- 📈 Placement Probability
- 🤖 Machine Learning Prediction
- 📱 Responsive Streamlit Interface

---

# 🧠 Machine Learning Model

Algorithm Used:

- Random Forest Classifier

Why Random Forest?

- High Accuracy
- Handles Multiple Features
- Reduces Overfitting
- Fast Prediction

---

# 📂 Dataset Features

The model uses the following features:

- Branch
- College Tier
- CGPA
- Backlogs
- Coding Skills
- DSA Score
- Aptitude Score
- Communication Skills
- Machine Learning Knowledge
- System Design
- Internships
- Projects Count
- Certifications
- Hackathons
- Open Source Contributions
- Extracurricular Activities

Target Variable

- Placement Status

---

# 🛠 Technologies Used

## Programming Language

- Python

## Framework

- Streamlit

## Machine Learning

- Scikit-learn

## Libraries

- Pandas
- NumPy
- Joblib

## Development Environment

- Visual Studio Code

---

# 📁 Project Structure

```
AI_Career_Placement/
│
├── app.py
├── predict.py
├── train_model.py
├── requirements.txt
├── README.md
│
├── dataset/
│   └── student_placement.csv
│
├── model/
│   ├── placement_model.pkl
│   ├── label_encoder.pkl
│   └── tier_encoder.pkl
│
├── pages/
│   ├── 1_Placement_Prediction.py
│   ├── 2_Career_Guidance.py
│   ├── 3_Skill_Gap_Analysis.py
│   └── 4_Job_Recommendations.py
│
└── utils/
    ├── __init__.py
    ├── helper.py
    ├── feature.py
    └── preprocessing.py
```

---

# ⚙ Installation

### Clone the Repository

```bash
git clone <repository-link>
```

### Open Project Folder

```bash
cd AI_Career_Placement
```

### Install Required Libraries

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
python -m streamlit run app.py
```

---

# 📦 Requirements

```
streamlit
pandas
numpy
scikit-learn
joblib
```

---

# 📈 Workflow

1. Load Dataset
2. Data Preprocessing
3. Train Machine Learning Model
4. Save Model (.pkl)
5. Load Model
6. User Inputs Data
7. AI Predicts Placement
8. Display Probability
9. Career Guidance
10. Skill Gap Analysis
11. Job Recommendations

---

# 📸 Application Pages

- Home
- Placement Prediction
- Career Guidance
- Skill Gap Analysis
- Job Recommendations

---

# 🎯 Future Enhancements

- Resume Analyzer
- Live Job Portal Integration
- Interview Preparation
- AI Chatbot
- Salary Prediction
- Resume Score Analysis

---

# 📚 Learning Outcomes

- Machine Learning Model Training
- Data Preprocessing
- Streamlit Development
- Model Deployment
- UI Design
- Feature Engineering
- Python Project Development

---

# 👨‍💻 Developed By

Harmanjot Singh

Vansheeka

---

# 📄 License

This project is developed for educational purposes.