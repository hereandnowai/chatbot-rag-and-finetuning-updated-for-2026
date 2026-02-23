from langchain_ollama import ChatOllama
import requests, sys, os

# Robust path to find config.py in the project root
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import config

llm = ChatOllama(model=config.CHAT_MODEL, base_url=config.OLLAMA_BASE_URL)

# Basic RAG: Read local text file
txt_path = os.path.join(os.path.dirname(__file__), "profile-of-ruthran-raghavan.txt")
with open(txt_path, "r") as f:
    context = f.read()

def ragbot_text(message, history):
    prompt = f"Context: {context}\n\nQuestion: {message}"
    return llm.invoke([("system", config.SYSTEM_PROMPT), ("human", prompt)]).content

if __name__ == "__main__":
    while True:
        user_input = input("You (Ask about the context): ")
        if user_input.lower() in ["exit", "quit", "bye"]: break
        print(f"Caramel AI: {ragbot_text(user_input, [])}")