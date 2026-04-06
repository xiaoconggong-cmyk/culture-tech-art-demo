# 🎨 文化IP智能创作与决策系统

**文化 + 科技 + 艺术深度融合 Demo**  

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](https://python.org)
[![Gradio](https://img.shields.io/badge/Gradio-6.10%2B-orange)](https://gradio.app)
[![LangChain](https://img.shields.io/badge/LangChain-0.3%2B-green)](https://langchain.com)

---

## 📌 项目简介

本项目针对“文化IP的智能化创作与商业决策”场景，构建了一套融合 **AIGC管线**、**RAG知识库** 与 **Agent商业决策** 的完整 Demo。核心目标是将“GXC”十年文化 IP 基因注入 AI 系统，实现从创意生成到商业落地的自动化闭环。

## 🚀 核心功能

### ⚙️ AIGC 自动化管线
- 基于 ComfyUI + FLUX.1 模型 + 敦煌/国风 LoRA 实现高质量图像生成
- 支持“敦煌飞天”“苏绣”“昆曲”等文化 IP 定制化提示词（传统/现代/融合三种风格）
- 提供模拟生成模式（无 ComfyUI 环境时自动降级）

### 🧬 RAG 文化基因库
- 使用 LangChain + HuggingFace Embeddings + FAISS 向量化 10 年文化 IP 文本
- 语义检索并自动注入 **“GXC·文化基因片段”** 标记
- 内置示例数据（非遗、敦煌、故宫、茶马古道等），支持上传自定义文档

### 📈 Agent 智能商业决策
- 基于 LangChain + 硅基流动大模型（DeepSeek-V3）构建多链 Agent
- 自动完成：商业策略分析 → 预算估算 → 营销方案生成
- 实现从文化 IP 到商业落地的闭环决策

## 🛠️ 技术栈

| 模块 | 技术 |
|------|------|
| AIGC 管线 | ComfyUI, FLUX.1, LoRA, PIL |
| RAG 知识库 | LangChain, FAISS, HuggingFace Embeddings |
| Agent 框架 | LangChain, ChatOpenAI (兼容硅基流动 API) |
| 前端界面 | Gradio 6.10 |
| 语言 | Python 3.10+ |

## 📦 快速开始

### 1. 克隆仓库
```bash
git clone https://github.com/xiaoconggong-cmyk/culture-tech-art-demo.git
cd culture-tech-art-demo
2. 创建虚拟环境并安装依赖
bash
python -m venv venv
source venv/bin/activate      # Linux/Mac
venv\Scripts\activate          # Windows
pip install -r requirements.txt
3. 配置 API 密钥（用于 Agent 模块）
复制 .env.example 为 .env，填入你的硅基流动 API 密钥：

text
OPENAI_API_KEY=sk-xxxxxx
OPENAI_BASE_URL=https://api.siliconflow.cn/v1
LLM_MODEL=Qwen/Qwen2.5-7B-Instruct
4. 启动 ComfyUI（可选，用于 AIGC 真实生成）
下载 ComfyUI 并启动

将本项目中的 modules/aigc_pipeline/workflow.json 导入 ComfyUI 并导出为 API 格式

确保 FLUX.1 模型与 LoRA 放置在正确目录

5. 运行 Demo
bash
python main.py
浏览器打开 http://127.0.0.1:7860 即可体验三模块功能。

🎯 使用示例
AIGC 管线
输入：敦煌飞天，选择风格 traditional

输出：生成敦煌风格的水墨/壁画质感图像

RAG 知识库
点击“使用示例数据”构建向量库

提问：苏绣有哪些创新技法？

回答：检索相关文化片段并带基因标记

Agent 决策
提问：如何将敦煌飞天IP开发成文旅产品？

输出：包含商业策略、预算估算、营销方案的完整报告

🔮 我的“疯狂观察”
AI 将催生“元文化”——文化 IP 不再是静态符号库，而是可自我进化的活态基因池。文化公司的角色从“守护者”变为“宇宙园丁”，设计初始规则让 AI 与人类共创无限衍生的文化生态。

📄 许可证
MIT

📧 联系
GXC - 2512497105@qq.com
GitHub: xiaoconggong-cmyk
