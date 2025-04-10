# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 14:20:03 2025

@author: user
"""
# =============================================================================
# import asyncio
# async def pp(x):
#     await asyncio.sleep(2)  # 模擬等待兩秒鐘的非同步操作
#     print(2*x)
# 
# async def test():
#     for i in range(5):
#         print(i)
#         pp(i)
#         
# asyncio.run(test())
# 
# =============================================================================


import time
import asyncio

async def dosomething(i):
    print(f"第 {i} 次開始")
    await asyncio.sleep(2)  # 模擬等待 2 秒
    print(f"第 {i} 次結束")

async def main():
    tasks = [dosomething(i+1) for i in range(5)]  # 建立所有異步任務
    await asyncio.gather(*tasks)  # 正確地等待所有協程完成

if __name__ == "__main__":
    start = time.time()
    asyncio.run(main())  # 使用 asyncio.run() 執行 main 協程
    print(f"time: {time.time() - start:.2f} (s)")
    
# =============================================================================
# 🕒 事件發生順序
# 時間	事件
# t=0s	dosomething(1) 開始，印出 "第 1 次開始"，然後 await asyncio.sleep(2) 讓出 CPU
# t=0s	dosomething(2) 開始，印出 "第 2 次開始"，然後 await asyncio.sleep(2) 讓出 CPU
# t=0s	dosomething(3) 開始，印出 "第 3 次開始"，然後 await asyncio.sleep(2) 讓出 CPU
# t=0s	dosomething(4) 開始，印出 "第 4 次開始"，然後 await asyncio.sleep(2) 讓出 CPU
# t=0s	dosomething(5) 開始，印出 "第 5 次開始"，然後 await asyncio.sleep(2) 讓出 CPU
# t=2s	dosomething(1) await asyncio.sleep(2) 完成，印出 "第 1 次結束"
# t=2s	dosomething(2) await asyncio.sleep(2) 完成，印出 "第 2 次結束"
# t=2s	dosomething(3) await asyncio.sleep(2) 完成，印出 "第 3 次結束"
# t=2s	dosomething(4) await asyncio.sleep(2) 完成，印出 "第 4 次結束"
# t=2s	dosomething(5) await asyncio.sleep(2) 完成，印出 "第 5 次結束"
# 總時間	2 秒 ✅
# =============================================================================
    
import asyncio


# =============================================================================
# 這是因為 Python 中的 asyncio 是非同步並發的，而且每個 await 操作會讓程式在等待期間去執行其他的任務，
# 所以程式執行順序不會完全是 1、2、3、4、5。
# 然後，每個 my_sleep(2) 會等 2 秒，當 2 秒結束時，它們的 print(f"第 {i} 次結束") 才會按順序打印出來，
# 但因為是並發執行，所以順序會有所不同。
# =============================================================================


# =============================================================================
# async def my_sleep(duration):
#     loop = asyncio.get_running_loop()
#     future = loop.create_future()
#     loop.call_later(duration, future.set_result, None)  # 設定 `duration` 秒後完成
#     await future  # 等待 future 完成，模擬非同步 sleep
# 
# async def dosomething(i):
#     print(f"第 {i} 次開始")
#     await my_sleep(2)  # 用我們自己寫的 my_sleep
#     print(f"第 {i} 次結束")
# 
# async def main():
#     tasks = [dosomething(i+1) for i in range(5)]
#     await asyncio.gather(*tasks)
# 
# if __name__ == "__main__":
#     import time
#     start = time.time()
#     asyncio.run(main())
#     print(f"time: {time.time() - start:.2f} (s)")
#     
#     
# =============================================================================
    
    
對的，你理解得很正確！當程式執行到 await asyncio.sleep(3) 時，await asyncio.sleep(3) 並不會阻止 func1() 執行，反而是讓 func1() 停止執行，並且讓出控制權給事件迴圈，這樣可以執行其他協程，例如 func2()。

讓我們更具體地說明一下這個過程。

詳細過程：
執行到 await asyncio.sleep(3)：

當程式執行到 await asyncio.sleep(3) 時，這個 await 會被執行，並讓事件迴圈開始等待 3 秒鐘。這裡的 await 並不會讓 func1() 阻塞，這只是告訴事件迴圈：「在 3 秒鐘後再回來繼續執行 func1()」。

讓出控制權給事件迴圈：

在 await 處，func1() 的執行會暫停，並且事件迴圈會開始執行其他還沒有進入 await 的協程。此時，事件迴圈會去執行 func2() 和 func3()。

事件迴圈執行其他協程：

因為 func2() 和 func3() 也有 await，但它們的等待時間可能不一樣（例如 func2() 只需等待 1 秒），事件迴圈會根據各協程的等待時間來安排它們的執行。

執行順序：

事件迴圈會並行地執行 func2() 和 func3()，直到它們的等待時間結束。當 func2() 等待 1 秒後完成時，事件迴圈會繼續執行 func3()。

當 await asyncio.sleep(3) 的 3 秒鐘結束後，func1() 會繼續執行並完成。

回答你的問題：
await asyncio.sleep(3) 會被 "執行" 並且讓出控制權執行 func2：

是的，await asyncio.sleep(3) 是被執行的，並且它會讓出控制權給事件迴圈。 當事件迴圈控制權轉到其他協程（如 func2() 和 func3()），它們也會執行直到它們的等待完成。而 func1() 會在等待的 3 秒鐘後繼續執行。    
    
    
    
    
    
    
    