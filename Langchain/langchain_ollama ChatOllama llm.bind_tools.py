# -*- coding: utf-8 -*-
"""
Created on Tue Apr  8 22:57:19 2025

@author: user
"""

from langgraph.graph import StateGraph, END
from langgraph.prebuilt import ToolExecutor
from langchain_core.tools import tool
from langchain_ollama import ChatOllama

# 1. 建立工具
@tool
def mutily(a,b):
    """兩個數相乘
    
    Args:
    a: int
    b: int

    """
    return a*b

# tools = [double]
# tool_executor = ToolExecutor(tools)

# 2. 初始化 Ollama LLM
llm = ChatOllama(model="llama3.1:8b")
llm_with_tool = llm.bind_tools([mutily])
llm_with_tool.invoke("請問3 * 2 等於多少")
