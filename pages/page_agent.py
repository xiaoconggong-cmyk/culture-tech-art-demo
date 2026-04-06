import gradio as gr
from modules.rag_engine.knowledge_base import CulturalIPKnowledgeBase
from modules.agent_framework.workflow_graph import BusinessAgentWorkflow
import os

kb = CulturalIPKnowledgeBase()
# 尝试加载已有知识库
try:
    kb.load_store("./cultural_ip_store")
except:
    pass

agent = BusinessAgentWorkflow(rag_engine=kb)

def generate_report(query):
    if not query.strip():
        return "请输入商业问题"
    try:
        report = agent.run(query)
        return report
    except Exception as e:
        return f"生成报告失败：{str(e)}"

def render():
    with gr.Blocks() as page:
        gr.Markdown("## 📈 智能商业决策")
        gr.Markdown("基于Agent框架实现商业逻辑自动化闭环")
        
        query_input = gr.Textbox(
            label="输入商业问题",
            placeholder="例如：如何将敦煌飞天IP开发成文旅产品？",
            lines=2
        )
        generate_btn = gr.Button("生成报告", variant="primary")
        output = gr.Markdown(label="商业决策报告")
        
        generate_btn.click(
            fn=generate_report,
            inputs=query_input,
            outputs=output
        )
        
        gr.Examples(
            examples=[
                ["如何将敦煌飞天IP开发成文旅产品？"],
                ["苏绣非遗如何商业化变现？"],
                ["昆曲如何吸引Z世代年轻人？"],
                ["故宫文创的成功经验如何复制？"]
            ],
            inputs=query_input
        )
    return page