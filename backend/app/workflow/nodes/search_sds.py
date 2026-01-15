from app.workflow.state import State
from langchain_tavily import TavilySearch
from urllib.parse import urlparse

tavily = TavilySearch(max_results=10, include_domains=[".au", ".com.au"])

def search_sds_node(state: State) -> State:
    SDS_keywords = ["sds", "safety data sheet", "safety datasheet"]

    product_name = state.get("product_name", "")
    product_code = state.get("product_code", "")
    cas_number = state.get("cas_number", "")
    manufacturer_url = state.get("manufacturer_url", "")

    domain = urlparse(manufacturer_url).netloc

    # keep query clean (minimal but better)
    search_terms = [t for t in [product_code, cas_number, product_name] if t]
    terms_query = " OR ".join(f'"{t}"' for t in search_terms)

    query = f'site:{domain} ({terms_query}) ("SDS" OR "Safety Data Sheet") filetype:pdf'
    sds_results = tavily.invoke(query)

    state["sds_search_results"] = None

    for result in sds_results.get("results", []):
        url = (result.get("url") or "")
        title = (result.get("title") or "")
        blob = (url + " " + title).lower()

        if url.lower().endswith(".pdf") and any(k in blob for k in SDS_keywords):
            state["sds_search_results"] = url
            break

    return state
