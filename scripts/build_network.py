import asyncio

from althea.network import build_network_around_work
from althea.openalex.utils import doi_to_entity_id

DOI = "10.1042/CS20230586"

EID = doi_to_entity_id(doi=DOI)
print(f"Building network for work: {EID}")

res = asyncio.run(build_network_around_work(entity_id=EID))

print(res)
