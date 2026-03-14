from pypdf import PdfReader
from pathlib import Path


def extract_text_from_pdf(pdf_path: str) -> str:
    """Izvlaci tekst iz PDF fajla."""
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"
    return text


def process_multiple_pdfs(directory: str) -> dict:
    """Procesira sve PDF-ove u direktorijumu."""
    results = {}
    pdf_dir = Path(directory)
    for pdf_file in pdf_dir.glob("*.pdf"):
        results[pdf_file.name] = extract_text_from_pdf(str(pdf_file))
    return results


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        text = extract_text_from_pdf(sys.argv[1])
        print(f"Extracted {len(text)} characters")
        print(text[:500])
