# AI RPG Content Engine (Structured Version)

## Overview
This project generates structured RPG content such as quests, NPCs, items, and lore using NLP.

## Features
- Structured output (Title, Objective, etc.)
- Parameter control (temperature, seed)
- FastAPI backend
- Clean modular design

## Run
pip install -r requirements.txt  
uvicorn main:app --reload  

Open:
http://127.0.0.1:8000/docs

## Example Input
{
  "type": "quest",
  "genre": "dark fantasy",
  "mood": "mysterious",
  "difficulty": "hard",
  "temperature": 0.7
}

## Output Style
Title  
Objective  
Location  
Enemy/Boss  
Reward  
Twist  

## Why Structured Output
- Easier to read  
- Game-ready format  
- Better for developers  

## Future Improvements
- Better models
- UI integration
