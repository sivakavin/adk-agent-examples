import os
import random
from dotenv import load_dotenv
from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

load_dotenv()

groq_model = LiteLlm(
    model="groq/qwen/qwen3-32b",
    temperature=0.3,
    api_key=os.getenv("GROQ_API_KEY")
)

def get_dad_joke() -> dict:
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "Why don't skeletons fight each other? They don't have the guts!",
        "What do you call fake spaghetti? An impasta!",
        "Why did the bicycle fall over? Because it was two-tired!"
    ]
    return {"joke": random.choice(jokes)}

root_agent = Agent(
    name="dad_joke_agent",
    model=groq_model,
    description="A dad joke agent.",
    instruction="""
You are a dad joke agent.
Always use the get_dad_joke tool.
Return only the joke.
""",
    tools=[get_dad_joke]
)