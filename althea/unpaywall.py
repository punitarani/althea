"""
althea/unpaywall.py

unpaywall API wrapper
"""

from pathlib import Path

import fitz
import httpx

from althea.utils import safe_filename
from config import DATA_DIR, EMAIL


async def get_paper_info(doi: str) -> dict:
    """
    Get the paper info from the Unpaywall API.

    Args:
        doi (str): DOI of the paper

    Returns:
        dict: Info of the paper
    """
    request_url = f"https://api.unpaywall.org/v2/{doi}?email={EMAIL}"
    async with httpx.AsyncClient() as client:
        response = await client.get(request_url)
        if response.status_code == 200:
            return response.json()
    return {}


async def get_paper_url(doi: str) -> str | None:
    """
    Get the URL of the paper from the Unpaywall API.

    Args:
        doi (str): DOI of the paper

    Returns:
        str | None: URL of the paper or None if not found
    """
    data = await get_paper_info(doi)
    best_oa_location = data.get("best_oa_location", None)
    if best_oa_location:
        return best_oa_location.get("url_for_pdf", None)


async def get_paper_authors(doi: str) -> list[set[str]]:
    """
    Get the authors of the paper from the Unpaywall API.

    Args:
        doi (str): DOI of the paper

    Returns:
        list[set[str]]: List of authors of the paper
    """
    data = await get_paper_info(doi)
    return data.get("z_authors", [])


async def download_paper(doi: str) -> Path | None:
    """
    Download the paper from the Unpaywall API.

    Args:
        doi (str): DOI of the paper

    Returns:
        Path | None: Path to the downloaded paper or None if not found
    """

    # Handle the case where the DOI is not found
    if doi is None:
        return None

    # Remove the prefix "https://doi.org/" from the DOI
    if doi.startswith("https://doi.org/"):
        doi = doi[16:]
    elif doi.startswith("doi.org/"):
        doi = doi[8:]

    filename = safe_filename(doi) + ".pdf"
    filepath = DATA_DIR.joinpath("pdf", filename)

    # If the file already exists, return it
    if filepath.exists():
        return filepath

    url = await get_paper_url(doi)
    if url is None:
        return None

    # Download the file
    async with httpx.AsyncClient() as client:
        response = await client.get(url, follow_redirects=True)
        if response.status_code == 200:
            with open(filepath, "wb") as f:
                f.write(response.content)
            return filepath
    return None


def extract_text(fp: Path) -> str:
    """
    Extract text from a PDF file.

    Args:
        fp (Path): Path to the PDF file

    Returns:
        str: Extracted text from the PDF file
    """
    text = ""
    with fitz.open(fp) as doc:
        for page in doc:
            text += page.get_text()

    return text
