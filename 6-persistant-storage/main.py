import asyncio
from dotenv import load_dotenv

from google.adk.runners import Runner
from google.adk.sessions import DatabaseSessionService
from memory_agent.agent import memory_agent
from utils import call_agent_async

load_dotenv()
db_url = "sqlite+aiosqlite:///./my_agent_data.db"
# db_url = "sqlite+aiosqlite:///C:/Users/mails/Documents/GitHub/adk-agent-examples/my_agent_data.db"

session_service = DatabaseSessionService(db_url=db_url)

initial_state = {
    "user_name": "sivakavin",
    "reminders": [],
}

async def main():
    APP_NAME = "MemoryAgent"
    USER_ID = "aiwithsivakavin"

    # ✅ async + correct response handling
    existing_sessions_res = await session_service.list_sessions(
        app_name=APP_NAME,
        user_id=USER_ID
    )
    existing_sessions = existing_sessions_res.sessions

    if existing_sessions:
        print("Existing session found, using the first one.")
        SESSION_ID = existing_sessions[0].id   # ✅ FIXED
        print("SESSION_ID:", SESSION_ID)
    else:
        new_session = await session_service.create_session(  # ✅ await added
            app_name=APP_NAME,
            user_id=USER_ID,
            state=initial_state,
        )
        SESSION_ID = new_session.id
        print("New session created with ID:", SESSION_ID)

    ### Creating Runner with session and agent
    runner = Runner(
        agent=memory_agent,
        app_name=APP_NAME,
        session_service=session_service,
    )

    print("=== Interactive Conversation with Memory Agent ===")
    print("Your reminders will be remembered across conversations.")
    print("Type 'exit' or 'quit' to end the conversation.")

    while True:
        user_input = input("You: ")

        if user_input.lower() in ["exit", "quit"]:
            print("Ending conversation. Data saved to database.")
            break

        await call_agent_async(runner, USER_ID, SESSION_ID, user_input)

if __name__ == "__main__":
    asyncio.run(main())