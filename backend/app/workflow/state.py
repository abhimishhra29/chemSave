from typing import Optional
from typing_extensions import TypedDict

class State(TypedDict):
    image_bytes: bytes
    ocr_text: Optional[str]