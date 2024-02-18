import os
from langchain import OpenAI

# The vectorstore we'll be using
from langchain.vectorstores import FAISS

# The LangChain component we'll use to get the documents
from langchain.chains import RetrievalQA
# The easy document loader for text
from langchain.document_loaders import TextLoader
# The embedding engine that will convert our text to vectors
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter

def read_api_key(api_path):
    with open(api_path, 'r') as file:
        return file.read().strip()
OPENAI_API_KEY = read_api_key('./API_Key/OPENAI_API_KEY.txt')
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

def embedding_txt(txt):
  
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=400)
    
    docs = text_splitter.split_documents(txt)
    
    embeddings = OpenAIEmbeddings()
    
    embedded_txt = FAISS.from_documents(docs, embeddings)#Use FAISS to accelerate the search

    return embedded_txt

def QA(embedded_txt,question,qabot):
    qabot = RetrievalQA.from_chain_type(
    chain_type="stuff",
    llm=ChatOpenAI(model="gpt-3.5-turbo-16k", temperature=0),
    retriever=embedded_txt.as_retriever(search_kwargs=dict(k=K)),
    return_source_documents=True,
)
    return qabot.invoke(dict(query=question))["result"]#return 0 if not related

