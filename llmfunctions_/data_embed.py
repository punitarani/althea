import os
from langchain import OpenAI

# The vectorstore we'll be using
from langchain.vectorstores import FAISS

# The LangChain component we'll use to get the documents
from langchain.chains import RetrievalQA
# The easy document loader for text
from langchain.document_loaders import TextLoader
# The embedding engine that will convert our text to vectors
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter

def read_api_key(api_path):
    with open(api_path, 'r') as file:
        return file.read().strip()
OPENAI_API_KEY = read_api_key('./API_Key/OPENAI_API_KEY.txt')
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
loader = TextLoader('/Users/luweitao/Documents/Projects/althea/llmfunctions_/10_1002_0471250953_bi0506s15.txt')
doc = loader.load()
print (f"You have {len(doc)} document")
print (f"You have {len(doc[0].page_content)} characters in that document")
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=400)
docs = text_splitter.split_documents(doc)
# Get the total number of characters so we can see the average later
num_total_characters = sum([len(x.page_content) for x in docs])

print (f"Now you have {len(docs)} documents that have an average of {num_total_characters / len(docs):,.0f} characters (smaller pieces)")

# Get your embeddings engine ready
embeddings = OpenAIEmbeddings()

# Embed your documents and combine with the raw text in a pseudo db. Note: This will make an API call to OpenAI
docsearch = FAISS.from_documents(docs, embeddings)
my_dict = docsearch.docstore._dict

count = 0
for key, value in my_dict.items():
    print(key, ':', value)
    count += 1
    if count == 5:
        break ##print the first 5 embedding

print("Document embedding is done",docsearch)


qabot = RetrievalQA.from_chain_type(
    chain_type="stuff",
    llm=OpenAI(temperature=0),
    retriever=docsearch.as_retriever(),
    return_source_documents=True,
)

def query(Input_Q,qabot):
    #check if the question is related(filter)
    Q = f"Is {Input_Q} relevant to any of the documents in your database?response 1 if yes else 0."
    
    if(qabot.invoke(dict(query=Q))["result"]=='0'):
        
        return "This question is not related to any domain in our paper database." 
    else:
        return qabot.invoke(dict(query=Input_Q))["result"]#return 0 if not related
        

#     #if not, return 0
# while True:
#     question = input("Ask a question: ")
#     answer = query(question,qabot)
#     print(answer)
