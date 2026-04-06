# 🎨 文化IP智能创作与决策系统

**文化 + 科技 + 艺术深度融合 Demo**  
视袭&君看 · 文化科技实验室 技术预研项目

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](https://python.org)
[![Gradio](https://img.shields.io/badge/Gradio-6.10%2B-orange)](https://gradio.app)
[![LangChain](https://img.shields.io/badge/LangChain-0.3%2B-green)](https://langchain.com)

---

## 📌 项目简介

本项目针对“文化IP的智能化创作与商业决策”场景，构建了一套融合 **AIGC管线**、**RAG知识库** 与 **Agent商业决策** 的完整 Demo。核心目标是将“视袭&君看”十年文化 IP 基因注入 AI 系统，实现从创意生成到商业落地的自动化闭环。

## 🚀 核心功能

### ⚙️ AIGC 自动化管线
- 基于 ComfyUI + FLUX.1 模型 + 敦煌/国风 LoRA 实现高质量图像生成
- 支持“敦煌飞天”“苏绣”“昆曲”等文化 IP 定制化提示词（传统/现代/融合三种风格）
- 提供模拟生成模式（无 ComfyUI 环境时自动降级）

### 🧬 RAG 文化基因库
- 使用 LangChain + HuggingFace Embeddings + FAISS 向量化 10 年文化 IP 文本
- 语义检索并自动注入 **“视袭&君看·文化基因片段”** 标记
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