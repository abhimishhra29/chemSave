import os, requests
import fitz  

def download_pdf(url: str) -> str:
    filename = url.split("/")[-1]
    r = requests.get(url, timeout=20)
    r.raise_for_status()
    open(filename, "wb").write(r.content)
    return os.path.abspath(filename)

def extract_pdf_text(pdf_path: str) -> str:
    text = ""
    doc = fitz.open(pdf_path)
    text = doc.load_page(0).get_text()
    doc.close()
    return text