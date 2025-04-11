# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 14:20:03 2025

@author: user
"""

import nest_asyncio
nest_asyncio.apply()

import asyncio
import time

# =============================================================================
# ⚠️ 缺點：這樣會佔用 CPU！
# 這種寫法會不停用 while 檢查時間是否到了，相當於 busy-waiting（忙等）。這會耗費 CPU 資源，不是真正的非同步行為。
# =============================================================================

class MySleep:
    def __init__(self, delay):
        self.delay = delay

    def __await__(self):
        start = time.time()
        # 我們模擬非同步行為，但實際是輪詢直到時間過去
        while time.time() - start < self.delay:
            # ⏳ 這個 while loop 表示「還沒過完指定秒數」
            # 這邊的邏輯是：「只要經過的時間還沒達到 delay，就繼續 loop」。
            
            
            # 將控制權交回 event loop，下一次再繼續
            yield  # 等效於 asyncio.sleep(0)  關鍵！這行 yield 是把控制權交回給 event loop
        return None

class MyAwaitable:
    def __await__(self):
        print("自定義 await 開始")
        yield from MySleep(1).__await__()
        print("做完步驟 1")
        yield from MySleep(1).__await__()
        print("做完步驟 2")
        return "自定義完成"

async def main():
    result = await MyAwaitable()
    print("結果：", result)

asyncio.run(main())


#%%
import time
async def dosomething(x):
    time.sleep(2)
    return x * 2

async def main2():
    result = await dosomething(10)
    print(result)  # 👉 20

# Notebook 或支援 await 的環境可以直接這樣跑
async def main():
    tasks = [main2 for i in range(5)]  # 建立所有異步任務
    await asyncio.gather(*tasks)  # 正確地等待所有協程完成
    
if __name__ == "__main__":
    start = time.time()
    asyncio.run(main())  # 使用 asyncio.run() 執行 main 協程
    print(f"time: {time.time() - start:.2f} (s)")
        
    
#%%
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


async def my_sleep(duration):
    loop = asyncio.get_running_loop()
    future = loop.create_future()
    loop.call_later(duration, future.set_result, None)  # 設定 `duration` 秒後完成
    await future  # 等待 future 完成，模擬非同步 sleep

async def dosomething(i):
    print(f"第 {i} 次開始")
    await my_sleep(i)  # 用我們自己寫的 my_sleep
    print(f"第 {i} 次結束")

async def main():
    tasks = [dosomething(i+1) for i in range(5)]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    import time
    start = time.time()
    asyncio.run(main())
    print(f"time: {time.time() - start:.2f} (s)")
    
    
    
    
# =============================================================================
# 對的，你理解得很正確！當程式執行到 await asyncio.sleep(3) 時，await asyncio.sleep(3) 並不會阻止 func1() 執行，反而是讓 func1() 停止執行，並且讓出控制權給事件迴圈，這樣可以執行其他協程，例如 func2()。
# 
# 讓我們更具體地說明一下這個過程。
# 
# 詳細過程：
# 執行到 await asyncio.sleep(3)：
# 
# 當程式執行到 await asyncio.sleep(3) 時，這個 await 會被執行，並讓事件迴圈開始等待 3 秒鐘。這裡的 await 並不會讓 func1() 阻塞，這只是告訴事件迴圈：「在 3 秒鐘後再回來繼續執行 func1()」。
# 
# 讓出控制權給事件迴圈：
# 
# 在 await 處，func1() 的執行會暫停，並且事件迴圈會開始執行其他還沒有進入 await 的協程。此時，事件迴圈會去執行 func2() 和 func3()。
# 
# 事件迴圈執行其他協程：
# 
# 因為 func2() 和 func3() 也有 await，但它們的等待時間可能不一樣（例如 func2() 只需等待 1 秒），事件迴圈會根據各協程的等待時間來安排它們的執行。
# 
# 執行順序：
# 
# 事件迴圈會並行地執行 func2() 和 func3()，直到它們的等待時間結束。當 func2() 等待 1 秒後完成時，事件迴圈會繼續執行 func3()。
# 
# 當 await asyncio.sleep(3) 的 3 秒鐘結束後，func1() 會繼續執行並完成。
# 
# 回答你的問題：
# await asyncio.sleep(3) 會被 "執行" 並且讓出控制權執行 func2：
# 
# 是的，await asyncio.sleep(3) 是被執行的，並且它會讓出控制權給事件迴圈。 當事件迴圈控制權轉到其他協程（如 func2() 和 func3()），它們也會執行直到它們的等待完成。而 func1() 會在等待的 3 秒鐘後繼續執行。    
#     
#     
#     
#     
#     
#     
# =============================================================================

#%%

# =============================================================================
# 🔍 控制權交出後，何時繼續執行？
# 📌 這取決於三件事：
# 你 await 的東西什麼時候完成？
# 比如 pyfetch() 是發送 HTTP 請求，那就要等伺服器回應。
# 
# Event loop 有沒有空？
# 
# 如果 event loop 裡有大量任務，它會根據排程順序「輪流」喚醒各個 coroutine。
# 
# 所以有可能你 await 的東西完成了，但 coroutine 還得等一下才排到你。
# 
# I/O、CPU、網路條件
# 
# pyfetch 涉及網路延遲，可能是 0.1 秒也可能是 3 秒。
# 
# 還可能遇到伺服器慢、丟包、DNS 等問題。
# 
# =============================================================================

import asyncio

async def taskA():
    print("A: 開始")
    await asyncio.sleep(0.00000000001)
    print("A: 結束")

async def taskC():
    print("C: 開始")      # 🧠 還沒 await，就會先執行
    await asyncio.sleep(0.5)
    print("C: 結束")

async def main():
    await asyncio.gather(taskA(), taskC())

asyncio.run(main())

# =============================================================================
# 對對對！你這個實驗做得超棒 🎯 這輸出正好說明了我們剛剛的討論邏輯！來，我幫你完整解析這段發生了什麼：
# 
# 💡 程式碼簡析：
# 
# async def taskA():
#     print("A: 開始")
#     await asyncio.sleep(0.00000000001)  # 幾乎等於立即完成
#     print("A: 結束")
# 
# async def taskC():
#     print("C: 開始")
#     await asyncio.sleep(0.5)
#     print("C: 結束")
# 
# await asyncio.gather(taskA(), taskC())
# 🧠 執行順序拆解：
# asyncio.gather(taskA(), taskC()) 被呼叫，taskA 與 taskC 同時啟動 coroutine。
# 
# event loop 先把 taskA() 和 taskC() 放進排程，兩個都「剛啟動」。
# 
# 因為他們都還沒到 await，所以會馬上開始跑他們的「同步開場段」。
# 
# taskA() → print("A: 開始")
# 
# taskC() → print("C: 開始")
# 
# 然後：
# 
# taskA() 遇到 await asyncio.sleep(0.00000000001)，把控制權交出去
# 
# taskC() 也遇到 await asyncio.sleep(0.5)，也交出去
# 
# 💥 但關鍵來了：
# asyncio.sleep(0.00000000001) 幾乎是 馬上完成的延遲，所以 taskA() 幾乎會立即被喚醒
# 
# event loop 下一輪檢查 ready queue，看到 taskA() 準備好了，就先執行它後半段 → print("A: 結束")
# 
# taskC() 的 sleep 還沒滿 0.5 秒，要等一段時間才會喚醒，所以它要「之後」才執行 print("C: 結束")
# 
# ✅ 最終輸出：
# vbnet
# 複製
# 編輯
# A: 開始     <-- taskA 還沒 await，先執行開場段
# C: 開始     <-- taskC 還沒 await，接著執行開場段
# A: 結束     <-- sleep 超短，幾乎立刻回來
# C: 結束     <-- sleep 0.5 秒後回來
# 🎓 小結：
# 階段	說明
# print()	都在 await 前，會同步執行
# await	將控制權交給 event loop
# 哪個先繼續	看誰 await 的結果先完成
# 為什麼 A 快	A 的 sleep 幾乎為零，幾乎立刻完成
# =============================================================================
