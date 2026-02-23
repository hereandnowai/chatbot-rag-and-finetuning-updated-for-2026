from langchain_ollama import ChatOllama
import sys, os

# Robust path to find config.py in the project root
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import config

# Setup Caramel AI
llm = ChatOllama(model=config.CHAT_MODEL,
                 base_url=config.OLLAMA_BASE_URL)

def ai_chatbot(message, history):
    # Send system prompt and user message to the local model
    response = llm.invoke([("system", config.SYSTEM_PROMPT), ("human", message)])
    return response.content

if __name__ == "__main__":
    print(ai_chatbot("What is AI?", []))