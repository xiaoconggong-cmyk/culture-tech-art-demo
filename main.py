import os
# 设置 Gradio 临时目录为短路径，避免 Windows 路径过长错误
os.environ["GRADIO_TEMP_DIR"] = r"D:\gradio_temp"
# 确保目录存在
if not os.path.exists(r"D:\gradio_temp"):
    os.makedirs(r"D:\gradio_temp")

import gradio as gr
from pages import page_aigc, page_rag, page_agent
from dotenv import load_dotenv

load_dotenv()

with gr.Blocks(title="文化+科技+艺术融合Demo", theme=gr.themes.Soft()) as demo:
    gr.Markdown("# 🎨 GXC · 文化科技实验室")
    gr.Markdown("### AI与文化IP深度融合的三模块演示")
    
    with gr.Tabs():
        with gr.TabItem("⚙️ AIGC管线"):
            page_aigc.render()
        with gr.TabItem("🧬 RAG文化基因库"):
            page_rag.render()
        with gr.TabItem("📈 智能商业决策"):
            page_agent.render()

if __name__ == "__main__":
    demo.launch(share=True)