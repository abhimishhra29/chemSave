from typing import Optional
from typing_extensions import TypedDict

class State(TypedDict):
    image_bytes: bytes
    ocr_text: Optional[str]

    # inputs to search (you can fill these later via an LLM parse node)
    manufacturer_name: Optional[str]
    manufacturer_url: Optional[str]
    product_name: Optional[str]
    product_code: Optional[str]
    cas_number: Optional[str]
    description: Optional[str]
    sds_search_results: Optional[str]
    validation_status:  bool
    
