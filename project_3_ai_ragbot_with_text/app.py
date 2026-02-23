from langchain_ollama import ChatOllama
import sys, os

# Robust path to find config.py in the project root
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import config

llm = ChatOllama(model=config.CHAT_MODEL, base_url=config.OLLAMA_BASE_URL)

# Basic RAG: Read local text file
txt_path = os.path.join(os.path.dirname(__file__), "profile-of-ruthran-raghavan.txt")
try:
    with open(txt_path, "r") as f:
        context = f.read()
except FileNotFoundError:
    context = "Knowledge base file not found."

def ragbot_text(message, history):
    prompt = f"Using this context:\n{context}\n\nQuestion: {message}"
    
    # Use .stream() for RAG streaming
    partial_text = ""
    for chunk in llm.stream([("system", config.SYSTEM_PROMPT), ("human", prompt)]):
        partial_text += chunk.content
        yield partial_text

if __name__ == "__main__":
    print("\n--- Caramel AI Project 3: Text RAG (Streaming) active ---")
    while True:
        try:
            user_input = input("\nYou (Ask about text): ")
            if user_input.lower() in ["exit", "quit", "bye"]: break
            if not user_input.strip(): continue

            print("Caramel AI: ", end="", flush=True)
            last_chars = 0
            for partial_text in ragbot_text(user_input, []):
                print(partial_text[last_chars:], end="", flush=True)
                last_chars = len(partial_text)
            print()
        except KeyboardInterrupt:
            break
