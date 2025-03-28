# -*- coding: utf-8 -*-
"""
Created on Fri Mar 28 11:48:53 2025

@author: USER
"""


import seaborn as sns
import numpy as np
import pandas as pd

titanic_df = sns.load_dataset("titanic")
titanic_df.columns

# =============================================================================
# 分組 (groupby)：
# titanic_df.groupby(['class', 'sex']) 首先根據 class 和 sex 這兩個欄位的值對資料進行分組。這會將 titanic_df 中相同 class 和 sex 的資料放到同一組。
# 選擇欄位 (['fare'])：
# 接著，你選擇了 fare 欄位，表示只對 fare 欄位中的資料進行操作。
# 聚合操作 (agg('sum'))：# 
# 使用 agg('sum') 聚合函數，它會對每個分組中的 fare 欄位進行總和計算。只有在執行 agg('sum') 這樣的聚合操作後，才會真正進行計算並返回結果。
# =============================================================================

# groupby 本身並不執行計算，它僅是分組操作。
# 執行 titanic_df.groupby(['class', 'sex']) 時，實際上只是告訴 pandas 對 titanic_df 這個 DataFrame 進行 分組操作，根據 class 和 sex 這兩個欄位的值來對資料進行分組。

titanic_df.groupby(['class','sex'])['fare'].agg('sum')


