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
    print("\n--- Caramel AI Project 1: Streaming mode ---")
    while True:
        try:
            user_input = input("\nYou: ")
            if user_input.lower() in ["exit", "quit", "bye"]: break
            if not user_input.strip(): continue
            
            print("Caramel AI: ", end="", flush=True)
            last_length = 0
            for partial_text in ai_chatbot(user_input, []):
                print(partial_text[last_length:], end="", flush=True)
                last_length = len(partial_text)
            print()
        except KeyboardInterrupt:
            break