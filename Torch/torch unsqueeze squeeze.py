# -*- coding: utf-8 -*-
"""
Created on Sat Mar 29 23:22:22 2025

@author: user
"""

import torch
# =============================================================================
# unsqueeze 用來增加維度，將指定位置插入大小為 1 的維度。
# squeeze 用來刪除大小為 1 的維度，簡化張量形狀。
# 這兩個操作在數據處理、模型輸入維度調整等情境中經常使用。
# =============================================================================

arr = torch.normal(0,1,(50,3))
arr.shape


# unsqueeze 用來增加維度，將指定位置插入大小為 1 的維度。
arr.unsqueeze(0).shape
arr.unsqueeze(1).shape
arr.unsqueeze(-1).shape


# squeeze 用來刪除大小為 1 的維度，簡化張量形狀。
arr.unsqueeze(-1).squeeze() # 預設不寫就是 用來刪除所有大小為 1 的維度，或是指定某個維度（dim）為 1 的時候將其刪除。
arr.unsqueeze(-1).squeeze(2) # 原來的tensor是在最後一維 維度是1 所以如果.squeeze()裡面的位置不是最後一維，會沒有效果
