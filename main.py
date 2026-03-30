from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from generator import GameContentGenerator
from utils import build_prompt

app = FastAPI(title="AI RPG Content Engine")

generator = GameContentGenerator()

@app.get("/")
def home():
    return {"message": "AI RPG Content Engine is running"}

class Request(BaseModel):
    type: str
    genre: str
    mood: str
    difficulty: str
    temperature: float = 0.7
    seed: Optional[int] = None

@app.post("/generate")
def generate_content(req: Request):
    prompt = build_prompt(req.type, req.genre, req.mood, req.difficulty)
    result = generator.generate(prompt, temperature=req.temperature, seed=req.seed)
    return {"result": result}
