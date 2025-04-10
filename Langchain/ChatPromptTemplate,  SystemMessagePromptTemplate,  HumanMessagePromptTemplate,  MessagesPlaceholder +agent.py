# -*- coding: utf-8 -*-
"""
Created on Mon Apr  7 00:39:16 2025

@author: user
"""

from langchain_experimental.agents import create_pandas_dataframe_agent
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import SystemMessage
from langchain_openai import ChatOpenAI

import os
import seaborn as sns

df = sns.load_dataset("titanic")

OPENAI_API_KEY = os.environ["openai_apikey"]

# 1. 建立 LLM（這裡用 GPT-4o，也可用 gpt-3.5-turbo）
llm = ChatOpenAI(
    model="gpt-4o",
    temperature=0.8,
    max_tokens=1000,
    openai_api_key=OPENAI_API_KEY
)


from langchain.prompts import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder,
)

# =============================================================================
# SystemMessagePromptTemplate 和 HumanMessagePromptTemplate 是讓你可以動態設定 message 內容（用 {} 佔位符）。
# SystemMessage 和 HumanMessage 則是靜態訊息（固定文字）。
# MessagesPlaceholder 必須對應 AgentExecutor 或 Runnable 中的 key，通常是 "input"。
# =============================================================================


# =============================================================================
# 🔍 重點說明：MessagesPlaceholder(variable_name="input") 是什麼？
# 這行的意思是：
# 當你呼叫 agent.invoke("你的問題") 時，那個 "你的問題" 會被當成變數 input 的值，並插入到對話中當作一個 HumanMessage。
# 所以 MessagesPlaceholder(variable_name="input") 並不是直接變成「字串」，而是 LangChain 在背後會把你傳入的值轉換成一條 HumanMessage，插入對話歷史中。
# 
# ✅ 實際例子：
# 你有這段 prompt：
# =============================================================================

# =============================================================================
# prompt = ChatPromptTemplate.from_messages([
#     SystemMessage(content="你是個資料助理"),
#     MessagesPlaceholder(variable_name="input")
# ])
# 
# agent.invoke("男女平均年齡是多少？")
# =============================================================================
# =============================================================================
# LangChain 背後實際會把你這句包成這樣的對話格式 👇
# [
#     SystemMessage(content="你是個資料助理"),
#     HumanMessage(content="男女平均年齡是多少？")
# ]
# =============================================================================
# =============================================================================
# ✅ 所以，結論：
# MessagesPlaceholder(variable_name="input") 不會等於字串 "男女平均年齡是多少？"。
# 
# 它的作用是：把你傳給 .invoke() 的值，用對應的 message 類型（通常是 HumanMessage）自動插進去。
# 
# 🧠 延伸技巧：如果你有多段對話歷史
# 你可以傳進多段 message，例如：
# =============================================================================

# =============================================================================
# from langchain_core.messages import HumanMessage, AIMessage
# 
# chat_history = [
#     HumanMessage(content="請問這份資料有哪些欄位？"),
#     AIMessage(content="欄位有姓名、年齡、性別、薪資。"),
#     HumanMessage(content="男女平均年齡是多少？")
# ]
# 
# agent.invoke({"input": chat_history})
# 這時 MessagesPlaceholder(variable_name="input") 會插入這整段訊息歷史。
# =============================================================================





from langchain_core.messages import SystemMessage

prompt = ChatPromptTemplate.from_messages([
    SystemMessage(content="你是一位資料分析助理，擅長用 pandas 處理資料。"),
    
    # ✅ 動態 System Prompt Template
    SystemMessagePromptTemplate.from_template(
        "請保持回覆在 {char_limit} 字以內。"
        "sex:性別"
        "age:年齡"
    ),

# =============================================================================
#     # ✅ 動態 Human Message Prompt Template
#     HumanMessagePromptTemplate.from_template(
#         "這是使用者的問題：{user_question}"
#     ),
# =============================================================================

    # ✅ 插入訊息歷史記錄（例如 AgentExecutor 輸入）
    MessagesPlaceholder(variable_name="input"),
])

# 用來帶參數
filled_prompt = prompt.format(
    char_limit=100,
    # user_question="男女平均年齡是多少?",
    input=[]  # 如果是搭配 agent executor，會自動處理這個
)

# 3. 建立 Agent
agent = create_pandas_dataframe_agent(
    llm=llm,
    df=df,
    prompt=prompt,
    verbose=True,
    allow_dangerous_code=True,
    # handle_parsing_errors=True,
)

# 4. 使用 Agent
response = agent.invoke("男女平均年齡是多少?")
print(response)


