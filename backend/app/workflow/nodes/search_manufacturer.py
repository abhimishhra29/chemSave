from app.workflow.state import State
from langchain_tavily import TavilySearch

tavily = TavilySearch(max_results=5, include_domains=[".au",".com.au"])

BAD_HOST_KEYWORDS  = ["amazon.com.au", "ebay.com.au", "alibaba.com.au", "wikipedia.org","wikipedia.org","dnb.com",
    "linkedin.com",
    "facebook.com",
    "twitter.com",
    "x.com",
    "instagram.com",
    "bloomberg.com",
    "yahoo.com",
    "crunchbase.com",
    "zoominfo.com"]

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

    tavily_results = tavily.invoke(query)
    
    best = None

    best = None
    for result in tavily_results["results"]:
        url = (result.get("url") or "").strip()
        if not url:
            continue
        low = url.lower()
        if any(b in low for b in BAD_HOST_KEYWORDS):
            continue

        best = url
        break

    
    state["manufacturer_url"] = best

    print("Manufacturer URL: ", state["manufacturer_url"])
    return state

