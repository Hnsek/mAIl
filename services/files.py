from pdfminer.high_level import extract_text
from io import BytesIO

def extract_text_from_pdf(file):
    return extract_text(BytesIO(file.read()))

def extract_text_from_txt(file):
    try:
        file.seek(0)

        text = file.read().decode('utf-8')
        return text
    except Exception as e:
        return f"Text reading error: {e}"