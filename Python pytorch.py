# -*- coding: utf-8 -*-
"""
Created on Sun Mar 23 17:07:19 2025

@author: user
"""

import torch
tensor = torch.normal(0,1,(100,100))
type(tensor)

torch.randn_like(tensor) # torch.randn_like()是一个PyTorch 函数，它返回一个与输入张量大小相同的张量，其中填充了均值为0 方差为1 的正态分布的随机值

tensor.view(-1,1) # Returns a new tensor with the same data as the self tensor but of a different shape.


torch.tensor([1,2,3])

matrix = torch.normal(0,1,(100,10))

matrix.squeeze(1)
# =============================================================================
# 為 squeeze 只會刪除那些大小為 1 的維度，而 matrix 的形狀是 (100, 10)，這兩個維度的大小都不是 1，所以 squeeze 不會對 matrix 做任何變更。
# 
# torch.squeeze(dim) 只會移除大小為 1 的維度，而不會影響其他的維度。
# =============================================================================
