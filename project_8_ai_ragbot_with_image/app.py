from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage
import base64, sys, os, gradio as gr

# Robust path to find config.py in the project root
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import config

llm = ChatOllama(model=config.VISION_MODEL, base_url=config.OLLAMA_BASE_URL)

def get_image_description(image_path):
    if not image_path: return "Please upload an image."
    
    with open(image_path, "rb") as f:
        img_b64 = base64.b64encode(f.read()).decode("utf-8")
    
    msg = HumanMessage(content=[
        {"type": "text", "text": "Describe this image."},
        {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{img_b64}"}}
    ])
    # Apply global system prompt
    return llm.invoke([("system", config.SYSTEM_PROMPT), msg]).content

if __name__ == "__main__":
    gr.Interface(
        fn=get_image_description,
        inputs=gr.Image(type="filepath", label="Upload Image"),
        outputs=gr.Textbox(label="Image Description"),
        title="AI Image Describer",
        description="Upload an image and the AI will describe it for you.",
    ).launch(theme="default")
