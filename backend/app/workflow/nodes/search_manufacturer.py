from app.workflow.state import State
from langchain_tavily import TavilySearch

tavily = TavilySearch(max_results=5, include_domains=[".au"])

def search_manufacturer_node(state: State) -> State:
    """
    LangGraph Search Manufacturer node:
    - reads manufacturer_name
    - runs Tavily search
    - stores search results in tavily_results
    """

    manufacturer_name = state.get("manufacturer_name", "")

    if not manufacturer_name:
        raise ValueError("manufacturer_name is required for search_manufacturer_node")
    
    query = f'"{manufacturer_name}" official website Australia site:.com.au OR site:.au'
    # tavily_results = tavily.invoke(query)
    tavily_results = tavily.invoke(query)
    state["manufacturer_url"] = tavily_results["results"][0]["url"]

    print("Manufacturer URL: ", state["manufacturer_url"])
    return state

