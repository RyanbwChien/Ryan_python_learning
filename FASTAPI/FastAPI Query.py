# -*- coding: utf-8 -*-
"""
Created on Thu Apr 10 23:26:35 2025

@author: user
"""

from fastapi import Query

q: str = Query(default=None, min_length=3, max_length=50)

# 好問題！Query(min_length=3, max_length=50) 是 FastAPI 提供的一個函式，用來設定查詢參數（query parameters）的驗證條件，也可以提供一些額外的 metadata，例如預設值、描述、範例等。

# =============================================================================
# 這段意思是：q 是一個查詢參數（例如 /items?q=hello 中的 q），它：
# 
# 是 str 類型
# 
# 最小長度為 3
# 
# 最大長度為 50
# 
# 預設值是 None
# 
# FastAPI 會自動根據這些條件進行驗證。
# =============================================================================

from fastapi import FastAPI, Query
from typing import Annotated

app = FastAPI()

@app.get("/items/")
def read_items(q: Annotated[str, Query(min_length=3, max_length=10)]):
    return {"q": q}

# =============================================================================
# 這會產生一個 /items?q=xxx 的 API：
# 
# 如果少於 3 個字元：會回傳 422 錯誤（Unprocessable Entity）
# 
# 超過 10 個字元：同樣報錯
# 
# 並且這些驗證條件會顯示在 /docs Swagger UI 上
# =============================================================================


# metadata 是甚麼?

# =============================================================================
# 🔍 在 Python 中的應用
# 在 Python 中，metadata 常用於裝飾器、型別註解、庫的配置選項等。metadata 本身不會改變函數或變數的行為，但可以幫助一些工具（例如 FastAPI、Pydantic 或靜態分析工具）進行進一步的處理。
# 
# 💡 例子 1: FastAPI 中的 Query 和 metadata
# 當你在 FastAPI 中使用 Query 或 Body 等來描述參數時，你就會使用 metadata。比如：
# 
# =============================================================================

from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/items/")
def read_items(q: str = Query(..., min_length=3, max_length=50, description="Search query")):
    return {"q": q}
# =============================================================================
# 在這裡：
# 
# min_length=3 和 max_length=50 是驗證的 metadata，限制了 q 參數的最小和最大長度。
# 
# description="Search query" 是描述文字，它在 FastAPI 生成的 API 文檔中會顯示，幫助用戶理解這個參數的用途。
# 
# 這些 metadata 會被 FastAPI 使用，用來生成 API 文檔（Swagger UI）或進行參數驗證。
# 
# 
# 🚀 總結
# metadata 是用來描述數據的額外資訊，通常用於輔助處理、文檔生成或驗證，但不會直接影響數據本身的邏輯。
# 
# 在 FastAPI 中，metadata 主要用於控制如何處理請求參數（例如查詢參數、路由參數等），並且它會影響文檔、驗證等。
# =============================================================================

