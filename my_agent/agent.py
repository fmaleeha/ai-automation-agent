from google.adk.agents import Agent

root_agent = Agent(
    model="gemini-2.5-flash"
    ,
    name="my_agent",
    description="test",
    instruction="test"
)