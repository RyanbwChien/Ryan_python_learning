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
    
    
    
    
    
    
    
    
    
    