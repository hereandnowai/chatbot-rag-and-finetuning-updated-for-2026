from langchain_ollama import ChatOllama
from bs4 import BeautifulSoup
import requests, sys, os, gradio as gr

# Robust path to find config.py in the project root
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import config

llm = ChatOllama(model=config.CHAT_MODEL, base_url=config.OLLAMA_BASE_URL)

# Web RAG
url = "https://ruthranraghavan.com"
soup = BeautifulSoup(requests.get(url).content, 'html.parser')
context = soup.body.get_text(separator=' ', strip=True)

def get_response(query, history):
    prompt = f"Context: {context}\n\nQuestion: {query}"
    return llm.invoke([("system", config.SYSTEM_PROMPT), ("human", prompt)]).content

if __name__ == "__main__":
    while True:
        user_input = input("You (Ask about the website): ")
        if user_input.lower() in ["exit", "quit", "bye"]: break
        print(f"Caramel AI: {get_response(user_input, [])}")