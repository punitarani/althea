import os
import kdbai_client as kdbai
from langchain.chains import RetrievalQA
from langchain.document_loaders import PyPDFLoader
from langchain_community.vectorstores import KDBAI
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
TEMP = 0.0 # temperature for LLMs
K = 3
API_path = '/Users/luweitao/Documents/Projects/API_Key/'
folder_path = '/Users/luweitao/Documents/Projects/TreehackAPI/' #This is where data is.
def read_api_key(api_path):
    with open(api_path, 'r') as file:
        return file.read().strip()

KDBAI_ENDPOINT = 'https://cloud.kdb.ai/instance/qpglwft3zm'
KDBAI_API_KEY = read_api_key(os.path.join(API_path, 'KDBAI_API_KEY.txt'))     
OPENAI_API_KEY = read_api_key(os.path.join(API_path, 'OPENAI_API_KEY.txt'))  
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
os.environ["KDBAI_API_KEY"] = KDBAI_API_KEY 
session = kdbai.Session(endpoint=KDBAI_ENDPOINT, api_key=KDBAI_API_KEY)
embeddings = OpenAIEmbeddings(model="text-embedding-ada-002")

vectordb =  KDBAI(session.table("documents"), embeddings)
print("Create LangChain Pipeline...")
qabot = RetrievalQA.from_chain_type(
    chain_type="stuff",
    llm=ChatOpenAI(model="gpt-3.5-turbo-16k", temperature=TEMP),
    retriever=vectordb.as_retriever(search_kwargs=dict(k=K)),
    return_source_documents=True,
)
def query(Input_Q):
    #check if the question is related(filter)
    Q = f"Is {Input_Q} relevant to any of the documents or related to asking the database information in your database?response 1 if yes else 0."
    
    if(qabot.invoke(dict(query=Q))["result"]=='#'):
        
        return "This question is not related to any domain in our paper database." 
    else:
        return qabot.invoke(dict(query=Input_Q))["result"]#return 0 if not related
        

    #if not, return 0

while True:
    print("Please input your question:")
    question = input()
    print(query(question))
    print("Do you have another question? (yes or no)")
    if input().lower() != 'yes':
        break
