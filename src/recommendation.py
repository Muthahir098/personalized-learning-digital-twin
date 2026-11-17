def generate_recommendations(student):

    recommendations = []

    # Math
    if student["math_score"] < 50:
        recommendations.append(
            "Practice Math for 30 minutes daily."
        )
    elif student["math_score"] < 70:
        recommendations.append(
            "Spend more time practicing Math problems."
        )

    # Python
    if student["python_score"] < 50:
        recommendations.append(
            "Practice Python programming using small coding exercises."
        )
    elif student["python_score"] < 70:
        recommendations.append(
            "Practice Python regularly and work on small projects."
        )

    # English
    if student["english_score"] < 50:
        recommendations.append(
            "Improve English through reading and vocabulary exercises."
        )
    elif student["english_score"] < 70:
        recommendations.append(
            "Spend more time on English reading and communication."
        )

    # Attendance
    if student["attendance"] < 75:
        recommendations.append(
            "Improve attendance to maintain consistent learning."
        )

    # Study hours
    if student["study_hours"] < 2:
        recommendations.append(
            "Increase daily study time to at least 2 hours."
        )

    # Quiz
    if student["quiz_score"] < 60:
        recommendations.append(
            "Take additional practice quizzes to improve understanding."
        )

    # Assignments
    if student["assignments_completed"] < 5:
        recommendations.append(
            "Complete more assignments to strengthen practical skills."
        )

    # If no weakness is found
    if not recommendations:
        recommendations.append(
            "Keep up the good work and continue your current study routine."
        )

    return recommendations