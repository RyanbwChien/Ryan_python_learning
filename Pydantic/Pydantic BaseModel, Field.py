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
