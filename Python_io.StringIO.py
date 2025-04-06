# -*- coding: utf-8 -*-
"""
Created on Sun Apr  6 00:01:45 2025

@author: user
"""
import io
'''
io.StringIO 的最大用途之一是作為 內存中的虛擬文件，這對於需要模擬文件操作但不想涉及磁碟 I/O 的情況非常有用，特別是在測試、資料處理或日常開發中。以下是幾個具體的範例：

1. 模擬文件操作進行單元測試
在單元測試中，我們可能需要測試函數或方法，這些函數通常會讀取或寫入文件。使用 StringIO 可以避免實際創建文件，減少測試過程中的 I/O 時間，並能夠快速清除資料。
'''

# 範例：測試函數寫入和讀取資料
import io

# 模擬函數，將資料寫入文件並讀取
def process_data(data):
    with io.StringIO() as f:
        f.write(data)
        f.seek(0)
        return f.read()

# 測試
data = "Test data"
result = process_data(data)
print(result)  # 輸出: Test data
# 這樣可以確保函數的邏輯正確，而不必實際處理磁碟檔案。

'''
2. 處理 JSON 或 CSV 格式資料
在需要讀寫 JSON 或 CSV 等格式資料時，StringIO 可以用來在內存中處理這些格式，避免了磁碟 I/O，並且能快速測試處理邏輯。
'''
# 範例：使用 StringIO 處理 CSV

import io
import csv

# 模擬 CSV 檔案的字符串
csv_data = "name,age\nAlice,30\nBob,25\n"

# 使用 StringIO 模擬一個檔案
with io.StringIO(csv_data) as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
# =============================================================================
# 輸出：
# ['name', 'age']
# ['Alice', '30']
# ['Bob', '25']
# 這樣你可以在不創建實際文件的情況下處理 CSV 資料。
# =============================================================================

'''
3. 快速處理格式化輸出
在一些情況下，可能會需要將格式化的資料寫入字串中，而不是文件。這在處理日誌、生成報告或串接多個資料來源時非常有用。
'''

# 範例：生成格式化的報告

import io

# 生成一個格式化報告
report = io.StringIO()
report.write("Report:\n")
report.write("Name: Alice\n")
report.write("Age: 30\n")

# 讀取報告內容
report.seek(0)
print(report.read())

'''
4. 處理內存中的大型資料
StringIO 可以用來處理需要在內存中進行大量處理的資料，例如大規模的文字資料分析，或進行批量處理和處理完後的回應。
'''

# 範例：模擬大規模資料處理
import io

# 模擬一個包含多行資料的情況
data = "\n".join([f"Line {i}" for i in range(1, 100000)])

# 使用 StringIO 處理
with io.StringIO(data) as f:
    lines = f.readlines()
    print(f"Processed {len(lines)} lines.")
    
# 這樣可以避免將大量資料寫入磁碟，從而提高處理效率。

'''
總結
io.StringIO 的最大用途是能夠在內存中高效地處理資料，模擬文件操作，特別適用於單元測試、資料格式處理、日誌生成、報告生成等多種場景。它能顯著提高代碼效率，減少磁碟 I/O 操作，並使得開發過程更加靈活
'''