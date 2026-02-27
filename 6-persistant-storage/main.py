import asyncio

from dotenv import load_dotenv
from google.adk.runners import Runner
from google.adk.sessions import DatabaseSessionService
from memory_agent.agent import memory_agent
from utils import call_agent_async

load_dotenv()

# Using SQLite for persistent storage, you can switch to other databases by changing the connection string and installing the appropriate database driver.
db_url = "sqlite:///sessions.db"

session_service = DatabaseSessionService(db_url=db_url) 

initial_state = {
    "user_name" : "sivakavin",
    "reminders" : [],}

async def main():
    ## Create new session
    APP_NAME = "MemoryAgent"
    USER_ID = "aiwithsivakavin"

    existing_sessions = session_service.list_sessions(app_name=APP_NAME, user_id=USER_ID)

    if existing_sessions and len(existing_sessions) > 0:
        print("Existing session found, using the first one.")
        SESSION_ID = existing_sessions.sessions[0].id
        print("SESSION_ID: ", SESSION_ID)
    else:
        new_session = session_service.create_session(
            app_name = APP_NAME,
            user_id = USER_ID,
            state = initial_state,
        )
        SESSION_ID = new_session.id
        print("New session created with ID: ", SESSION_ID)
        