from app.workflow.state import State
from langchain_community.tools.tavily_search import TavilySearchResults

tavily = TavilySearchResults(max_results=5)

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

    state["search_results"] = tavily.invoke(query)

    print("Search Results:", state["search_results"])  # Print search results
    return state

    