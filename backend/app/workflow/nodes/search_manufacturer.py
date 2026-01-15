from app.workflow.state import State
from langchain_tavily import TavilySearch
from urllib.parse import urlparse

tavily = TavilySearch(max_results=7, include_domains=[".au",".com.au"])

BAD_HOST_KEYWORDS  = ["amazon.com.au", "ebay.com.au", "alibaba.com.au", "wikipedia.org","wikipedia.org","dnb.com",
    "linkedin.com",
    "facebook.com",
    "twitter.com",
    "x.com",
    "instagram.com",
    "bloomberg.com",
    "yahoo.com",
    "crunchbase.com",
    "zoominfo.com",
    "yellowpages.com.au",
    "lusha.com",
    "australianexporters.net",
    "leadiq.com",
    ]

def has_name_in_domain(url: str, name: str) -> bool:
    host = urlparse(url).netloc.lower().lstrip("www.")
    tokens = [t.lower() for t in name.split() if len(t) > 3]
    return any(t in host for t in tokens)

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
    queries = [
            f'"{manufacturer_name}" (contact OR "contact us" OR about) (site:.com.au OR site:.au)',
            f'"{manufacturer_name}" official website (site:.com.au OR site:.au)',
            f'"{manufacturer_name}" (site:.com.au OR site:.au)',
        ]
    
    query = f'"{manufacturer_name}" official website Australia site:.com.au OR site:.au'

    tavily_results = tavily.invoke(query)

    best = None
    for result in tavily_results["results"]:
        url = (result.get("url") or "").strip()
        if not url:
            continue

        low = url.lower()
        if any(b in low for b in BAD_HOST_KEYWORDS):
            continue

        if not has_name_in_domain(url, manufacturer_name):
            continue

        best = url
        break

    
    state["manufacturer_url"] = best

    print("Manufacturer URL: ", state["manufacturer_url"])
    return state

