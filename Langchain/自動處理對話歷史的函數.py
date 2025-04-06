# -*- coding: utf-8 -*-
"""
Created on Mon Apr  7 01:18:52 2025

@author: user
"""

from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_openai import ChatOpenAI

# 1. 設定 LLM（GPT-4o）
llm = ChatOpenAI(
    model="gpt-4o",
    temperature=0.8,
    max_tokens=1000,
)

# 2. 初始化聊天歷史
chat_history = [
    SystemMessage(content="你是資料分析助理，請根據使用者的問題分析資料。")
]

# 3. 定義對話模板（將 `MessagesPlaceholder` 留給動態變更）
prompt = ChatPromptTemplate.from_messages([
    SystemMessage(content="你是資料分析助理，請根據使用者的問題分析資料。"),
    MessagesPlaceholder(variable_name="input")
])

# 4. 自動處理對話歷史的函數
def get_response(user_input):
    # 1. 生成使用者訊息並加入歷史記錄
    chat_history.append(HumanMessage(content=user_input))
    
    # 2. 將歷史訊息與 prompt 組合並傳遞給 LLM
    response = llm.invoke(chat_history + [MessagesPlaceholder(variable_name="input")])
    
    # 3. 取得 LLM 的回應並將其加入歷史
    ai_message = AIMessage(content=response.content)
    chat_history.append(ai_message)
    
    return response.content

# 5. 呼叫範例
user_question = "男女平均年齡是多少？"
response = get_response(user_question)
print(response)

# 接著再問一個問題
user_question_2 = "那哪一組比較年輕？"
response2 = get_response(user_question_2)
print(response2)
