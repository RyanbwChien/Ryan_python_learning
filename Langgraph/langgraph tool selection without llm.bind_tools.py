from langgraph.graph import StateGraph, END
from langchain_core.runnables import RunnableLambda
from langchain_ollama import ChatOllama
from typing import TypedDict
import re

# 初始化模型
llm = ChatOllama(model="llama3.1:8b")

# 定義狀態 schema
class MyState(TypedDict):
    question: str
    llm_response: str
    result: str

# 工具函式
def double(x): return x * 2
def triple(x): return x * 3

tools = {
    "double": double,
    "triple": triple
}

# 節點1: LLM 根據輸入決定要用哪個工具
def thought_action_node(state: MyState) -> MyState:
    question = state["question"]
    response = llm.invoke(    f"""你是一個工具選擇器，只需要從輸入中擷取一個工具名稱（double 或 triple）和一個數字。
不要自己計算，只要找出要用的工具以及原始輸入的數字，格式為：
Use tool: <tool_name> with input <number>

問題：{question}
請依照格式回覆：
""")
    return {**state, "llm_response": response.content}

# 節點2: 根據回應執行對應工具
def make_execute_tool_node(tools: dict):
    def execute_tool_node(state: MyState) -> MyState:
        response = state["llm_response"]
        match = re.match(r"Use tool: (\w+) with input (\d+)", response)
        if match:
            tool_name, value = match.group(1), int(match.group(2))
            tool_func = tools.get(tool_name)
            if tool_func:
                result = tool_func(value) # 這裡就是呼叫函式 帶入 由一開始thought_action_node 所找到的值 Use tool: <tool_name> with input <number> 得到結果
                return {**state, "result": str(result)}
        return {**state, "result": "Invalid tool or format."}
    return execute_tool_node

# 建立 StateGraph，記得加入 schema
workflow = StateGraph(MyState)
workflow.add_node("thought_action", RunnableLambda(thought_action_node))
workflow.add_node("execute_tool", RunnableLambda(make_execute_tool_node(tools)))
workflow.set_entry_point("thought_action")
workflow.add_edge("thought_action", "execute_tool")
workflow.set_finish_point("execute_tool")

# 編譯 workflow
app = workflow.compile()

# 執行範例
result = app.invoke({"question": "請把 4 乘以 3"})
print(result)  # 應該會輸出：{'question': ..., 'llm_response': ..., 'result': '8'}
