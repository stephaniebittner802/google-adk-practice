def calculate_grade(
    earned_points: float,
    total_points: float,
) -> dict:
    """
    Calculate a student's percentage and letter grade.

    Args:
        earned_points: Points earned by the student.
        total_points: Total possible points.

    Returns:
        The calculated percentage and letter grade.
    """

    if total_points <= 0:
        return {
            "status": "error",
            "message": "Total points must be greater than zero.",
        }

    if earned_points < 0:
        return {
            "status": "error",
            "message": "Earned points cannot be negative.",
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
        "percentage": round(percentage, 2),
        "letter_grade": letter_grade,
    }


def create_study_plan(
    topic: str,
    days: int,
    minutes_per_day: int = 30,
) -> dict:
    """
    Create a basic study plan.

    Args:
        topic: Topic the student wants to study.
        days: Number of study days.
        minutes_per_day: Minutes available each day.

    Returns:
        A daily study plan.
    """

    if days <= 0:
        return {
            "status": "error",
            "message": "Days must be greater than zero.",
        }

    if minutes_per_day <= 0:
        return {
            "status": "error",
            "message": "Minutes per day must be greater than zero.",
        }

    activities = [
        "Review the fundamentals",
        "Study worked examples",
        "Complete guided practice",
        "Complete independent practice",
        "Review mistakes and summarize",
    ]

    plan = []

    for day in range(1, days + 1):
        activity_index = (day - 1) % len(activities)

        plan.append(
            {
                "day": day,
                "topic": topic,
                "minutes": minutes_per_day,
                "activity": activities[activity_index],
            }
        )

    return {
        "status": "success",
        "topic": topic,
        "total_minutes": days * minutes_per_day,
        "plan": plan,
    }