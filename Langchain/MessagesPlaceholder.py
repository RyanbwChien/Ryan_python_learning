# -*- coding: utf-8 -*-
"""
Created on Tue Apr  8 15:55:49 2025

@author: USER
"""

# MessagesPlaceholder(variable_name="input") 是在 LangChain 裡用來表示一個「訊息佔位符」的元件，常出現在 ChatPromptTemplate 當中。




# [問題]  MessagesPlaceholder是不是會將USER輸入的對話進去 變成新的 HUMANMESSAGE 插入在記憶體中LIST裡面?
    
# ✅ 是的，你完全理解正確！

memory = ConversationBufferMemory(
    memory_key="messages",
    return_messages=True
)

prompt = ChatPromptTemplate.from_messages([
    ("system", "你是個 helpful assistant"),
    MessagesPlaceholder(variable_name="messages"),  # <== 重點
    ("user", "{input}")
])
# 這裡的 MessagesPlaceholder(variable_name="messages") 會自動被 memory 中記錄的歷史對話所取代，格式是 HumanMessage（user 輸入）和 AIMessage（模型回覆）的 list。

# =============================================================================
# 🧠 所以實際流程如下：
# 使用者輸入第一個問題（input: "今天天氣如何？"）
# 
# 模型回覆（例如: "今天天氣晴"）
# 
# 這一對對話會被記錄到 memory 中，格式像這樣：
# =============================================================================

[
    HumanMessage(content="今天天氣如何？"),
    AIMessage(content="今天天氣晴")
]


# =============================================================================
# 下一輪對話時，這些 message 就會被插入到 MessagesPlaceholder 那一行，成為上下文的一部分
# 
# 然後新的 ("user", "{input}") 就是這一輪的新輸入
# 
# ✅ 重點回覆你的問題：
# MessagesPlaceholder 是不是會將 USER 輸入的對話進去變成新的 HumanMessage？
# 
# ✔️ 是的，會
# 每一輪的使用者輸入都會自動變成新的 HumanMessage，並由 ConversationBufferMemory 幫你記錄下來，供後續上下文使用。
# =============================================================================

















🎯 功能簡介
它的用途是：
➡️ 在 prompt 中保留一個位置，用來插入多輪對話訊息（messages）。這對於 Agent 或 Chat 互動來說非常重要。

🧩 使用範例
假設你這樣定義 prompt：

python
複製
編輯
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

prompt = ChatPromptTemplate.from_messages([
    ("system", "你是一個智慧助理"),
    MessagesPlaceholder(variable_name="input"),
    ("user", "請幫我總結上面的對話")
])
# =============================================================================
# 這代表：
# 一開始會給 LLM 一個系統角色。
# 
# 然後會在 "input" 這個位置插入多輪對話記錄。
# 
# 最後再補上一句：「請幫我總結上面的對話」。
# 
# 🛠 真實用法（搭配 Agent）
# 當你使用像這樣的 Chain 或 Agent：

chat_prompt = ChatPromptTemplate.from_messages([
    ("system", "你是滙嘉健康的查詢助手"),
    MessagesPlaceholder(variable_name="messages")
])

chain = chat_prompt | llm
# =============================================================================
# 當你呼叫 chain.invoke({"messages": [...訊息列表...]})
# 就會把整個對話訊息插入這個 Placeholder 裡！
# =============================================================================

✅ 什麼時候用？
使用 ChatPromptTemplate + 多輪對話時。

Agent 記憶體（memory）在記錄訊息時。

用 tools 時，把過去訊息給 model。

🧠 小補充：搭配 ConversationBufferMemory
如果你是 Agent 架構，也會看到這種寫法：

memory = ConversationBufferMemory(return_messages=True, memory_key="messages")
這時你就會在 prompt 裡用：

MessagesPlaceholder(variable_name="messages")
這樣 memory 裡的訊息會自動插進去！





✅ 是的，如果你這樣用：

prompt = ChatPromptTemplate.from_messages([
    MessagesPlaceholder(variable_name="input"),
])
然後後續執行時你給它：

python
複製
編輯
prompt.invoke({"input": messages})
那麼這個 messages（一串對話記錄，例如 ChatMessage 格式的 list）就會插進去這個 MessagesPlaceholder 的位置。

❗️但「是否會持續記錄」要看你有沒有用 記憶體機制（memory）
MessagesPlaceholder 本身 只是個佔位符，不會自動幫你記錄對話。

要做到「每一輪對話都自動加進去」，你需要搭配：

🧠 ConversationBufferMemory（或其他記憶體類型）
範例如下：

python
複製
編輯
from langchain.memory import ConversationBufferMemory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

memory = ConversationBufferMemory(
    memory_key="messages",     # 對應到下面 Placeholder 的 variable_name
    return_messages=True
)

prompt = ChatPromptTemplate.from_messages([
    ("system", "你是個 helpful assistant"),
    MessagesPlaceholder(variable_name="messages"),  # 這會被 memory 自動填入
    ("user", "{input}")  # 目前這一輪的提問
])
然後在 Agent/Chain 中你就會看到：


chain = prompt | llm

# 第一輪
res1 = chain.invoke({"input": "你好"}, config={"configurable": {"memory": memory}})

# 第二輪，記憶體已保留上一輪
res2 = chain.invoke({"input": "剛剛我說了什麼？"}, config={"configurable": {"memory": memory}})
🔁 總結重點
功能	是否自動
MessagesPlaceholder 插入訊息	✅
自動記錄使用者對話	❌（需要搭配 memory）
多輪對話上下文連貫	✅（搭配記憶體）
如果你是用 LangGraph 的話，也可以搭配 memory node 或用 state 傳遞 message list，我也可以幫你做一個模組化設計 🌟