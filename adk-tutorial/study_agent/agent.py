from google.adk.agents.llm_agent import Agent
from .tools import calculate_grade, create_study_plan

root_agent = Agent(
    model='gemini-3.5-flash',
    name='study_agent',
    description=(
        "A beginner-friendly study assistant with tools "
        "for calculating grades and creating study plans."
    ),
    instruction="""
    You are a helpful study assistant.

    Use calculate_grade whenever the user asks you to calculate a grade.

    Use create_study_plan whenever the user asks for a structured
    study schedule.

    Explain your answers clearly.
    Never invent tool results.
    """,
    tools=[
        calculate_grade,
        create_study_plan,
    ],
)
