import gradio as gr
from app import search_chatbot
import json, os

# Load branding
with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'branding.json'))) as f:
    brand_info = json.load(f)['brand']

with gr.Blocks(title=f"Search - {brand_info['organizationName']}") as demo:
    gr.HTML(f'''<div style="display: flex; justify-content: center; margin-bottom: 20px;">
            <img src="{brand_info['logo']['title']}" alt="Logo" style="height: 100px;">
        </div>''')
    
    gr.ChatInterface(
        fn=search_chatbot,
        chatbot=gr.Chatbot(height=500, avatar_images=(None, brand_info['chatbot']['avatar'])),
        title="Caramel AI: Internet Search Mode",
        description="I can now search the real-time internet to answer questions about news, weather, or current events!",
        examples=["What is the latest news in AI today?", "What is the weather in Chennai right now?", "Who won the latest cricket match?"]
    )

if __name__ == "__main__":
    import signal, sys
    def handler(signum, frame): sys.exit(0)
    signal.signal(signal.SIGINT, handler)
    demo.launch()
