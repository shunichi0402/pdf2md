from pdf2md.convert_markdown import convert_pdf_text_to_markdown
from pdf2md.read_pdf import read_pdf_text

def convert(pdf_path: str) -> str:
    pdf_text = read_pdf_text(pdf_path)
    return convert_pdf_text_to_markdown(pdf_text)
