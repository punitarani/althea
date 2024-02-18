import asyncio

from althea.network import build_network_around_work
from althea.openalex.utils import doi_to_entity_id

DOI = "https://doi.org/10.3390/life13122281"

EID = doi_to_entity_id(doi=DOI)
print(f"Building network for work: {EID}")

res = asyncio.run(
    build_network_around_work(
        entity_id=EID, depth=3, citations_limit=10, references_limit=10
    )
)
print(res)
