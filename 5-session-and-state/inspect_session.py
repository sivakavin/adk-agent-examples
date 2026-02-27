from google.adk.sessions import InMemorySessionService
import inspect

print("create_session", inspect.signature(InMemorySessionService.create_session))
print("get_session", inspect.signature(InMemorySessionService.get_session))
print(inspect.getsource(InMemorySessionService))
