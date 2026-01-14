from state import State
from agents.ocr_agent import OCRAgent

ocr_agent = OCRAgent()

def ocr_node(state: State) -> State:
    """
    LangGraph OCR node:
    - reads image_bytes from state
    - runs Mistral OCR
    - stores extracted text in ocr_text
    """

    image_bytes = state["image_bytes"]
    state["ocr_text"] = ocr_agent.process(image_bytes)
    print("OCR Text:", state["ocr_text"][:100])  # Print first 100 characters of OCR text
    return state