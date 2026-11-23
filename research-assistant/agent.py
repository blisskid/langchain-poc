from managed_deepagents import define_deep_agent

from tools.search import internet_search

agent = define_deep_agent(
    name="research-assistant",
    model="google_genai:gemini-3.5-flash-lite",
    tools=[internet_search],
)
