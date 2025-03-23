# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 23:51:36 2024

@author: user
"""

import pandas as pd

'''
'dict'

{
colname_1:{index1:value_11, index2:value_21,..., indexn:value_n1},

colname_2:{index1:value_12, index2:value_22,..., indexn:value_n2},
   .....
colname_p:{index1:value_1p, index2:value_2p,..., indexn:value_np},
}
'''

pd.DataFrame(
{"A":{"1":1,"2":2,"3":3},
 "B":{"1":4,"2":5,"3":6},
 "C":{"1":7,"2":8,"3":9} 
 }
)

pd.DataFrame(
{"A":{"1":1,"2":2,"3":3},
 "B":{"1":4,"2":5,"3":6},
 "C":{"1":7,"2":8,"3":9} 
 }
).T


A = [1,2,3]
B = ['A','B','C']
C = [1.1,1.2,1.3]

pd.DataFrame(data= list(zip(A,B,C)), 
             columns=['A','B','C'])


import numpy as np
np.array([A,B,C]).T # array 裡面的元素資料型態都一樣

var = [A,B,C]

dict( )


import pandas as pd

# 定義三個變數
var1 = [1, 2, 3]
var2 = [4, 5, 6]
var3 = [7, 8, 9]

# 合併成 DataFrame
df = pd.DataFrame({
    "Variable1": var1,
    "Variable2": var2,
    "Variable3": var3
})

df
df.to_dict('list')
df.to_dict('records')
df.to_dict('dict')
df.to_dict('split')

df.to_dict('series')
df.to_dict('series')['Variable1']
df.to_dict('tight')
