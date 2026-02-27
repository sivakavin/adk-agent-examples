from google.adk.agents import LlmAgent

## create root agent
question_answering_agent = LlmAgent(
    name="question_answering_agent",
    model="gemini-2.5-flash-lite",
    description = "Question answering agent",
    instruction = """
    You are a helpful assistant that answers questions about the user's preferences.

    Here some information about the user:
    Name:
    {user_name}
    Preferences:
    {user_preferences}
    """,
)