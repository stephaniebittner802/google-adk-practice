from google.adk.agents.llm_agent import Agent
from .tools import calculate_grade, recommend_study_topic, create_study_plan

root_agent = Agent(
    model='gemini-3.5-flash',
    name='study_agent',
    description="A study assistant with grade and study-planning tools.",
    instruction="""
    You are a helpful study assistant.

    Use calculate_grade for grade calculations.
    Use recommend_study_topic when the user wants advice about what to study next.
    Use create_study_plan whenever the user asks for a structured
    plan for learning a topic.

    Never invent tool results.
    If required information is missing, ask the user for it.
    Explain the result clearly after using a tool.
    Ask for missing information when a required tool argument is not provided.
    """,
    tools=[
        calculate_grade,
        recommend_study_topic,
        create_study_plan,
    ],
)
