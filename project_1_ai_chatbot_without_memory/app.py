from langchain_ollama import ChatOllama
import sys, os

# Robust path to find config.py in the project root
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import config

# Setup Caramel AI
llm = ChatOllama(model=config.CHAT_MODEL,
                 base_url=config.OLLAMA_BASE_URL)

def ai_chatbot(message, history):
    # Use .stream() for word-by-word streaming
    stream = llm.stream([("system", config.SYSTEM_PROMPT), ("human", message)])
    partial_text = ""
    for chunk in stream:
        partial_text += chunk.content
        yield partial_text

if __name__ == "__main__":
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in ["exit", "quit", "bye"]: break
        print(f"\nCaramel AI: {ai_chatbot(user_input, [])}")