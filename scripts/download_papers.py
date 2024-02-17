"""scripts/download_papers.py"""

import asyncio
import json

from althea.network import download_papers
from config import PROJECT_PATH

with open(f"{PROJECT_PATH}/data/network.json", "r") as f:
    WORKS = json.load(f).get("works", [])

print(f"Downloading {len(WORKS)} papers")
downloaded = asyncio.run(download_papers(works=WORKS))
