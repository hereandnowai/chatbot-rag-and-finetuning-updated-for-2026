from langchain_ollama import ChatOllama
from langchain_community.tools.tavily_search import TavilySearchResults
import sys, os

# Robust path to find config.py in the project root
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import config

# Set API Key for the session
os.environ["TAVILY_API_KEY"] = config.TAVILY_API_KEY

# Setup Caramel AI
llm = ChatOllama(model=config.CHAT_MODEL, base_url=config.OLLAMA_BASE_URL)

# Setup Search Tool
search = TavilySearchResults(k=3)

def search_chatbot(message, history):
    # Step 1: Search the internet
    print(f"🔍 Caramel AI is searching for: {message}")
    search_results = search.run(message)
    
    # Step 2: Combine results into context
    context = "\n".join([res['content'] for res in search_results])
    
    # Step 3: Stream the response with internet context
    prompt = f"Using this fresh internet data:\n{context}\n\nQuestion: {message}"
    
    partial_text = ""
    for chunk in llm.stream([("system", config.SYSTEM_PROMPT), ("human", prompt)]):
        partial_text += chunk.content
        yield partial_text

if __name__ == "__main__":
    print("\n--- Caramel AI Project 6: Tavily Search active ---")
    while True:
        try:
            user_input = input("\nYou (Ask anything about the world): ")
            if user_input.lower() in ["exit", "quit", "bye"]: break
            if not user_input.strip(): continue
            
            print("Caramel AI: ", end="", flush=True)
            last_length = 0
            for partial_text in search_chatbot(user_input, []):
                print(partial_text[last_length:], end="", flush=True)
                last_length = len(partial_text)
            print()
        except KeyboardInterrupt:
            break
