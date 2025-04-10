# -*- coding: utf-8 -*-
"""
Created on Thu Apr 10 23:40:26 2025

@author: user
"""

'''
所以YIELD本質上也是透過 __ITER__ 跟 __NEXT__組成的嗎?
是的，yield 本質上是透過 __iter__() 和 __next__() 來實現的，並且它們的行為非常相似。當你使用 yield 時，你其實是在創建一個生成器，它自動具備了 __iter__() 和 __next__() 方法的功能。
'''

def generator(x):
    for i in range(x):
        print(i)
        yield(i)
        
gg = generator(5)


next(gg)


# =============================================================================
# 將生成器寫成類別的方式，通常是為了更細緻地控制生成器的狀態，或是當你需要更多的功能和可定制性時。使用類別來實現生成器相當於創建一個自定義的迭代器。
# 
# 類別實現生成器
# 你可以通過實現 __iter__() 和 __next__() 方法來讓一個類別具備生成器的功能。__iter__() 方法返回迭代器本身，而 __next__() 方法定義如何產生下個項目。
# 
# 這裡是一個簡單的例子，將生成器寫成類別：
# =============================================================================

class MyGenerator:
    def __init__(self, x):
        self.x = x
        self.current = 0  # 初始化當前值
    
    # 讓類別成為可迭代物件
    def __iter__(self):
        return self
    
    # 生成器的核心邏輯
    def __next__(self):
        if self.current < self.x:
            value = self.current
            self.current += 1
            return value
        else:
            raise StopIteration  # 當生成器結束時，引發 StopIteration

# 使用 MyGenerator 類別
gg = MyGenerator(5)

for item in gg:
    print(item)  # 輸出 0 1 2 3 4
# =============================================================================
# 說明：
# __init__()：
# 
# 這是初始化方法，用來設置生成器的初始狀態。這裡 self.x 是生成器的範圍（類似之前的 range(x)），self.current 是當前的索引。
# 
# __iter__()：
# 
# 這使得 MyGenerator 類別成為一個可迭代物件，返回自身，這樣就可以使用 for 迴圈來進行迭代。
# 
# __next__()：
# 
# 這個方法實現了生成器的核心邏輯。每次調用 __next__() 時，會返回當前的 current 值，然後遞增 current，直到達到 x。
# 
# 當達到結束條件時，raise StopIteration 會停止生成器的運行。
# =============================================================================

# =============================================================================
# 🌟 進一步的擴展：
# 你可以將更多的功能和條件加入到這個類別中，例如設置起始值、步進值，甚至是異常處理等。這樣你可以創建更靈活的生成器。
# 
# =============================================================================
class CustomGenerator:
    def __init__(self, start, stop, step=1):
        self.start = start
        self.stop = stop
        self.step = step
        self.current = start
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current >= self.stop:
            raise StopIteration  # 超過範圍時停止
        value = self.current
        self.current += self.step
        return value

# 使用 CustomGenerator 類別
gg = CustomGenerator(0, 10, 2)

for item in gg:
    print(item)  # 輸出 0 2 4 6 8
# =============================================================================
# 這個 CustomGenerator 類別允許你指定起始值、結束值和步進值。這樣的擴展讓生成器更加靈活。
# 
# 🧑‍💻 總結：
# 使用類別來實現生成器，實際上是創建自定義的迭代器。
# 
# 通過實現 __iter__() 和 __next__() 方法，讓類別可以像生成器一樣使用。
# 
# 類別方式可以讓你在生成器中加入更多自定義的邏輯和狀態管理。
# 
# 如果有其他問題，或是想擴展這個範例，隨時告訴我！
# =============================================================================
