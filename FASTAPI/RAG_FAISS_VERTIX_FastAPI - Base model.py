import os
import re
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.prompts.chat import ChatPromptTemplate, HumanMessagePromptTemplate, SystemMessagePromptTemplate
from langchain_openai import ChatOpenAI
from langchain.chains import RetrievalQA
from pathlib import Path

# 初始化 FastAPI
app = FastAPI(title="RAG Chat API", description="使用 FAISS 進行檢索增強生成 (RAG) 的 API 服務", version="1.0")

# 載入 FAISS
model_path = Path(__file__).parent / "faiss_index_dir"
embeddings = HuggingFaceEmbeddings(model_name="BAAI/bge-base-zh")
db = FAISS.load_local(model_path, embeddings, allow_dangerous_deserialization=True)


access_token = os.getenv("LINE_ACCESS_TOKEN")
GPT_SYS_PROMPT = os.getenv("GPT_SYS_PROMPT","你是一名人工智慧助理，專職於反詐騙服務領域，使用以下上下文請簡短回答用戶的問題並控制字數在100以內：")
# 設置 Prompt
system_template = f"""{GPT_SYS_PROMPT}                   
----------------"""+"""{context}"""
human_template = "{question}"

messages = [
    SystemMessagePromptTemplate.from_template(system_template),
    HumanMessagePromptTemplate.from_template(human_template),
]

qa_prompt = ChatPromptTemplate.from_messages(messages)

# 設置 LLM 和 Retriever
retriever = db.as_retriever(search_kwargs={"k": 10, "score_threshold": 0.5})

openai_api_key = os.getenv("OPENAI_API_KEY")
if not openai_api_key:
    raise ValueError("Missing OpenAI API key. Please set the OPENAI_API_KEY environment variable.")
llm = ChatOpenAI(model="gpt-4o", api_key=os.environ["openai_apikey"])

qa = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=retriever,
    verbose=False,
    chain_type_kwargs={"verbose": False, "prompt": qa_prompt},
)

# 輔助函數：清理輸入文字
def preprocess_text(text):
    text = re.sub(r"<br\s*/?>", ". ", text)  # 移除 HTML `<br>` 標籤
    text = re.sub(r"\s+", " ", text.strip())  # 清理多餘空格
    return text

# 定義 API 請求格式
class QueryRequest(BaseModel):
    question: str
query = QueryRequest(question="What is the weather today?")
type(query)
print(query)
# API 端點
@app.post("/query")
async def query_rag(request: QueryRequest):
    try:
        question = preprocess_text(request.question)
        response = qa.run(question)
        return {"question": request.question, "answer": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# 啟動服務（開發模式）
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)#, host="0.0.0.0", port=8080