import fitz  # PyMuPDF

def read_pdf_text(pdf_path: str) -> str:
    all_text = ""
    with fitz.open(pdf_path) as doc:
        for page_num in range(len(doc)):
            page = doc[page_num]
            all_text += page.get_text()
    return all_text