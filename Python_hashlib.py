# -*- coding: utf-8 -*-
"""
Created on Fri Mar 28 11:33:59 2025

@author: USER
"""

# hash() 在不同 Python 版本或不同運行時可能會有不同結果，因此這種方法不可靠。
# 無法直接透過 hash() 回傳的數字來 反推 出原始字串，因為 hash() 是一個不可逆的雜湊函數


import hashlib

# 建立 SHA-256 雜湊表
def sha256_hash(text):
    return hashlib.sha256(text.encode()).hexdigest()

hash_dict = {sha256_hash(word): word for word in ["apple", "banana", "cherry"]}

# 查找 SHA-256 雜湊值
def reverse_sha256(target_hash):
    return hash_dict.get(target_hash, "Not Found")

if __name__ == "main":
    hashed_value = sha256_hash("banana")
    print(reverse_sha256(hashed_value))  # 成功找到 "banana"
