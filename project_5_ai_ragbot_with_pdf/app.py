from langchain_ollama import ChatOllama
from pypdf import PdfReader
import requests, sys, os, gradio as gr

# Robust path to find config.py in the project root
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import config

llm = ChatOllama(model=config.CHAT_MODEL, base_url=config.OLLAMA_BASE_URL)

# PDF RAG - Use local file from root
pdf_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'profile-of-ruthran-raghavan-chief-ai-scientist-here-and-now-ai.pdf'))
reader = PdfReader(pdf_path)
context = " ".join([page.extract_text() for page in reader.pages])

def get_response(msg, history):
    return llm.invoke([("system", config.SYSTEM_PROMPT), ("human", f"Context: {context}\n\nQuestion: {msg}")]).content

if __name__ == "__main__":
    while True:
        user_input = input("You (Ask about the PDF): ")
        if user_input.lower() in ["exit", "quit", "bye"]: break
        print(f"Caramel AI: {get_response(user_input, [])}")
