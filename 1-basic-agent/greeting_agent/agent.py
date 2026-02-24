from google.adk.agents import Agent


root_agent = Agent(
    name="greeting_agent",
    model="gemini-2.5-flash",
    description="Greeting agent",
    instruction = """
    You are a helpful assistant that greets the user. When the user says 'hello' or some other greeting, you should respond with 'Hello! How can I assist you today?/suitable creating , before that ask user name say
    greeting along with there name.
    """
)