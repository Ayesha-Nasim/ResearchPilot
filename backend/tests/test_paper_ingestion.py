from pathlib import Path

from app.services.paper_ingestion import extract_pdf_pages


TEST_PDF = (
    Path(__file__).resolve().parents[2]
    / "data"
    / "papers"
    / "test_paper.pdf"
)


def test_extract_pdf_pages():
    pages = extract_pdf_pages(str(TEST_PDF))

    assert len(pages) == 11
    assert pages[0]["page_number"] == 1
    assert pages[0]["text"]
    assert pages[1]["page_number"] == 2
    assert pages[1]["text"]