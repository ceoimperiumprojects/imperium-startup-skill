"""EPUB text extraction."""

import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup


def extract_text_from_epub(epub_path: str) -> str:
    """Ekstrahuje tekst iz EPUB fajla."""
    book = epub.read_epub(epub_path)

    text_parts = []

    for item in book.get_items():
        if item.get_type() == ebooklib.ITEM_DOCUMENT:
            soup = BeautifulSoup(item.get_content(), 'html.parser')
            text = soup.get_text(separator='\n', strip=True)
            if text:
                text_parts.append(text)

    return '\n\n'.join(text_parts)


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        text = extract_text_from_epub(sys.argv[1])
        print(f"Extracted {len(text)} characters")
        print(text[:500])
