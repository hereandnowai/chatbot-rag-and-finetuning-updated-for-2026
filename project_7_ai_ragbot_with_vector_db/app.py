from langchain_ollama import ChatOllama, OllamaEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import CharacterTextSplitter
import os, sys

# Robust path to find config.py in the project root
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import config

llm = ChatOllama(model=config.CHAT_MODEL, base_url=config.OLLAMA_BASE_URL)
embeddings = OllamaEmbeddings(model=config.EMBEDDING_MODEL, base_url=config.OLLAMA_BASE_URL)

# Setup Vector DB - Use local file from root
print("🔍 Loading & Indexing PDF knowledge...")
pdf_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'profile-of-ruthran-raghavan-chief-ai-scientist-here-and-now-ai.pdf'))
loader = PyPDFLoader(pdf_path)
docs = CharacterTextSplitter(chunk_size=500, chunk_overlap=50).split_documents(loader.load())
vectorstore = FAISS.from_documents(docs, embeddings)
print("✅ Knowledge Base Ready!")

def get_response(query, history):
    # Perform similarity search
    results = vectorstore.similarity_search(query, k=2)
    # Extract only the text content from documents
    context = "\n".join([doc.page_content for doc in results])
    
    prompt = f"Using this context:\n{context}\n\nQuestion: {query}"
    return llm.invoke([("system", config.SYSTEM_PROMPT), ("human", prompt)]).content

if __name__ == "__main__":
    print("\n--- Caramel AI Project 7: Vector search is active! ---")
    while True:
        try:
            user_input = input("You: ")
            if user_input.lower() in ["exit", "quit", "bye"]: break
            if not user_input.strip(): continue
            
            print("Caramel AI thinking...")
            print(f"Caramel AI: {get_response(user_input, [])}")
        except KeyboardInterrupt:
            print("\nShutting down...")
            break
