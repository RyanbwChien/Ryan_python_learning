from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float

@app.post("/items/")
def create_item(item: Item):
    return {"message": f"{item.name} costs {item.price}"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000) #host="0.0.0.0"：這會讓 FastAPI 應用程式監聽所有網路接口的請求
    # uvicorn.run(app, host="127.0.0.1", port=8000)