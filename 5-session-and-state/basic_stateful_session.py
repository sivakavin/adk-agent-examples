from dotenv import load_dotenv
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types
# from question_answering_agent import question_answering_agent
from question_answering_agent.agent import question_answering_agent
import uuid
import asyncio

load_dotenv()

async def main():
    ## create a new session service to store state
    session_service_stateful = InMemorySessionService()

    initial_state = {
        "user_name" : "sivakavin",
        "user_preferences" : """
            - I like to play keyboard and I am a software engineer. I am interested in learning about new technologies and programming languages. I also enjoy reading tech blogs and watching tech videos on YouTube.
            - Favorite food is biriyani
            - Love to dance 
        """
    }

    ## Create new session
    APP_NAME = "GenMan_Bot"
    USER_ID = "sivakavin"
    SESSION_ID = str(uuid.uuid4())
    stateful_session = await session_service_stateful.create_session(
        app_name=APP_NAME,
        user_id=USER_ID,
        session_id=SESSION_ID,
        state=initial_state
    )

    print("CREATED NEW SESSION WITH ID")
    print("SESSION_ID: ", SESSION_ID)

    runner = Runner(
        agent=question_answering_agent,
        app_name=APP_NAME,
        session_service =session_service_stateful
    )

    new_message = types.Content(
        role="user",parts=[types.Part(text="what is sivakavin's favorite food?")]
    )

    print(f"new_message: {new_message}")

    for event in runner.run(user_id = USER_ID,session_id = SESSION_ID,
        new_message = new_message):
        if event.is_final_response():
            if event.content and event.content.parts:
                print("FINAL RESPONSE: ", event.content.parts[0].text)

    print("=== Session Event Exploration ====")
    session = await session_service_stateful.get_session(app_name=APP_NAME,user_id=USER_ID,session_id= SESSION_ID)

    ## Log final session state
    print("==== FINAL SESSION STATE ==== ")
    for key,value in session.state.items():
        print(f"{key} : {value}")

if __name__ == "__main__":
    asyncio.run(main())
