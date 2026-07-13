from google.adk.agents.llm_agent import Agent

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


root_agent = Agent(
    model='gemini-3.5-flash',
    name='study_agent',
    description="A study assistant that can explain topics and calculae grades.",
    instruction="""
    You are a helpful study assistant.

    Explain concepts clearly and use simple language.

    When the user asks you to calculate a grade, use the
    calculate_grade tool. Do not calculate the grade yourself.

    Explain the tool result naturally to the user.
    """,
    tools=[calculate_grade]
)
