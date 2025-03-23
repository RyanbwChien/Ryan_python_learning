# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 10:11:19 2025

@author: user
"""

import pandas as pd

df1 = pd.DataFrame(
    {
        "A": ["A0", "A1", pd.NA, "A3"],
        "B": ["B0", "B1", "B2", "B3"],
        "C": ["C0", "C1", "C2", "C3"],
        "D": ["D0", "D1", "D2", "D3"],
    },
    index=[0, 1, 2, 3],
)


df1.value_counts()
