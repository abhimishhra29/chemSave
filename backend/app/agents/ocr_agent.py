import os
from mistralai import Mistral
from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv()

import base64
from mistralai import Mistral

class OCRAgent:
    def __init__(self):
        self.model = "mistral-small-latest"
        self.client = Mistral(api_key=os.environ["MISTRAL_API_KEY"])

    def process(self, image_bytes: bytes, content_type="image/jpeg") -> str:
        b64 = base64.b64encode(image_bytes).decode()
        data_url = f"data:{content_type};base64,{b64}"

        resp = self.client.chat.complete(
            model=self.model,
            messages=[{
                "role": "user",
                "content": [
                    {"type": "text", "text": "Read all text in this image. Output only the text."},
                    {"type": "image_url", "image_url": data_url},
                ],
            }],
        )
        return resp.choices[0].message.content