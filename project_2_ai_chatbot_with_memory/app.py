from langchain_ollama import ChatOllama
import sys, os

# Robust path to find config.py in the project root
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import config

llm = ChatOllama(model=config.CHAT_MODEL, base_url=config.OLLAMA_BASE_URL)

def ai_chatbot(message, history):
    # 'history' for Gradio 6 is a list of [user, ai] message pairs or specialized objects. 
    # For simplicity in this teaching project, we convert standard historical interaction.
    chat_history = [("system", config.SYSTEM_PROMPT)]
    for user_msg, ai_msg in history:
        chat_history.append(("human", user_msg))
        chat_history.append(("ai", ai_msg))
    
    chat_history.append(("human", message))
    return llm.invoke(chat_history).content

if __name__ == "__main__":
    print(ai_chatbot("Hi! I'm learning AI.", []))