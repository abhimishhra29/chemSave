from app.workflow.state import State
from app.agents.validation_agent import validationAgent
from app.workflow.utility import download_pdf, extract_pdf_text

validation_agent = validationAgent()

def validate_sds_node(state: State) -> State:

    sds_url=state["sds_search_results"]
    sds_file_path=download_pdf(sds_url)
    sds_text=extract_pdf_text(sds_file_path)

    expected=[]
     
    cas_number=state.get("cas_number")
    product_code=state.get("product_code")
    product_name=state.get("product_name")
    manufacturer_name=state.get("manufacturer_name")

    if cas_number:
        expected.append("CAS number")
    if product_code:
        expected.append("product code")
    if product_name:
        expected.append("product name")
    if manufacturer_name:
        expected.append("manufacturer name")
    
    result=validation_agent.validate_sds(expected, sds_text)
    state["validation_status"] = bool(result.get("is_match"))
    print("Validation Status: ", state["validation_status"])
    return state

    
    