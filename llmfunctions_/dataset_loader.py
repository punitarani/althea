# This file is to embed pdf to vectors in KDBAIimport os
# Important to set the tag!!!
tag = "law"
import time
from getpass import getpass
import kdbai_client as kdbai
import pandas as pd
import requests
from langchain.chains import RetrievalQA
from langchain.document_loaders import PyPDFLoader
from langchain_community.vectorstores import KDBAI
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
import glob
import os

folder_path = '/Users/luweitao/Documents/Projects/TreehackAPI/' #This is where data is.
def read_api_key(api_path):
    with open(api_path, 'r') as file:
        return file.read().strip()

KDBAI_ENDPOINT = 'https://cloud.kdb.ai/instance/qpglwft3zm'
KDBAI_API_KEY = read_api_key('./API_Key/KDBAI_API_KEY.txt')    

OPENAI_API_KEY = read_api_key('./API_Key/OPENAI_API_KEY.txt')
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
os.environ["KDBAI_API_KEY"] = KDBAI_API_KEY


TEMP = 0.0 # temperature for LLMs
K = 3
print("Create a KDB.AI session...")
session = kdbai.Session(endpoint=KDBAI_ENDPOINT, api_key=KDBAI_API_KEY)
print('Create table "documents"...')
schema = {
    "columns": [
        {"name": "id", "pytype": "str"},
        {"name": "text", "pytype": "bytes"},
        {
            "name": "embeddings",
            "pytype": "float32",
            "vectorIndex": {"dims": 1536, "metric": "L2", "type": "hnsw"},
        },
        {"name": "tag", "pytype": "str"},
        {"name": "title", "pytype": "bytes"},
    ]
}
if 'documents' in session.list():
    session.table("documents").drop()
table = session.create_table("documents", schema)

# Set the path to the folder


# Construct the search pattern to match all PDF files
search_pattern = os.path.join(folder_path, '*.pdf')

# Use glob.glob to find all files matching the search pattern
pdf_files = glob.glob(search_pattern)

# Print the names of the PDF files
for pdf_file in pdf_files:
    #print(os.path.basename(pdf_file))
    PDF = f"{os.path.basename(pdf_file)}"

    print("Read a PDF...")
    
    loader = PyPDFLoader(os.path.join(folder_path, PDF))
    pages = loader.load_and_split()
    len(pages)
    print("Create a Vector Database from PDF text...")
    embeddings = OpenAIEmbeddings(model="text-embedding-ada-002")
    texts = [p.page_content for p in pages]
    metadata = pd.DataFrame(index=list(range(len(texts))))
    metadata["tag"] = tag
    metadata["title"] = f"{PDF[:-3]}".encode(
        "utf-8"
    )
    vectordb = KDBAI(table, embeddings)
    vectordb.add_texts(texts=texts, metadatas=metadata)