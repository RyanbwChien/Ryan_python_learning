# -*- coding: utf-8 -*-
"""
Created on Tue Apr  8 09:33:02 2025

@author: USER
"""

from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: float
    
obj = Item(**{'name':'123', "price":456})
obj.json()
obj.dict()




import json
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: float

def process_item(item: Item):
    print(f"Processing item: {item.name} with price {item.price}")

# 假設來自外部 API 的 JSON 資料
json_data = '{"name": "Smartphone", "price": 999.99}'

# 將 JSON 字符串轉換為字典並創建 Item 物件
item = Item.parse_raw(json_data)
process_item(item)
