"""scripts/map_work_id_doi.py"""

import json

from althea.openalex.work import Work
from config import DATA_DIR

with open(f"{DATA_DIR}/network.json", "r") as f:
    WORKS = json.load(f).get("works", [])


work_doi = {}

for work_id in WORKS:
    work = Work(work_id)
    work_doi[work_id] = work.doi
