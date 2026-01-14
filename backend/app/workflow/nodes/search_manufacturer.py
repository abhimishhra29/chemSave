from app.workflow.state import State
from langchain_tavily import TavilySearch
from urllib.parse import urlparse

tavily = TavilySearch(max_results=1)

def search_manufacturer_node(state: State) -> State:
    """
    LangGraph Search Manufacturer node:
    - reads manufacturer_name, product_name, product_code, cas_number, description from state
    - runs Tavily search
    - stores search results in search_results
    """

    manufacturer_name = state.get("manufacturer_name", "")

    if not manufacturer_name:
        raise ValueError("manufacturer_name is required for search_manufacturer_node")
    
    query = f'"{manufacturer_name}" official website Australia site:.com.au OR site:.au'

    tavily_results = tavily.invoke(query)
    state["manufacturer_url"] = tavily_results["results"][0]["url"]
    return state

