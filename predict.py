import joblib
import pandas as pd

# Load trained model and encoders
import os


# Add this to predict.py before loading
model = joblib.load("model/placement_model.pkl")
branch_encoder = joblib.load("model/label_encoder.pkl")
tier_encoder = joblib.load("model/tier_encoder.pkl")

def predict_placement(
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
):

    # Encode categorical values
    branch = branch_encoder.transform([branch])[0]
    college_tier = tier_encoder.transform([college_tier])[0]

    input_data = pd.DataFrame([{
        "branch": branch,
        "college_tier": college_tier,
        "cgpa": cgpa,
        "backlogs": backlogs,
        "coding_skills": coding_skills,
        "dsa_score": dsa_score,
        "aptitude_score": aptitude_score,
        "communication_skills": communication_skills,
        "ml_knowledge": ml_knowledge,
        "system_design": system_design,
        "internships": internships,
        "projects_count": projects_count,
        "certifications": certifications,
        "hackathons": hackathons,
        "open_source_contributions": open_source_contributions,
        "extracurriculars": extracurriculars
    }])

    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]

    return prediction, probability
