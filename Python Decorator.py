# -*- coding: utf-8 -*-
"""
Created on Wed Mar 19 19:30:57 2025

@author: user
"""

#%% 
# decorator 
def decorator(func):
    def warraper(*args, **kwargs): #這是包裝函式，它會接收原始函式的所有參數（使用 *args 和 **kwargs），並將它們轉發給 func
        return func(*args, **kwargs)+1
    return warraper


@decorator
def fn(x):
    return(x+1)

fn(5)

#%% 
def arg_in_decorator(*args, **kwargs):  # 第1層：裝飾器接受參數
    def decorator(func):  # 第2層：這層是實際的裝飾器，它包裝函式
        def wrapper(*args, **kwargs):  # 第3層：包裝函式，執行原始函式，並修改結果
            return sum(args) + func(*args, **kwargs) + 1  # 在原來的結果上加 1
        return wrapper  # 返回包裝函式
    return decorator  # 返回真正的裝飾器函式

@arg_in_decorator(5)
def fn(x):
    return(x+1)

fn(5)


#%% 
class MyClass:
    def __init__(self):
        self.prefix = "[裝飾器]"

    def _decorator(self, func):  # 保護方法作為裝飾器
        def wrapper(*args, **kwargs):
            print(f"{self.prefix} 執行 {func.__name__}")
            return func(*args, **kwargs)
        return wrapper

    def example(self):
        @self._decorator  # 使用內部方法作為裝飾器
        def inner_function():
            print("執行內部函數")
        inner_function()

obj = MyClass()
obj.example()

#%% 
def print_func_name(func):
    def warp_1():
        print("Now use function '{}'".format(func.__name__))
        func()
    return warp_1


def print_time(func):
    import time
    def warp_2():
        print("Now the Unix time is {}".format(int(time.time())))
        func()
    return warp_2


@print_time
@print_func_name

def dog_bark():
    print("Bark !!!")
    
    
#%%    
import time
from functools import wraps
 
class Timer:
    def __init__(self, time_sleep):
        print('[__init__]')
        print('[time_sleep]:', time_sleep)
 
        self.time_sleep = time_sleep
 
    def __call__(self, func):
# =============================================================================
#         @wraps(func)
#         def wrap(*args, **kargs):
#             t_start = time.time()
#             time.sleep(self.time_sleep)
#             value = func(*args, **kargs)
#             t_end = time.time()
#             t_count = t_end - t_start
#             print('[共花費時間]', t_count)
#             return value
#  
#         return wrap
#         @wraps(func)
# =============================================================================
        def test(*args, **kargs):
            
            t_start = time.time()
            time.sleep(self.time_sleep)
            value = func(*args, **kargs)
            t_end = time.time()
            t_count = t_end - t_start
            print('[共花費時間]', t_count)
            return value
 
        return test
 
 
@Timer(time_sleep=3)
def dosomethingClass(a, b):
    print('do some thing')
    print('a + b = ', a + b)
 
 
dosomethingClass(1, 2)    

