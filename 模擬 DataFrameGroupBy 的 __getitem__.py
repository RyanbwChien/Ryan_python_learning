# -*- coding: utf-8 -*-
"""
Created on Fri Mar 28 12:02:25 2025

@author: USER
"""
class MyGroupBy:
    def __init__(self, data, group_columns):
        # 將資料轉換為字典格式
        self.data = data  
        self.group_columns = group_columns  # 用來分組的欄位

    def __getitem__(self, column_name):
        # 如果 column_name 在資料中
        if column_name in self.data[0]:  # 假設每個元素都是字典
            # 根據分組欄位對資料進行分組，這裡簡單處理
            group_data = {}
            for key, group in self._group_data().items():
                group_data[key] = [item[column_name] for item in group]
            return group_data
        else:
            raise KeyError(f"Column '{column_name}' not found in the DataFrame")

    def _group_data(self):
        # 簡單的分組方法，按給定欄位進行分組
        grouped = {}
        for row in self.data:
            key = tuple(row[col] for col in self.group_columns)
            if key not in grouped:
                grouped[key] = []
            grouped[key].append(row)
        return grouped

# 範例資料
data = [
    {'class': 'First', 'sex': 'female', 'fare': 50.0, 'age': 22},
    {'class': 'Second', 'sex': 'male', 'fare': 15.2, 'age': 35},
    {'class': 'First', 'sex': 'male', 'fare': 8.75, 'age': 28},
    {'class': 'Second', 'sex': 'female', 'fare': 20.0, 'age': 30}
]

# 建立 MyGroupBy 物件
grouped = MyGroupBy(data, ['class', 'sex'])

# 使用 __getitem__ 按欄位名稱選擇
print(grouped['fare'])
