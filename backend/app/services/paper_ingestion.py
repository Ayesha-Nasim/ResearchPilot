import pymupdf


def extract_pdf_pages(file_path: str) -> list[dict]:
    """
    Extract text from each page of a PDF.

    Returns:
        A list containing page number and extracted text.
    """

    document = pymupdf.open(file_path)

    pages = []

    for page_number, page in enumerate(document, start=1):
        text = page.get_text("text")

        pages.append(
            {
                "page_number": page_number,
                "text": text.strip(),
            }
        )

    document.close()

    return pages