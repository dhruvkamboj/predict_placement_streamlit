# app.py

import streamlit as st
import joblib

# Load model
model = joblib.load("prediction_model.joblib")
st.set_page_config(
    page_title="Placement Predictor",
    page_icon="🎓",
    layout="centered"
)

# Sidebar inputs
st.sidebar.header("Input Student Details")

IQ = st.sidebar.number_input("IQ (Intelligence Quotient)", min_value=0, max_value=200, step=1, help="Enter the student's IQ score.")
Prev_Sem_Result = st.sidebar.number_input("Previous Semester Result", step=0.1)
CGPA = st.sidebar.number_input("CGPA", min_value=0.0, max_value=10.0, step=0.1)
Academic_Performance = st.sidebar.slider("Academic Performance (0–10)", 0, 10)
Internship_Experience = st.sidebar.radio("Internship Experience", ["Yes", "No"])
Internship_Experience = 1 if Internship_Experience == "Yes" else 0
Extra_Curricular_Score = st.sidebar.slider("Extra Curricular Score", 0, 10)
Communication_Skills = st.sidebar.slider("Communication Skills", 0, 10)
Projects_Completed = st.sidebar.number_input("Projects Completed", min_value=0, step=1)

# Main page
st.title("🎓 Placement Prediction App")
st.markdown(
    """
    This app predicts if a student is likely to be placed based on their academic and extracurricular profile.
    """
)

if st.button("Predict Placement"):
    features = [
        IQ,
        Prev_Sem_Result,
        CGPA,
        Academic_Performance,
        Internship_Experience,
        Extra_Curricular_Score,
        Communication_Skills,
        Projects_Completed
    ]

    prediction = model.predict([features])[0]
    prediction_prob = model.predict_proba([features])[0][1]

    if prediction == 1:
        st.success(f"🎉 The student is likely to be placed! ✅ (Confidence: {prediction_prob:.2%})")
    else:
        st.error(f"❌ The student is not likely to be placed. (Confidence: {prediction_prob:.2%})")
