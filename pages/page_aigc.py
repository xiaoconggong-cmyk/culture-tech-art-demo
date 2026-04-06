import gradio as gr
from modules.aigc_pipeline.comfyui_client import ComfyUIClient

client = ComfyUIClient()

def generate(ip_element, style):
    if not ip_element.strip():
        return "请输入文化IP元素", None
    img = client.generate_with_cultural_style(ip_element, style)
    return f"生成成功！风格：{style}", img

def render():
    with gr.Blocks() as page:
        gr.Markdown("## ⚙️ AIGC自动化管线")
        gr.Markdown("基于ComfyUI的AI图像生成管线，注入文化IP基因")
        
        with gr.Row():
            with gr.Column():
                ip_input = gr.Textbox(label="文化IP元素", placeholder="例如：敦煌飞天、苏绣、昆曲...")
                style_radio = gr.Radio(
                    choices=["traditional", "modern", "fusion"],
                    label="艺术风格",
                    value="traditional",
                    info="traditional: 传统水墨 | modern: 赛博朋克 | fusion: 东西融合"
                )
                generate_btn = gr.Button("生成图像", variant="primary")
                status = gr.Textbox(label="状态", interactive=False)
            with gr.Column():
                output_image = gr.Image(label="生成结果", type="pil")
        
        generate_btn.click(
            fn=generate,
            inputs=[ip_input, style_radio],
            outputs=[status, output_image]
        )
        
        gr.Examples(
            examples=[
                ["敦煌飞天", "traditional"],
                ["苏绣", "modern"],
                ["昆曲牡丹亭", "fusion"]
            ],
            inputs=[ip_input, style_radio]
        )
    return page