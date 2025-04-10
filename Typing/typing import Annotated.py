# -*- coding: utf-8 -*-
"""
Created on Thu Apr 10 22:29:37 2025

@author: user
"""

from typing import Annotated

from typing_extensions import Annotated


# =============================================================================
# 
# from typing import Annotated 和 from typing_extensions import Annotated 之間的差異主要在於 Python 版本支援度：
# 
# ✅ from typing import Annotated
# 標準函式庫中的版本
# 
# Python 3.9 開始正式納入 typing 模組中。
# 
# 適用於 Python 3.9 及以上版本。
# 
# 使用這個匯入方式代表你使用的是標準庫提供的 Annotated。
# 
# 🧪 from typing_extensions import Annotated
# 提供給舊版 Python 的向下相容支援
# 
# typing_extensions 是一個外部套件，用來補充新版本 typing 功能到舊版本 Python。
# 
# 適用於 Python 3.8 及以下 的版本，讓這些舊版本也能使用 Annotated。
# 
# 🔧 什麼時候用哪一個？
# 你的 Python 版本	匯入方式建議
# 3.9 或更新版本	from typing import Annotated
# 3.8 或更舊版本	from typing_extensions import Annotated
# ✨ 小提示
# 如果你正在開發一個支援多版本 Python 的套件，建議統一使用：
# 

# from typing_extensions import Annotated
# 這樣在不同 Python 版本中都能正確執行，避免錯誤。
# 
# =============================================================================


from typing import Annotated

MyType = Annotated[int, "這是額外資訊"]
# 在這裡，MyType 本質上還是 int，但附加了一個 "這是額外資訊" 註解。這個註解本身對執行期沒有影響，但工具可以用來做額外處理。


from fastapi import Query
from typing import Annotated

def read_items(
    q: Annotated[str, Query(min_length=3, max_length=50)] = "default"
):
    return {"q": q}

# =============================================================================
# 這裡 Annotated[str, Query(...)] 表示這個變數是 str 類型，但我們也提供了 FastAPI 專用的額外資訊來進行驗證和說明。
# 
# 🧠 概念總結
# Annotated[T, metadata1, metadata2, ...]
# 
# T 是實際的型別
# 
# 後面的 metadata 是附加資訊，可被工具使用
# 
# 執行時通常還是 T 的行為，不影響邏輯
# 
# 可與 pydantic, FastAPI, dataclass, dependency injection 等搭配使用
# =============================================================================
