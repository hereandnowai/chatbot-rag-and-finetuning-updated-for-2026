from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage
import base64, sys, os

# Robust path to find config.py in the project root
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import config

llm = ChatOllama(model=config.VISION_MODEL, base_url=config.OLLAMA_BASE_URL)

def get_image_description(image_path):
    if not image_path:
        yield "Please upload an image."
        return
    
    with open(image_path, "rb") as f:
        img_b64 = base64.b64encode(f.read()).decode("utf-8")
    
    msg = HumanMessage(content=[
        {"type": "text", "text": "Describe this image."},
        {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{img_b64}"}}
    ])
    
    # Use .stream() for Vision streaming
    partial_text = ""
    for chunk in llm.stream([("system", config.SYSTEM_PROMPT), msg]):
        partial_text += chunk.content
        yield partial_text

if __name__ == "__main__":
    import signal, sys
    def handler(signum, frame): sys.exit(0)
    signal.signal(signal.SIGINT, handler)
    print("\n--- Caramel AI Project 8: Vision (Streaming) active ---")
    while True:
        try:
            path = input("\nEnter image path (or 'exit'): ")
            if path.lower() in ["exit", "quit"]: break
            if not os.path.exists(path):
                print("File not found.")
                continue

            print("Caramel AI: ", end="", flush=True)
            last_chars = 0
            for partial_text in get_image_description(path):
                print(partial_text[last_chars:], end="", flush=True)
                last_chars = len(partial_text)
            print()
        except KeyboardInterrupt:
            break
