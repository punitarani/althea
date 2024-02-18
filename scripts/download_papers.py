"""scripts/download_papers.py"""

import asyncio
import json

from tqdm import tqdm

from althea.openalex import Work
from althea.utils import safe_filename
from config import DATA_DIR

with open(f"{DATA_DIR}/network.json", "r") as f:
    WORKS = json.load(f).get("works", [])


async def map_work_id_to_doi(works: list[str]) -> dict[str, str]:
    """
    Map work IDs to DOIs

    Args:
        works (list[str]): List of work IDs

    Returns:
        dict[str, str]: Dictionary mapping work IDs to DOIs
    """

    work_doi = {}
    for work_id in tqdm(works, desc="Mapping"):
        work = await Work(work_id).data
        doi = work.doi

        # Check if the txt file exists
        if doi:
            if doi.startswith("https://doi.org/"):
                doi = doi[16:]
            if doi.startswith("http://doi.org/"):
                doi = doi[15:]
            elif doi.startswith("doi.org/"):
                doi = doi[8:]

            filename = safe_filename(doi) + ".txt"
            filepath = DATA_DIR.joinpath("txt", filename)
            if filepath.exists():
                work_doi[work_id] = doi

    return work_doi


if __name__ == "__main__":
    import asyncio

    print("Mapping work IDs to DOIs")
    work_dois = asyncio.run(map_work_id_to_doi(WORKS))

    print("Saving to file works.json")
    with open(f"{DATA_DIR}/works.json", "w") as f:
        json.dump(work_dois, f, indent=2)
