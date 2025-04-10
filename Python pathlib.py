# -*- coding: utf-8 -*-
"""
Created on Thu Apr 10 13:00:51 2025

@author: USER
"""


from pathlib import Path

Path(r"123/456") / "133"

# =============================================================================
# 
# 這是一個 pathlib.Path 的超強功能之一，它的 / 運算子被重載（overload）來當作路徑拼接使用了！
# 
# ✅ 你寫的程式碼解釋：
# python
# 複製
# 編輯
# from pathlib import Path
# 
# Path(r"123/456") / "133"
# 這邊發生了什麼事？
# 
# Path(r"123/456") → 建立一個路徑物件，表示 123/456。
# 
# Path(...) / "133" → / 在 Path 類別中被重新定義，變成「把 "133" 接在這個路徑的後面」。
# 
# 結果變成：123/456/133
# 
# ✅ / 在 pathlib.Path 中的角色
# 在 pathlib 裡，/ 被用來像這樣直覺地拼接路徑：
# 
# python
# 複製
# 編輯
# base = Path("folder")
# full = base / "subfolder" / "file.txt"
# print(full)  # folder/subfolder/file.txt
# 等同於：
# 
# python
# 複製
# 編輯
# Path("folder/subfolder/file.txt")
# 比傳統的 os.path.join() 更簡潔、直觀、乾淨，而且支援跨平台。
# 
# ✅ 類似範例
# python
# 複製
# 編輯
# from pathlib import Path
# 
# p = Path("my_project") / "data" / "train.csv"
# print(p)  # my_project/data/train.csv
# ✅ / 的本質是什麼？
# 其實是 Path 類別裡的魔術方法 __truediv__()：
# 
# python
# 複製
# 編輯
# class Path:
#     def __truediv__(self, key):
#         # 實作如何接上子目錄
# 這樣一來就可以用 / 當作語法糖，讓你寫路徑像寫字串一樣簡單 😎
# =============================================================================
