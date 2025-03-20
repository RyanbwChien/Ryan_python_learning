# -*- coding: utf-8 -*-
"""
Created on Thu Mar 20 20:43:16 2025

@author: user
"""
'''
Python 函數的參數順序確實有特定的要求。當你定義函數時，必須遵循一定的順序來排列不同類型的參數。這些類型的參數包括 位置參數、可變長度位置參數（*args）和 可變長度關鍵字參數（**kwargs）。以下是 Python 函數定義中參數的正確順序：

參數順序規則：
位置參數（Positional Parameters）
可變長度位置參數（*args，Positional Variable-length Arguments）
關鍵字參數（Keyword Parameters）
可變長度關鍵字參數（**kwargs，Keyword Variable-length Arguments）
'''

def func(a, b, c, *args, d=4, e=5, **kwargs):
    print(a, b, c)
    print(args)
    print(d, e)
    print(kwargs)

func(1, 2, 3, 6, 7, d=8, f=9)

# 一般定義函數參數也是稱為位置參數 EX: def test(a,b,c) a,b,c也是位置參數

# =============================================================================
# *arg
# 可變動位置參數(位置引數（Positional Variable-length Arguments） 傳遞值時，不需要指定參數名稱，直接按照順序賦值。
# 
    # *kwarg
    # 關鍵字引數（Keyword Variable-length Arguments）
# 關鍵字引數是在函數調用時，通過指定參數名稱來傳遞值的參數。 這樣的傳遞方式與參數在函數定義中的順序無關。        
# =============================================================================

def ttt(a,b,c,*arg,**kwarg):
    
    
    return ([a+b+c,arg,kwarg])

ttt(1,  2, 3, 3,4,5,v=6,j=7,k=8)



# =============================================================================
# *iterable 解包後的變化
# 調用方式	進入函數的 arg 內容
# test_arg(*[1,2,3])	(1, 2, 3)（tuple）
# test_arg(*(1,2,3))	(1, 2, 3)（tuple）
# =============================================================================

# =============================================================================
# * 只能在函數參數中解包，不能單獨在全局範圍解包 iterable。
# 在函數內使用 * 解包可迭代對象（如 list 或 tuple）是合法的，這會把它的元素作為單獨的參數傳遞給函數。
# 在全局範圍內，* 只能在函數調用或參數中使用，不能單獨在語句中使用。
# =============================================================================

def test_arg(*arg):
    for i in arg:
        print(i)
    print(arg)
    
test_arg(*[1,2,3]) 
# 1. test_arg(*[1,2,3]) 先解包成 test_arg(1,2,3)
# 2. test_arg(1,2,3) 因為預設def test_arg(*arg) 會將輸入的參 1,2,3 數變成 tuple (1,2,3)傳給 arg
test_arg(*(1,2,3))


dict_parameter = {
    "A":1,
    "B":2,
    "C":3
    }

def test_kwarg(**kwarg):
    print(kwarg.values())
# 1. test_arg(**{"A":1,"B":2,"C":3}) 先解包成 test_kwarg(A=1,B=2,C=3)
# 2. test_kwarg(A=1,B=2,C=3) 因為預設def test_arg(**kwarg) 會將輸入的可變動KW參數 A=1,B=2,C=3 數變成 dict(A=1,B=2,C=3)傳給 kwarg
    
test_kwarg(**dict_parameter)