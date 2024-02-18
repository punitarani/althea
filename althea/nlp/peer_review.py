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

controvesal_score = 0
duplicate_score = 0

def read_api_key(api_path):
    with open(api_path, 'r') as file:
        return file.read().strip()
OPENAI_API_KEY = read_api_key('../API_Key/OPENAI_API_KEY.txt')
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
#Set up a reference dataset, only use 1 doc here, can use more
loader = TextLoader('/Users/luweitao/Documents/Projects/althea/althea/dataset/txt/10_1002_anie_201206749.txt')
doc = loader.load()
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=400)
docs = text_splitter.split_documents(doc)
embeddings = OpenAIEmbeddings()

# Embed your documents and combine with the raw text in a pseudo db. Note: This will make an API call to OpenAI
docsearch = FAISS.from_documents(docs, embeddings)
my_dict = docsearch.docstore._dict

qabot = RetrievalQA.from_chain_type(
    chain_type="stuff",
    llm=OpenAI(temperature=0),
    retriever=docsearch.as_retriever(),
    return_source_documents=True,
)

def check_chunk(chunk,qabot):
    #check if the question is related(filter)
    Input_Q = f'''Is {chunk} similar to any of the "chunk" in your database? Grade in this format: 1: if similar and 
    have same conclusion. -1 if similar and have controversal conclusion. 0 if not similar at all. Response in this format:
    1:the similar "chunk" example in your database. -1:the similar "chunk" example in your database.0:N/A'''
    return qabot.invoke(dict(query=Input_Q))["result"]#return 0 if not related

#how to use:
# Input a chunk
test_chunk = dict(docs[8])['page_content']
print(test_chunk)
print(check_chunk(test_chunk,qabot))
wrong_chunk ='''In a stunning turn of events, scientists have discovered that the art of graffiti tagging has taken a microscopic turn, with D-enantiomers becoming the spray cans of the cellular world. These tiny molecular artists, known as FDAAs, have shown a rebellious streak, choosing to paint only the living cells' walls, shunning the inanimate peptidoglycan (PG) canvas as if it were unworthy of their vibrant hues (as seen in the avant-garde exhibit, Figure S4).

In a dramatic plot twist, these microscopic Picassos have also turned their noses up at the teichoic acid neighborhoods, keeping their street art exclusive to the peptidoglycan district. This was evidenced by a lackluster performance in the B. subtilis metropolis, where even the ΔdltA mutants, known for their plain, unadorned teichoic acids, failed to attract the colorful flair of the FDAAs (critics rave about Figures S5a–b for this unexpected snub).

The sacculi district showcased the enduring nature of their work, with graffiti that wouldn't wash away, proving the bond between FDAA paint and PG canvas was not just a summer fling but a covalent commitment (applause for Figures 1 and S3a, lower panels). The chromatographic streets of HPLC town confirmed that only a select few muropeptides were deemed worthy of this exclusive FDAA tag, ranging from a modest 0.2% to a slightly more flamboyant 2.8% (Figures 2a–c, S6, and S7 standing ovations). This selective tagging strategy ensures the cellular city remains vibrant but not overwhelmed, maintaining the delicate balance between artistic freedom and the structural integrity of the cell.

In conclusion, this microscopic tagging saga reveals an intricate dance of specificity, exclusivity, and covalent bonding, proving that even at the smallest scales, the desire to leave one's mark on the world is a universal impulse. The FDAA crew, with their discerning taste and commitment to viable cellular canvases, have set a new standard in the world of molecular graffiti.'''
print(check_chunk(wrong_chunk,qabot))


    

