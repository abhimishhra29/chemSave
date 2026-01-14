import os
from mistralai import Mistral
from dotenv import load_dotenv
from langchain_core.utils.json import parse_json_markdown
import base64
from mistralai import Mistral
load_dotenv()

class validationAgent:
    def __init__(self):
        self.model = "mistral-small-latest"
        self.client = Mistral(api_key=os.environ["MISTRAL_API_KEY"])

    
    def validate_sds(self, expected: list, pdf_text: str) -> dict:
            prompt = (  
                 f"""You are validating a Safety Data Sheet (SDS) document.

                    Expected product information:
                    {expected}

                    First page of SDS:
                    {pdf_text}

                    Question: Does this SDS match the expected product?

                    Check if ANY of the expected identifiers (CAS number, product code, or product name) match what's in the SDS text. Be flexible with formatting and minor variations.

                    Respond ONLY with JSON:
                    {{
                        "is_match": true/false,
                        "matched_fields": ["list of what matched, e.g. 'CAS number', 'product code'"],
                        "explanation": "brief explanation of what you found"
                    }}
                    """
            )

            resp = self.client.chat.complete(
                model=self.model,
                messages=[{
                    "role": "user",
                    "content": [
                        {"type": "text", "text": prompt},
                    ],
                }],
            )

            raw = resp.choices[0].message.content
            
            return parse_json_markdown(raw)
    
    