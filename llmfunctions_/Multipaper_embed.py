import os
import glob
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
folder_path = '/Users/luweitao/Documents/Projects/althea/llmfunctions_/' #This is where data is.
def read_api_key(api_path):
    with open(api_path, 'r') as file:
        return file.read().strip()
OPENAI_API_KEY = read_api_key('./API_Key/OPENAI_API_KEY.txt')
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
llm = OpenAI(temperature=0)
search_pattern = os.path.join(folder_path, '*.txt')

# Use glob.glob to find all files matching the search pattern
txt_files = glob.glob(search_pattern)

# Print the names of the PDF files
for txt_file in txt_files:
    #print(os.path.basename(pdf_file))
    print(txt_file)
    loader = TextLoader(txt_file)
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

qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=docsearch.as_retriever())
while True:
    query = input("Ask a question: ")
    print(qa.run(query))