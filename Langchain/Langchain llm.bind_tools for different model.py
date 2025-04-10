# -*- coding: utf-8 -*-
"""
Created on Wed Apr  9 14:23:47 2025

@author: USER
"""

# qwen2.5:32b llama3.1:8b 有bind_tools功能
# gemma3:27b  deepseek-r1:14b 沒有bind_tools功能

import os
from langchain.chat_models import init_chat_model
from langchain_core.tools import tool
from langchain_ollama import ChatOllama

from langgraph.graph import StateGraph, MessagesState, START, END
from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="qwen2.5:32b",
    temperature=0,
    # other params...
)


@tool
def mutily(a,b):
    """兩個數相乘
    
    Args:
    a: int
    b: int

    """
    return a*b


llm_with_tool = llm.bind_tools([mutily])
res = llm_with_tool.invoke("請問3 * 2 等於多少")

print(res)