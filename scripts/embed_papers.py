import asyncio
import json

from tqdm.asyncio import tqdm

from althea.nlp.embed import chunk_text_into_documents
from althea.openalex import Work
from althea.openalex.utils import parse_id_from_url
from althea.store.vector import pc
from althea.utils import safe_filename
from config import DATA_DIR

papers_index = pc.Index("papers")

with open(DATA_DIR.joinpath("works.json")) as f:
    WORKS_MAP = json.load(f)
    WORKS = list(WORKS_MAP.keys())


# async def main():
#     for work_id in tqdm(WORKS, desc="Embedding papers"):
#         eid = parse_id_from_url(work_id)
#
#         try:
#             work = await Work(work_id).data
#
#             with open(DATA_DIR.joinpath("txt", f"{safe_filename(WORKS_MAP.get(work.id))}.txt"), encoding="utf-8") as f:
#                 text = f.read()
#
#             docs = await chunk_text_into_documents(text, eid, work.title)
#             vecs = [doc.dict() for doc in docs]
#             papers_index.upsert(vecs)
#             print(work.id, "embedded")
#
#         except Exception as e:
#             print(f"Error embedding {work_id}: {e}")


async def fetch_and_process_work(work_id):
    eid = parse_id_from_url(work_id)
    try:
        work = await Work(work_id).data
        filepath = DATA_DIR.joinpath(
            "txt", f"{safe_filename(WORKS_MAP.get(work.id))}.txt"
        )
        with open(filepath, mode="r", encoding="utf-8") as f:
            text = f.read()

        docs = await chunk_text_into_documents(text, eid, work.title)
        vecs = [doc.dict() for doc in docs]
        papers_index.upsert(vecs)
        return work.id, "embedded"
    except Exception as e:
        return work_id, f"Error embedding {work_id}: {e}"


async def main():
    chunks = [WORKS[i : i + 10] for i in range(0, len(WORKS), 10)]
    for chunk in tqdm(chunks, desc="Processing chunks"):
        results = await asyncio.gather(
            *[fetch_and_process_work(work_id) for work_id in chunk]
        )
        for work_id, message in results:
            print(message)


if __name__ == "__main__":
    asyncio.run(main())
