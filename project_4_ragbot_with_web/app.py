from langchain_ollama import ChatOllama
from bs4 import BeautifulSoup
import requests, sys, os

# Robust path to find config.py in the project root
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import config

llm = ChatOllama(model=config.CHAT_MODEL, base_url=config.OLLAMA_BASE_URL)

# Web RAG
url = "https://ruthranraghavan.com"
try:
    soup = BeautifulSoup(requests.get(url).content, "html.parser")
    context = soup.body.get_text(separator=" ", strip=True)
except:
    context = "Website could not be reached."

def get_response(query, history):
    prompt = f"Using this context:\n{context}\n\nQuestion: {query}"
    
    # Use .stream() for Web RAG streaming
    partial_text = ""
    for chunk in llm.stream([("system", config.SYSTEM_PROMPT), ("human", prompt)]):
        partial_text += chunk.content
        yield partial_text

if __name__ == "__main__":
    import signal, sys
    def handler(signum, frame): sys.exit(0)
    signal.signal(signal.SIGINT, handler)
    print("\n--- Caramel AI Project 4: Web RAG (Streaming) active ---")
    while True:
        try:
            user_input = input("\nYou (Ask about website): ")
            if user_input.lower() in ["exit", "quit", "bye"]: break
            if not user_input.strip(): continue

            print("Caramel AI: ", end="", flush=True)
            last_chars = 0
            for partial_text in get_response(user_input, []):
                print(partial_text[last_chars:], end="", flush=True)
                last_chars = len(partial_text)
            print()
        except KeyboardInterrupt:
            break
