import streamlit as st

from src.prediction import classify_score, predict_score

st.set_page_config(page_title="Student Performance Predictor", page_icon="📚")

st.title("📚 Student Performance Predictor")
st.write("Estimate academic performance from study and academic inputs.")

with st.form("prediction_form"):
    study_hours = st.slider("Study hours per day", 0.0, 12.0, 4.0, 0.5)
    attendance = st.slider("Attendance (%)", 0, 100, 75)
    previous_marks = st.slider("Previous marks (%)", 0, 100, 65)
    assignments_completed = st.slider("Assignments completed", 0, 10, 7)
    internal_marks = st.slider("Internal marks (%)", 0, 100, 65)
    sleep_hours = st.slider("Sleep hours per day", 0.0, 12.0, 7.0, 0.5)

    submitted = st.form_submit_button("Predict Performance")

if submitted:
    values = {
        "study_hours": study_hours,
        "attendance": attendance,
        "previous_marks": previous_marks,
        "assignments_completed": assignments_completed,
        "internal_marks": internal_marks,
        "sleep_hours": sleep_hours,
    }

    try:
        score = predict_score(values)
        category, risk = classify_score(score)

        st.metric("Predicted score", f"{score:.1f}%")
        st.write(f"**Performance:** {category}")
        st.write(f"**Risk level:** {risk}")

        if risk == "High":
            st.warning("The model indicates a higher academic risk. Focus on attendance, study consistency, and internal performance.")
        elif risk == "Medium":
            st.info("The model indicates moderate risk. Improving consistency could raise the predicted score.")
        else:
            st.success("The model predicts a strong performance range.")
    except FileNotFoundError as exc:
        st.error(str(exc))
