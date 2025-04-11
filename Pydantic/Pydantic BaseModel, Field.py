# -*- coding: utf-8 -*-
"""
Created on Tue Apr  8 10:25:45 2025

@author: USER
"""


from pydantic import BaseModel, Field


class FraudNewsSchema(BaseModel):
    reported_date: str = Field(..., description="The date the article or case occurred.")
    victim_gender: str = Field(..., description="ender of the victim (e.g., Male, Female, if the date is not available, then null.")
    victim_age: int = Field(..., description="Age of the victim. if the date is not available, then null.")
    fraud_type: str = Field(..., description="Type of fraud (e.g., phishing, investment scam. if the date is not available, then null.")
    fraud_details: str = Field(..., description="Specific tactics or messages used by the fraudsters. if the date is not available, then shownull.")
    financial_loss: str = Field(..., description="Total monetary loss suffered by the victim. if the date is not available, then null.")
    fraud_report: str = Field(..., description="original report full text of the news. if the date is not available, then null.")


# 在 Field(..., description="...") 中的 ...（三個點，又稱 Ellipsis），代表這個欄位是「必填」的，不能省略或為 None。這是 Pydantic 的寫法慣例，用來告訴模型：「這個欄位在建立物件時必須提供。」


from pydantic import BaseModel, Field

class Item(BaseModel):
    name: str = Field(..., description="The name of the item")
# 上面代表 name 是一個 必填欄位，如果你不給它值，Pydantic 會直接報錯。

Item(name="Book")           # ✅ 正常
Item()                      # ❌ 會出錯：缺少 'name'
type(Item) # 類別
# 可以像對待普通 Python 類別一樣使用 Item() 來創建實例。


Item(name="Book").dict()

# =============================================================================
# name: str = None
# 那 name 就變成選填的，而且還能是 None，這在你需要允許缺值的欄位時才會用。
# =============================================================================

# ... 是 Python 的一個特殊物件... 實際上是 Python 裡的內建物件 Ellipsis，你可以看到：

print(type(...))  # <class 'ellipsis'>
# 在 Pydantic 裡，這被用來標示欄位為「必填欄位」，是一種慣例寫法。



# =============================================================================
# ✅ 小總結：
# 寫法	意義
# Field(..., description="...")	必填欄位
# Field(None, description="...")	可為 None 或省略
# Field("default", description="...")	有預設值
# 
# =============================================================================

# =============================================================================
# 
# 
# 當我們說 Field() 用來「自訂欄位的行為」，意思是你可以控制這個欄位在資料驗證、轉換、預設值、API 文件上的各種「行為」與「規則」。
# 
# 🔧 Field() 常見的「自訂欄位行為」有：
# 1. ✅ 是否是必填欄位
# 
# from pydantic import BaseModel, Field
# 
# class User(BaseModel):
#     name: str = Field(...)  # 表示這是必填欄位，沒有預設值
# 2. 📝 加上描述（常用於文件或 Swagger）
# 
#     name: str = Field(..., description="使用者的名字")
# 3. ✏️ 設定預設值（也可以用等號，但 Field 比較彈性）
# 
#     age: int = Field(18, description="使用者年齡，預設是 18 歲")
# 4. 🔢 數值驗證（ge, le, gt, lt）
# 
#     age: int = Field(ge=0, le=120)  # 限制年齡介於 0 到 120
# 5. 🧵 長度限制（字串或 list）
# 
#     password: str = Field(min_length=8, max_length=32)
# 6. 🎯 正則驗證（字串格式）
# 
#     email: str = Field(pattern=r"^\S+@\S+\.\S+$")
# 7. 📛 別名（alias）和序列化選項
# 
#     full_name: str = Field(alias="fullName")  # 支援 camelCase → snake_case 轉換
# 8. 🧪 排除欄位、不序列化等進階選項
# 
#     token: str = Field(exclude=True)  # 不包含在輸出結果裡
# 🧠 總結一下：
# Field() 就像是欄位的「設定中心」，你可以透過它做以下事：
# 
# 類型	功能範例
# ✅ 必填與預設	Field(...), Field(default=123)
# 📖 說明	Field(description="說明文字")
# 🚦 驗證規則	ge=0, max_length=10, pattern=...
# 🪄 轉換與別名	alias="fullName", exclude=True
# =============================================================================

