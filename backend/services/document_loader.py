from pypdf import PdfReader
from pathlib import Path


def extract_text_from_pdf(file_path: str) -> str:
    reader = PdfReader(file_path)
    text = ""

    for page in reader.pages:
        text += page.extract_text() + "\n"

    return text


def extract_text_from_txt(file_path: str) -> str:
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()


def load_document(file_path: str) -> str:
    path = Path(file_path)

    if path.suffix == ".pdf":
        return extract_text_from_pdf(file_path)

    elif path.suffix == ".txt":
        return extract_text_from_txt(file_path)

    else:
        raise ValueError("Unsupported file type")