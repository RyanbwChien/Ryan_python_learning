# -*- coding: utf-8 -*-
"""
Created on Sat Apr  5 17:23:20 2025

@author: user
"""

code = """
def test(xx):
    return xx+5
print(test(xx))
"""

exec(code, {"xx":5}) # 可以從外部帶參數


eval("1+1")
