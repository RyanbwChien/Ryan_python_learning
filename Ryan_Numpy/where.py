# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 11:59:48 2025

@author: user
"""

import numpy as np
import random

random.choice([True,False]) # 只有抽一個

condi = np.random.choice([True,False], size=20, replace=True) # 可隨機選取 size 個

np.where(condi, 1, 0) # 條件成立回傳1 不成立回傳0
