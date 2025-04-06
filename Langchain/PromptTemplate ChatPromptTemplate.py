# -*- coding: utf-8 -*-
"""
Created on Sun Apr  6 00:22:48 2025

@author: user
"""

from langchain.prompts import PromptTemplate
from langchain.prompts.chat import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate,
)


# =============================================================================
# 在 langchain 中，根據使用情境來看，ChatPromptTemplate 和 PromptTemplate 都是常見的選擇，
# 但兩者的使用方式略有不同。
# =============================================================================

'''
1. PromptTemplate：
主要用途：用於生成傳統的單一問題或命令，這些問題是直接傳遞給模型的。

常見用途：若你只需要單一的 prompt 來生成回應，這是最常用的選擇，尤其在非對話型應用中。

使用範例：
'''

from langchain.prompts import PromptTemplate

prompt_template = PromptTemplate(
    input_variables=["name"],
    template="Hello, {name}!"
)

'''
2. ChatPromptTemplate：
主要用途：專門用於生成適合聊天的 prompt。這通常是多輪對話的情境，會包含多個訊息模板（例如，Human、System 訊息）。

常見用途：如果你的應用是基於多輪對話，或者需要區分系統訊息和使用者訊息，這個選擇比較常見。

使用範例：
'''

from langchain.prompts.chat import ChatPromptTemplate, HumanMessagePromptTemplate, SystemMessagePromptTemplate

prompt_template = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("human", "{question}"),
])


'''
🏆 最常用的選擇：
如果是簡單的問題與回應，尤其在 非對話型 應用中，PromptTemplate 更為常見。

如果是設計多輪對話，或者想要定義系統消息、使用者消息等多個不同角色，則 ChatPromptTemplate 是更常見的選擇。

通常，若你的應用涉及聊天機器人、客服等對話型應用，ChatPromptTemplate 的使用頻率會較高；如果只是需要簡單生成一個 prompt，PromptTemplate 是最基本且常見的。

你目前的使用場景是什麼？這樣我可以幫你更精確地選擇適合的模板。
'''