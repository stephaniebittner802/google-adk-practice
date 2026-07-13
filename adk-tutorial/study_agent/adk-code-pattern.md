from google.adk.agents.llm_agent import Agent


def some_tool(value: str) -> dict:
    """Explain exactly what this tool does."""

    return {
        "status": "success",
        "result": value,
    }


root_agent = Agent(
    name="my_agent",
    model="gemini-flash-latest",
    description="What this agent specializes in.",
    instruction="How this agent should behave.",
    tools=[some_tool],
)