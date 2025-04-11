# -*- coding: utf-8 -*-
"""
Created on Thu Apr 10 15:10:20 2025

@author: USER
"""

from langchain_core.messages import AnyMessage, HumanMessage, AIMessage
from typing_extensions import TypedDict


class State(TypedDict):
    messages: list[AnyMessage]
    extra_field: int
State({"messages": '1',"extra_field":2})    


# =============================================================================
# 寫法	版本要求	範例
# list[int]	Python 3.9+	list[HumanMessage]
# List[int]	Python <3.9	List[HumanMessage]（需 from typing import List）
# =============================================================================


# =============================================================================
# 這表示 State 是一個字典，其結構應該像這樣：
# 
# {
#     "messages": [<AnyMessage>, <AnyMessage>, ...],
#     "extra_field": 42
# }
# messages: 是一個 AnyMessage 類別的 list。
# 
# extra_field: 是一個 int 整數。
# 
# =============================================================================


state: State = {
    "messages": [HumanMessage(content="Hello"), AIMessage(content="Hi there!")],
    "extra_field": 10
}

'''TypedDict 只是型別提示（type hint），不是強制的限制'''
# =============================================================================
# class State(TypedDict):
#     messages: list[AnyMessage]
#     extra_field: int
# State({"messages": '1',"extra_field":2})    
# 但為何"messages": '1'這樣寫不會報錯
# =============================================================================


    

from typing import Optional

# =============================================================================
# Optional 意思
# 
# Optional 在 Python 的 type hint 裡，意思是「這個變數可以是某個類型，也可以是 None」。
# =============================================================================


# =============================================================================
# from typing import Optional
# 
# x: Optional[int] = 42     # ✅ 合法
# 
# 問題: x 是要一個list裡面放int的物件嗎?
# =============================================================================


# =============================================================================
# ❌ 它不是 list 裡面放 int，而是單純一個 int 或 None。
# ✅ 如果你想要「一個 list 裡面放 int」的值，那要這樣寫：
# python
# 複製
# 編輯
# x: list[int] = [1, 2, 3]
# 如果你想讓這個 list 本身可以是 None（也就是：要嘛是 list of int，要嘛是 None），那就結合 Optional：
# 
# python
# 複製
# 編輯
# x: Optional[list[int]] = [1, 2, 3]   # ✅ 合法
# x = None                             # ✅ 也合法
# 這樣 x 就是「一個整數 list 或 None」。
# =============================================================================



