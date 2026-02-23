from langchain_ollama import ChatOllama, OllamaEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
import requests, os, sys, gradio as gr

# Robust path to find config.py in the project root
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import config

llm = ChatOllama(model=config.CHAT_MODEL, base_url=config.OLLAMA_BASE_URL)
embeddings = OllamaEmbeddings(model=config.EMBEDDING_MODEL, base_url=config.OLLAMA_BASE_URL)

# Setup Vector DB - Use local file from root
pdf_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'profile-of-ruthran-raghavan-chief-ai-scientist-here-and-now-ai.pdf'))
loader = PyPDFLoader(pdf_path)
docs = CharacterTextSplitter(chunk_size=500, chunk_overlap=50).split_documents(loader.load())
vectorstore = FAISS.from_documents(docs, embeddings)

def get_response(query, history):
    context = vectorstore.similarity_search(query, k=2)
    prompt = f"Context: {context}\n\nQuestion: {query}"
    return llm.invoke([("system", config.SYSTEM_PROMPT), ("human", prompt)]).content

if __name__ == "__main__":
    while True:
        user_input = input("You (Ask Search Query): ")
        if user_input.lower() in ["exit", "quit", "bye"]: break
        print(f"Caramel AI: {get_response(user_input, [])}")
