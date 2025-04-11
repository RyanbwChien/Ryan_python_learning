# -*- coding: utf-8 -*-
"""
Created on Fri Apr 11 14:16:06 2025

@author: USER
"""

from langchain_groq import ChatGroq

from langchain_community.llms import Ollama

from ollama import chat
from ollama import ChatResponse

response: ChatResponse = chat(model='llama3.1:8b', messages=[
  {
    'role': 'user',
    'content': 'Why is the sky blue?',
  },
  {
    'role': 'system',
    'content': '請用中文回答',
  },
])
print(response['message']['content'])
# or access fields directly from the response object
print(response.message.content)
# 使用 DeepSeek 或 Llama3 作為 Agent 的 LLM
llm = Ollama(model="llama3.1:8b")  # 也可以改成 "llama3:8b"



from langchain.chat_models import init_chat_model

model = init_chat_model("llama3.1:8b", model_provider="ollama")


from langchain_core.prompts import HumanMessagePromptTemplate
