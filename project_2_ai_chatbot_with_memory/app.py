from langchain_ollama import ChatOllama
import sys, os

# Robust path to find config.py in the project root
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import config

llm = ChatOllama(model=config.CHAT_MODEL, base_url=config.OLLAMA_BASE_URL)

def ai_chatbot(message, history):
    # Handle Gradio 6 history (list of dicts) vs terminal history (list of pairs)
    chat_history = [("system", config.SYSTEM_PROMPT)]
    for item in history:
        if isinstance(item, dict):
            role = "human" if item["role"] == "user" else "ai"
            chat_history.append((role, item["content"]))
        else:
            user_msg, ai_msg = item
            chat_history.append(("human", user_msg))
            chat_history.append(("ai", ai_msg))
    
    chat_history.append(("human", message))
    
    # Use .stream() for memory-aware streaming
    stream = llm.stream(chat_history)
    partial_text = ""
    for chunk in stream:
        partial_text += chunk.content
        yield partial_text

if __name__ == "__main__":
    chat_history_state = []
    print("\n--- Caramel AI Project 2: Memory & Streaming mode ---")
    while True:
        try:
            user_input = input("\nYou: ")
            if user_input.lower() in ["exit", "quit", "bye"]: break
            if not user_input.strip(): continue

            print("Caramel AI: ", end="", flush=True)
            full_response = ""
            last_chars = 0
            for partial_text in ai_chatbot(user_input, chat_history_state):
                print(partial_text[last_chars:], end="", flush=True)
                full_response = partial_text
                last_chars = len(partial_text)
            print()
            chat_history_state.append((user_input, full_response))
        except KeyboardInterrupt:
            break