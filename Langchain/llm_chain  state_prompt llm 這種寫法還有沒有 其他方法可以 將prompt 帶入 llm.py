# -*- coding: utf-8 -*-
"""
Created on Tue Apr  8 15:47:42 2025

@author: USER
"""








In addition to using state_prompt | llm, there are other ways to pass a prompt to an LLM. Here are a few alternatives:

1. Use llm.call() method:
You can call the model directly using the call method:

python
複製
編輯
response = llm.call({"input": state_prompt.format(question=question)})
2. Use LLMChain:
Another approach is to use the LLMChain from LangChain. Here's how:

python
複製
編輯
from langchain.chains import LLMChain

chain = LLMChain(llm=llm, prompt=state_prompt)
response = chain.run({"question": question})
This method encapsulates the prompt and LLM into a chain and executes it.

3. Using apply with ChatPromptTemplate:
You can also apply the prompt to the LLM with apply() method:

python
複製
編輯
response = state_prompt.apply({"question": question})
These are some other ways to pass the prompt to the LLM and get a response. Each method can be useful depending on your structure and needs.




llm_chain = state_prompt | llm 這種寫法其實是使用 langchain 中的 管道 (chain) 機制，這個符號 | 被用來連接不同的處理階段，讓 state_prompt 和 llm（LLM 模型）之間形成一個鏈條。這樣，state_prompt 生成的提示會被傳遞到 llm，並產生最終的結果。

但是，除了這種方法，還有其他幾種方式可以將 prompt 帶入 llm，具體取決於你的需求和框架。

1. 直接使用 llm.call 或 llm.invoke
你可以使用 llm 提供的 call 或 invoke 方法來直接執行模型，將 state_prompt 作為輸入傳入。這樣不必依賴管道運行。

範例：
python
複製
編輯
from langchain_core.prompts import ChatPromptTemplate

# 建立提示模板
state_prompt = ChatPromptTemplate.from_template(
    """你需要根據以下所有的資訊來隨機給201、202、203、204、205、206床，每個老人可能拿到相同的狀態
    床位狀態有: ['離床','清醒','呼吸異常','淺睡','深睡']
    呼吸數值: 根據每個狀態來給合理的數值
    睡眠數值: [淺睡時間,淺睡時間比例,深睡時間,深睡時間比例,清醒時間,清醒時間比例,總睡眠時長,睡眠效率]
    使用者問題: {question}
    """
)

# 用 `llm.invoke` 執行並傳遞結果
response = llm.invoke({"question": "如何改善睡眠?"})  # 直接傳遞 prompt 輸入
print(response)
在這個例子中，llm.invoke 方法直接將 prompt 和相關參數傳遞給 llm，並獲得結果。這樣可以避免使用管道運行。

2. 使用 LLMChain
LLMChain 是 langchain 中專門設計來處理 LLM 交互的類，它可以讓你更靈活地處理不同的步驟。

範例：
python
複製
編輯
from langchain.chains import LLMChain
from langchain.prompts import ChatPromptTemplate

# 創建提示模板
state_prompt = ChatPromptTemplate.from_template(
    """請隨機給201、202、203、204、205、206床的每個老人賦予相同狀態，根據使用者問題選擇輸出格式。
    使用者問題: {question}
    """
)

# 用 LLMChain 來包裝模型
llm_chain = LLMChain(prompt=state_prompt, llm=llm)

# 呼叫並獲得結果
response = llm_chain.run({"question": "床位的狀態如何?"})
print(response)
這樣使用 LLMChain 將 state_prompt 和 llm 組合在一起，並能夠簡單調用 .run() 方法來獲取結果。

3. 手動構建完整的 prompt
如果你需要更多的控制權，或者希望將一些邏輯步驟插入到 prompt 生成過程中，你可以手動構建 prompt 並將它傳遞給 llm。

範例：
python
複製
編輯
from langchain.prompts import ChatPromptTemplate

# 手動生成提示
state_prompt = ChatPromptTemplate.from_template(
    """根據以下資料隨機生成一個床位狀態和呼吸睡眠數值，根據使用者問題選擇對應輸出格式。
    使用者問題: {question}
    """
)

# 手動生成提示的具體內容
prompt_text = state_prompt.format(question="床位狀態")

# 呼叫 `llm` 並傳遞已經構建的 `prompt_text`
response = llm.invoke({"question": prompt_text})
print(response)
這種方式讓你對生成的 prompt 有更多控制權，尤其是在需要多步處理或動態改變 prompt 的情況下。

4. 使用 langchain 的 Chain 類
Chain 是 langchain 的基礎類，可以用來組合不同的處理步驟，這樣你可以將 prompt 和其他處理邏輯封裝在一起。

python
複製
編輯
from langchain.chains import SimpleChain
from langchain_core.prompts import ChatPromptTemplate

# 這裡手動生成 prompt 並定義 Chain
state_prompt = ChatPromptTemplate.from_template(
    """床位狀態有: ['離床','清醒','呼吸異常','淺睡','深睡']。請根據使用者問題顯示相關結果。
    使用者問題: {question}
    """
)

# 自定義 Chain，並將 prompt 和 LLM 結合
class MyChain(SimpleChain):
    def _call(self, inputs):
        prompt_text = state_prompt.format(question=inputs["question"])
        return llm.invoke({"question": prompt_text})

# 呼叫 Chain
my_chain = MyChain()
response = my_chain({"question": "狀態為何?"})
print(response)
這樣，你就可以將 prompt 和 LLM 模型處理邏輯封裝在一個自定義的 Chain 類中，進一步提高代碼的可擴展性。

總結：
管道寫法 (|) 是 langchain 中的一個簡潔方式，用來鏈接不同的處理階段。

可以使用 llm.invoke 或 llm.call 直接執行，無需使用管道。

LLMChain 是一個方便的方式，將 prompt 和 llm 包裝成一個可重用的處理流程。

手動生成提示並傳遞給 llm 可以提供更多靈活性，適合需要自定義處理的場景。

根據你的需求選擇不同的方式，可以讓你的工作流程更加清晰和可擴展。