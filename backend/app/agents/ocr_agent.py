import os
from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv()

class OCRAgent:
    def __init__(self):
        self.model = "mistral-small-latest"
        self.api_url =  "https://api.mistral.ai/v1/chat/completions"
        self.api_key = os.getenv("MISTRAL_API_KEY")