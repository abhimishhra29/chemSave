import os
from mistralai import Mistral
from dotenv import load_dotenv
from langchain_core.utils.json import parse_json_markdown
import base64
from mistralai import Mistral
load_dotenv()

class OCRAgent:
    def __init__(self):
        self.model = "mistral-small-latest"
        self.client = Mistral(api_key=os.environ["MISTRAL_API_KEY"])

    def process(self, image_bytes: bytes, content_type="image/jpeg") -> str:
        b64 = base64.b64encode(image_bytes).decode()
        data_url = f"data:{content_type};base64,{b64}"

        prompt = (
            "You are an OCR agent. Extract ALL visible text exactly as shown, "
            "preserving order as best as possible. Then, if possible, identify:\n"
            "- Product Name\n"
            "- product_code: any SKU/catalog/ID/code (often alphanumeric; may include hyphens/slashes).\n"
            "- CAS Number (if available)\n"
            "- Manufacturer Name\n"
            "- Short chemical or product description\n\n"
            "Return ONLY JSON with keys: full_text, product_name, product_code, "
            "cas_number, manufacturer_name, description. Use null when unknown. "
            "Do not fabricate."
        )


        resp = self.client.chat.complete(
            model=self.model,
            messages=[{
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt},
                    {"type": "image_url", "image_url": data_url},
                ],
            }],
        )

        raw = resp.choices[0].message.content
        
        return parse_json_markdown(raw)