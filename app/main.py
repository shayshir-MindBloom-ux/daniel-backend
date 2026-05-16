from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class ChatRequest(BaseModel):
    user_id: str
    message: str


@app.get("/")
def root():
    return {"status": "Daniel backend running"}


@app.post("/chat")
def chat(req: ChatRequest):
    return {
        "response": "Hello from Daniel",
        "state": "stable"
    }