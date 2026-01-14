import json
from app.workflow.state import State
from app.agents.ocr_agent import OCRAgent

ocr_agent = OCRAgent()

def ocr_node(state: State) -> State:
    """
    LangGraph OCR node:
    - reads image_bytes from state
    - runs Mistral OCR
    - stores extracted text in ocr_text
    """
    
    image_bytes = state["image_bytes"]
    ocr_result = ocr_agent.process(image_bytes)

    state["product_name"] = ocr_result.get("product_name")
    state["product_code"] = ocr_result.get("product_code")
    state["cas_number"] = ocr_result.get("cas_number")
    state["manufacturer_name"] = ocr_result.get("manufacturer_name")
    state["description"] = ocr_result.get("description")
    
    return state