# -*- coding: utf-8 -*-
"""
Created on Fri Mar 28 09:18:38 2025

@author: USER
"""

import seaborn as sns
import numpy as np
import pandas as pd

titanic_df = sns.load_dataset("titanic")

fare_class = titanic_df[['class', 'fare']].drop_duplicates()
len(fare_class)
# =============================================================================
# 為什麼 np.unique() 會報錯？
# NumPy 的 np.unique() 主要針對**單一數組（array）**運行，而 DataFrame 包含不同型別（如 str 和 float），導致 NumPy 嘗試排序時發生錯誤。
# =============================================================================

unique_groups = titanic_df[['class', 'fare']].apply(tuple, axis = 1) #變成Series
np.unique(unique_groups).__len__()

{ dict(i) for i in unique_groups}


titanic_df





hash("板橋榮家")
hash("華仁大樹中興北路日照")
