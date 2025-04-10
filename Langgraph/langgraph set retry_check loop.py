from langgraph.graph import StateGraph, END
from langchain_core.runnables import RunnableLambda
from typing import TypedDict

# ✅ 定義 State Schema
class GraphState(TypedDict, total=False):
    question: str
    response: str
    should_retry: bool
    retry_count: int

# ✅ 模擬 agent
def agent_node(state: GraphState):
    count = state.get("retry_count", 0)
    if count < 3:
        return {"response": "錯誤：缺少資訊"}
    return {"response": "處理完成"}

# ✅ Retry node factory
def make_retry_node(condition_fn, max_retries: int = 3):
    def retry_node(state: GraphState):
        count = state.get("retry_count", 0)
        should_retry = condition_fn(state)
        return {
            "should_retry": should_retry,
            "retry_count": count + 1 if should_retry else count
        }

    def condition_router(state: GraphState):
        if state["should_retry"] and state["retry_count"] < max_retries:
            return "retry"
        else:
            return "end"

    return retry_node, condition_router

# ✅ Retry 條件函數
def should_retry(state: GraphState):
    return "錯誤" in state.get("response", "")

# ✅ 建立節點
retry_node_fn, retry_router = make_retry_node(should_retry, max_retries=2)

# ✅ 建立流程圖
graph = StateGraph(GraphState)
graph.add_node("agent", RunnableLambda(agent_node))
graph.add_node("retry_check", RunnableLambda(retry_node_fn))

graph.set_entry_point("agent")
graph.add_edge("agent", "retry_check")

graph.add_conditional_edges(
    "retry_check",              # 節點名稱
    retry_router,               # ✅ 條件 function（位置參數！）
    {
        "retry": "agent",       # ✅ 條件值對應的下一步節點
        "end": END
    }
)

# 為什麼 retry_router 不需要 add_node()？
# 條件函數的角色：retry_router 只是用來決定在特定條件下轉移到哪個節點。它不會直接執行某些動作或處理資料，而是根據 state 來選擇是否繼續重試，或者結束流程。

# add_conditional_edges 用法：在你的程式中，retry_router 並不是被當作獨立的節點來執行，而是與 retry_check 節點綁定，並用來作為條件來判斷流程的走向。這就像是一個指引流程的「路由器」，在條件滿足時，根據回傳的結果選擇要繼續重試還是結束。

# 條件邏輯與節點分離：retry_router 只處理路由邏輯，並不需要有自己的節點。所有的判斷和邏輯都交由 add_conditional_edges 來管理，這樣可以清晰地分離「邏輯判斷」和「實際動作」的部分。


# ✅ 執行
app = graph.compile()

# for event in app.stream({"question": "請處理這個"}):
#     event["question"].pretty_print()
#     event["response"].pretty_print()
#     event["retry_count"].pretty_print()

from PIL import Image as PILImage
import io
from langchain_core.runnables.graph import MermaidDrawMethod

print(app.get_graph().draw_mermaid())

# result = app.invoke({"question": "請處理這個"})
# png_data = app.get_graph().draw_mermaid_png(draw_method=MermaidDrawMethod.API,timeout=30)
# image = PILImage.open(io.BytesIO(png_data))
# image.show()

# print(result)

