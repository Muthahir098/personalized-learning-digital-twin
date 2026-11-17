import pandas as pd
import joblib


def create_student_twin(student):

    # Academic average
    academic_average = (
        student["math_score"]
        + student["python_score"]
        + student["english_score"]
    ) / 3

    # Overall learning score
    overall_score = (
        academic_average * 0.6
        + student["attendance"] * 0.2
        + student["quiz_score"] * 0.2
    )

    # Subject scores
    subjects = {
        "Math": student["math_score"],
        "Python": student["python_score"],
        "English": student["english_score"]
    }

    strongest_subject = max(subjects, key=subjects.get)
    weakest_subject = min(subjects, key=subjects.get)

    # Learning status
    if overall_score >= 75:
        status = "Good"
    elif overall_score >= 50:
        status = "Needs Improvement"
    else:
        status = "At Risk"

    # Load ML model
    model = joblib.load("models/student_support_model.pkl")

    # Prepare data for prediction
    features = [[
        student["attendance"],
        student["math_score"],
        student["python_score"],
        student["english_score"],
        student["study_hours"],
        student["quiz_score"],
        student["assignments_completed"]
    ]]

    prediction = model.predict(features)[0]

    if prediction == 1:
        support_prediction = "Needs Learning Support"
    else:
        support_prediction = "No Immediate Support Needed"

    return {
        "student_id": student["student_id"],
        "academic_average": round(academic_average, 2),
        "overall_score": round(overall_score, 2),
        "strongest_subject": strongest_subject,
        "weakest_subject": weakest_subject,
        "status": status,
        "ai_prediction": support_prediction
    }


if __name__ == "__main__":

    data = pd.read_csv("data/student_data.csv")

    # Select first student
    student = data.iloc[0]

    twin = create_student_twin(student)

    print("\n===== STUDENT DIGITAL TWIN =====")

    for key, value in twin.items():
        print(f"{key}: {value}")