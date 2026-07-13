def calculate_grade(
    earned_points: float,
    total_points: float,
) -> dict:
    """
    Calculate a student's percentage and letter grade.

    Args:
        earned_points: Number of points the student earned.
        total_points: Total number of possible points.

    Returns:
        A dictionary containing the percentage and letter grade.
    """

    if total_points <= 0:
        return {
            "status": "error",
            "message": "Total points must be greater than zero.",
        }
    
    percentage = earned_points / total_points * 100

    if percentage >= 90:
        letter_grade = "A"
    elif percentage >= 80:
        letter_grade = "B"
    elif percentage >= 70:
        letter_grade = "C"
    elif percentage >= 60:
        letter_grade = "D"
    else:
        letter_grade = "F"

    return {
        "status": "success",
        "earned_points": earned_points,
        "total_points": total_points,
        "percentage": round(percentage, 2),
        "letter_grade": letter_grade,
    }

def recommend_study_topic(
    subject: str,
    confidence_level: int,
) -> dict:
    """
    Recommend what the student should study next.

    Args:
        subject: The subject the student is studying.
        confidence_level: Student confidence from 1 to 5.

    Returns:
        A study recommendation based on confidence.
    """

    if confidence_level < 1 or confidence_level > 5:
        return {
            "status": "error",
            "message": "Confidence level must be between 1 and 5.",
        }

    if confidence_level <= 2:
        recommendation = (
            f"Review the fundamentals of {subject}, then complete "
            "several guided practice problems."
        )
    elif confidence_level <= 4:
        recommendation = (
            f"Practice intermediate {subject} problems and review "
            "any mistakes carefully."
        )
    else:
        recommendation = (
            f"Try advanced {subject} problems or teach the topic "
            "to someone else."
        )

    return {
        "status": "success",
        "subject": subject,
        "confidence_level": confidence_level,
        "recommendation": recommendation,
    }

def create_study_plan(
    topic: str,
    days: int,
    minutes_per_day: int = 30,
) -> dict:
    """
    Create a simple study plan.

    Args:
        topic: Topic the student wants to learn.
        days: Number of days available.
        minutes_per_day: Daily study time. Defaults to 30.
    """

    return {
        "status": "success",
        "topic": topic,
        "days": days,
        "minutes_per_day": minutes_per_day,
        "total_minutes": days * minutes_per_day,
    }