from fastapi import FastAPI, Request
from pydantic import BaseModel
from app.memory import load_memory
from app.openai_handler import get_ai_response

app = FastAPI()

class Message(BaseModel):
    user_input: str

@app.post("/chat")
async def chat(message: Message):
    memory = load_memory()
    user_input = message.user_input
    ai_reply = get_ai_response(user_input, memory)
    return {"response": ai_reply}

@app.post("/journal")
async def journal_entry(entry: Message):
    from app.memory import add_memory_event
    add_memory_event(f"Journaled: {entry.user_input}")
    return {"message": "Journal entry saved."}

