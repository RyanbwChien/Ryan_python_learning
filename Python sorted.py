# -*- coding: utf-8 -*-
"""
Created on Thu Mar 27 15:15:05 2025

@author: USER
"""

iterable = list(reversed(range(10)))

sorted(iterable, key=None, reverse=False)

# iterable：要排序的可迭代物件（如列表、元組等）。
# key：一個函數，對每個元素應用該函數的返回值進行排序（默認為 None）。
# reverse：如果設為 True，則降序排序（默認為 False，即升序排序）。


class obj:
    def __init__(self):
        self.new = 123
    def __eq__