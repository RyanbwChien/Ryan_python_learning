# -*- coding: utf-8 -*-
"""
Created on Tue Apr  8 16:05:44 2025

@author: USER
"""

# =============================================================================
# ChatPromptTemplate.from_messages 與  ChatPromptTemplate.from_messages 差異
# 
# 
# 這兩個都是 LangChain 的 prompt 建構方法，但用途和彈性不同，這邊直接幫你整理成對照表👇
# 
# 🔸 from_template 是最基本的 Prompt 建構器
# =============================================================================

from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_template("你叫什麼名字？我叫 {name}")
# =============================================================================
# ✅ 適合單一句子模板
# ✅ 支援 .format 或 .invoke({"name": "小明"})
# ❌ 不支援多輪訊息（例如多段角色訊息）
# 🔸 from_messages 是多輪對話訊息的建構器
# =============================================================================

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

prompt = ChatPromptTemplate.from_messages([
    ("system", "你是一個助理"),
    ("user", "你好"),
    ("ai", "哈囉！"),
    ("user", "{question}"),
])

# =============================================================================
# 
# ✅ 可以建構多個角色的訊息（system、user、ai）
# 
# ✅ 支援 MessagesPlaceholder，用來串 memory 或多輪對話
# 
# ✅ 非常適合 Agent、Chat 應用
# 
# ✅ 支援多樣化訊息類型（也能接 tool call 等）
# 
# ✅ 較新版本也支援 JSON message 格式
# 
# 🔁 實際執行用 .invoke({"question": "現在幾點？"})
# 
# 🧠 簡單來說：
# 功能/差異點	from_template	from_messages
# 單句 prompt	✅ 適合	❌ 不適合
# 多段對話訊息	❌ 不支援	✅ 適合
# 插入變數	✅ {var}	✅ {var}
# 搭配記憶體	❌	✅ 支援 MessagesPlaceholder
# 適合用於	單輪輸入或簡單模板	Chat Agent、RAG、LangGraph 等
# 如果你是要開發 多輪對話 Agent 或工具調用型的 AI 助理，建議你使用 from_messages。
# 
# 要我幫你改寫一個範例讓兩種都看得懂差異嗎？
# 
# =============================================================================






