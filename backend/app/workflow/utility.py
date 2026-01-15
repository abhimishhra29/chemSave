import os, requests
import fitz  
from urllib.parse import urlparse


def download_pdf(url: str) -> str:
    filename = os.path.basename(urlparse(url).path)
    r = requests.get(url, timeout=20, headers={"User-Agent": "Mozilla/5.0"})
    r.raise_for_status()
    if "pdf" not in (r.headers.get("content-type","").lower()):
        return None
    open(filename, "wb").write(r.content)
    return os.path.abspath(filename)

def extract_pdf_text(pdf_path: str) -> str:
    text = ""
    doc = fitz.open(pdf_path)
    text = doc.load_page(0).get_text()
    doc.close()
    return text