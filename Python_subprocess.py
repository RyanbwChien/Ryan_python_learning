# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 12:34:08 2023

@author: G0225
"""


import os


token = ["activate py27_32",r"cd C:\Users\G0225\python project", r"python python_send_Notes_mail.py"]

'&'.join(token)

# r"cd C:\Users\G0225\python project" 路徑有空白 CMD 還是可以讀取

#Method 1
os.system(
         '&'.join(token)
          ) 


#Method 2
os.system(
         r"activate py27_32 & cd C:\Users\G0225\python project & python python_send_Notes_mail.py"
          ) 


commands = """
echo AAA ^BBB ^CCC
"""
os.system(  commands ) 

import subprocess
# =============================================================================
# subprocess.Popen 是 Python 中最靈活、功能最強大的方式之一，用來與外部程式或 shell 進行互動。你可以把它想像成：啟動一個子程序的「完整控制器」。
# 
# 🔧 功能一覽（你可以做到這些）：
# 功能	說明
# ✅ 啟動外部指令	跑任意 shell / 可執行檔
# ✅ 控制標準輸入 / 輸出 / 錯誤	可以把資料送進 stdin、接收 stdout、stderr
# ✅ 非同步執行	不會卡住主程式，可搭配 .poll()、.wait()
# ✅ 可寫可讀（互動式）	可以邊寫入邊讀出，像與一個 CLI 工具對話
# ✅ 可以與管線 / 多個子程序一起運作	Popen(..., stdout=PIPE) 串接管線
# =============================================================================

commands = """
echo AAA \
BBB \
CCC \
"""

subprocess.run(commands, shell=True)

import subprocess

commands = """
echo AAA ^
BBB ^
CCC
"""
result = subprocess.run(["cmd", "/c", "echo hello world"], # ✅ 加上 /c，告訴 cmd：「請執行後面的命令然後離開」
               
               capture_output=True,   # 抓住 stdout / stderr
               text=True              # 自動解碼為文字
               )

print("輸出：", result.stdout)
print("錯誤：", result.stderr)
print("回傳碼：", result.returncode)


result = subprocess.run(["python", "-c", "print('TESTING')"], # python -c "print('hello')" 是 Python 官方參數，用來直接執行一段 Python 程式碼。
               
               capture_output=True,   # 抓住 stdout / stderr
               text=True              # 自動解碼為文字
               )

print("輸出：", result.stdout)
print("錯誤：", result.stderr)
print("回傳碼：", result.returncode)

# -c 是 Python 的命令行選項，用來指定你要直接執行的一段 Python 程式碼。
# =============================================================================
# C:\Users\user>python --help
# usage: python [option] ... [-c cmd | -m mod | file | -] [arg] ...
# Options (and corresponding environment variables):
# -b     : issue warnings about converting bytes/bytearray to str and comparing
#          bytes/bytearray with str or bytes with int. (-bb: issue errors)
# -B     : don't write .pyc files on import; also PYTHONDONTWRITEBYTECODE=x
# -c cmd : program passed in as string (terminates option list)
# =============================================================================

#%%
import subprocess

# =============================================================================
# 運作過程：
# command = ["echo", "AAA"]：command 是一個列表，分別包含 echo 和 AAA 兩個元素。
# shell=True：這告訴 subprocess 使用 shell（例如 cmd.exe 或 bash）來執行命令。
# 問題：如果傳遞的是列表並且使用 shell=True，它會把 echo 當作一個獨立的命令，再把 AAA 當作另外一個參數傳遞給 echo。這樣會導致錯誤或無法正常執行，因為它期望的是一個完整的命令字串，而不是分開的命令和參數。
# =============================================================================

commands = ["AAA", "BBB","CCC"]

# 啟動外部命令
for command in commands:
    with subprocess.Popen(
        ["echo", command],        # 或直接給字串，搭配 shell=True
        stdout=subprocess.PIPE,         # 擷取輸出
        stderr=subprocess.PIPE,         # 擷取錯誤
        stdin=subprocess.PIPE,          # 可寫入 stdin（互動）
        text=True,                       # 自動文字編碼，不然會是 bytes
        shell=True,   # 用 shell 來跑，才能使用 echo
    ) as p:

        out, err = p.communicate()          # 等待並擷取輸出
        print("輸出：", out)

#%%
import subprocess

# 啟動外部命令
p = subprocess.Popen(
    ["echo", "hello world"],        # 或直接給字串，搭配 shell=True
    stdout=subprocess.PIPE,         # 擷取輸出
    stderr=subprocess.PIPE,         # 擷取錯誤
    stdin=subprocess.PIPE,          # 可寫入 stdin（互動）
    text=True,                       # 自動文字編碼，不然會是 bytes
    shell=True,   # 用 shell 來跑，才能使用 echo
)

out, err = p.communicate()          # 等待並擷取輸出
print("輸出：", out)

#%%

import subprocess

p = subprocess.Popen(
    ["cmd", "/c", "echo hello world"],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True
)

out, err = p.communicate()
print("輸出：", out)

#%% 寫一個 Pipeline

p1 = subprocess.Popen(["echo", "hello world"], stdout=subprocess.PIPE, text=True, shell=True)
p2 = subprocess.Popen(["findstr", "hello"], stdin=p1.stdout, stdout=subprocess.PIPE, text=True, shell=True)
p1.stdout.close()  # 必要！避免死鎖
output = p2.communicate()[0]

print("結果：", output)


#%%

import subprocess

commands = [
    "echo AAA",
    "echo BBB",
    "echo CCC"
]

# 啟動 cmd 並傳送多行命令
with subprocess.Popen(
    ["cmd", "/c"] + commands, # ['cmd', '/c', 'echo AAA', 'echo BBB', 'echo CCC']
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True
) as proc:
    out, err = proc.communicate()

print("輸出：", out)
print("錯誤：", err)
