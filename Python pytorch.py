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
