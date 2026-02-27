from google.adk.agents import Agent
from google.adk.tools import google_search
from datetime import datetime

def echo_tool(text: str) -> dict:
    return {
        "message": str(text)  # force string
    }

# def get_current_time()-> dict:
#     """Get the current time in ISO format. format YYYY-MM-DDTHH:MM:SS.mmmmmm"""    
#     # return {"current_time": str(datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f"))}  
#     return {"current_time": "2024-06-01T12:00:00.000000"}  # Mocked time for 

root_agent = Agent(
    name="tool_agent",
    model="gemini-2.5-flash",
    description="Tool agent",
    instruction = """ 
   You are helpful assistant that can use following tools:
   - echo_tool: This tool takes a string input and returns it as output. It is useful for testing and debugging purposes.
    """,
    tools=[echo_tool]
)