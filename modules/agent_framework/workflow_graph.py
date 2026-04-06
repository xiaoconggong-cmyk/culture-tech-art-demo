import os
import traceback
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from modules.rag_engine.knowledge_base import CulturalIPKnowledgeBase

class BusinessAgentWorkflow:
    def __init__(self, rag_engine=None, api_key=None):
        self.rag_engine = rag_engine
        # 硬编码硅基流动配置（请替换为你的真实信息）
        self.llm = ChatOpenAI(
            model="Qwen/Qwen2.5-7B-Instruct",  # 硅基流动支持的模型
            temperature=0.7,
            openai_api_key="sk-luuenjceutdqayerfufqrqyqkrdkyaangylzxipvzrllyspp",      # 替换
            openai_api_base="https://api.siliconflow.cn/v1"
        )
    
    def run(self, query: str) -> str:
        ip_context = ""
        if self.rag_engine:
            try:
                docs = self.rag_engine.search(query, k=3)
                ip_context = "\n".join([doc.page_content for doc in docs])
            except Exception as e:
                ip_context = f"（检索失败：{e}）"
        
        try:
            strategy_prompt = ChatPromptTemplate.from_template(
                "基于以下文化IP元素：\n{ip_context}\n\n针对问题：{query}\n请制定详细的商业策略（包括目标受众、商业模式、实施路径、风险评估）。"
            )
            strategy_chain = strategy_prompt | self.llm | StrOutputParser()
            strategy = strategy_chain.invoke({"ip_context": ip_context, "query": query})
            
            budget_prompt = ChatPromptTemplate.from_template(
                "根据以下商业策略，估算预算（研发成本、营销预算、运营成本、预期ROI、实施周期）：\n{strategy}"
            )
            budget_chain = budget_prompt | self.llm | StrOutputParser()
            budget = budget_chain.invoke({"strategy": strategy})
            
            marketing_prompt = ChatPromptTemplate.from_template(
                "针对问题：{query}\n结合商业策略：{strategy}\n制定创新的营销方案（渠道、内容、活动、KPI）。"
            )
            marketing_chain = marketing_prompt | self.llm | StrOutputParser()
            marketing = marketing_chain.invoke({"query": query, "strategy": strategy})
            
            return f"""
## 📊 商业决策报告

### 检索到的文化IP元素
{ip_context[:500]}{'...' if len(ip_context) > 500 else ''}

### 商业策略分析
{strategy}

### 预算估算
{budget}

### 营销方案
{marketing}

---
*报告由AI商业Agent自动生成*
"""
        except Exception as e:
            error_msg = f"生成报告失败：{str(e)}\n\n{traceback.format_exc()}"
            print(error_msg)
            return f"生成报告失败：{str(e)}"