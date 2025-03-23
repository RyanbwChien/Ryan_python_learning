# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 16:00:31 2024

@author: user
"""

from sklearn import datasets
import pandas as pd

datasets.load_iris()


df1 = pd.DataFrame(
    {
        "A": ["A0", "A1", "A2", "A3"],
        "B": ["B0", "B1", "B2", "B3"],
        "C": ["C0", "C1", "C2", "C3"],
        "D": ["D0", "D1", "D2", "D3"],
    },
    index=[0, 1, 2, 3],
)


df2 = pd.DataFrame(
    {
        "A": ["A4", "A5", "A6", "A7"],
        "B": ["B4", "B5", "B6", "B7"],
        "C": ["C4", "C5", "C6", "C7"],
        "D": ["D4", "D5", "D6", "D7"],
    },
    index=[4, 5, 6, 7],
)


df3 = pd.DataFrame(
    {
        "A": ["A8", "A9", "A10", "A11"],
        "B": ["B8", "B9", "B10", "B11"],
        "C": ["C8", "C9", "C10", "C11"],
        "D": ["D8", "D9", "D10", "D11"],
    },
    index=[8, 9, 10, 11],
)

df4 = pd.DataFrame(
    {
        "B": ["B2", "B3", "B6", "B7"],
        "D": ["D2", "D3", "D6", "D7"],
        "F": ["F2", "F3", "F6", "F7"],
    },
    index=[2, 3, 6, 7],
)


pd.merge(df1, df4, left_on='B', right_on = 'B')

# Merge two dataframes by index
pd.merge(df1, df4, left_index=True, right_index=True, how = 'left')


# A table 某一欄位 去跟 B table MERGE 做判斷式 (on A.sal > B.min_sal, A.sal<B.max_sal)


import pandas as pd

# 创建示例数据
data_a = {'id': [1, 2, 3, 4, 5], 'sal': [5000, 7000, 9000, 11000, 7500]}
data_b = {'id': [1, 2, 3], 'Degree':['A','B','C'] ,  'min_sal': [4000, 6000, 8000], 'max_sal': [6000, 8000, 10000]}

df_a = pd.DataFrame(data_a)
df_b = pd.DataFrame(data_b)

# 使用merge条件逻辑
merged_df = df_a.merge(df_b, how='cross')  # 使用笛卡尔积的方式进行合并
filtered_df = merged_df[(merged_df['sal'] > merged_df['min_sal']) & (merged_df['sal'] < merged_df['max_sal'])]

print(filtered_df)


result = []

# how = left
for A_row in range(len(df_a)):
    cnt = 0
    for B_row in range(len(df_b)):

        if (df_a.loc[A_row,'sal'] >= df_b.loc[B_row,'min_sal']) & (df_a.loc[A_row,'sal'] <= df_b.loc[B_row,'max_sal']):
            concat = pd.concat([df_a.loc[A_row,:], df_b.loc[B_row,:]])
            
            result.append(concat.to_dict())
            cnt += 1
    if cnt == 0:
        concat = pd.concat([df_a.loc[A_row,:], pd.Series([pd.NA]*len(df_b.columns),index = df_b.columns)])
        result.append(concat.to_dict())
        

# how = inner
for A_row in range(len(df_a)):
    for B_row in range(len(df_b)):

        if (df_a.loc[A_row,'sal'] >= df_b.loc[B_row,'min_sal']) & (df_a.loc[A_row,'sal'] <= df_b.loc[B_row,'max_sal']):
            concat = pd.concat([df_a.loc[A_row,:], df_b.loc[B_row,:]])
            
            result.append(concat.to_dict())

pd.DataFrame(result)

pd.DataFrame(
{"A":{"1":1,"2":2,"3":3},
 "B":{"1":4,"2":5,"3":6},
 "C":{"1":7,"2":8,"3":9} 
 }
)