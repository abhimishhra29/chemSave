from app.workflow.state import State
from langchain_tavily import TavilySearch
from urllib.parse import urlparse

tavily = TavilySearch(max_results=3)

def search_sds_node(state: State) -> State:
    """
    LangGraph Search SDS node:
    - reads manufacturer_name, product_name, product_code, cas_number, description from state
    - runs Tavily search
    - stores search results in search_results
    """

    manufacturer_name = state.get("manufacturer_name", "")
    product_name = state.get("product_name", "")
    product_code = state.get("product_code", "")
    cas_number = state.get("cas_number", "")
    description = state.get("description", "")  
    manfactuerer_url = state.get("manufacturer_url", "")

    search_terms = [t for t in [manufacturer_name, product_name, product_code, cas_number, description] if t]
    terms_query = " OR ".join(f'"{t}"' for t in search_terms)
    query = (f'site:{manfactuerer_url} ({terms_query}) '
            '("SDS" OR "Safety Data Sheet") filetype:pdf')
    sds_results = tavily.invoke(query)
    print(sds_results)
    return state