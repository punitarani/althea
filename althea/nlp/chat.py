"""althea/nlp/chat.py"""

from langchain.chains import RetrievalQA
from langchain_community.chat_models import ChatCohere

from althea.nlp.base import vectorstore

retriever = vectorstore.as_retriever(k=5)

chatbot = RetrievalQA.from_chain_type(
    chain_type="stuff",
    llm=ChatCohere(temperature=0.25),
    retriever=vectorstore.as_retriever(search_kwargs=dict(k=10)),
    return_source_documents=True,
)


def chat_answer(question: str) -> str:
    """Answer a question using the chatbot."""
    return chatbot.invoke(input=dict(query=question))["result"]
