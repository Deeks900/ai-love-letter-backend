from fastapi import FastAPI
import os
from dotenv import load_dotenv
from schemas import LetterRequest, emotion_description
from llm import call_llm
from datetime import date
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_valentine_day():
    today = date.today()
    valentine_days = {
        7: "Rose Day 🌹",
        8: "Propose Day 💍",
        9: "Chocolate Day 🍫",
        10: "Teddy Day 🧸",
        11: "Promise Day 🤞",
        12: "Hug Day 🤗",
        13: "Kiss Day 💋",
        14: "Valentine’s Day ❤️"
    }

    if today.month == 2 and today.day in valentine_days:
        return valentine_days[today.day]
    return "Valentine season"

# ---------- API Endpoint ----------
@app.post("/generate-letter")
def generate_letter(data: LetterRequest):
    emotion = emotion_description(data.emotion_level)
    valentine_day = get_valentine_day()

    prompt = f"""
Write a heartfelt love letter from {data.sender_name} to {data.receiver_name}.

IMPORTANT RULES:
- Address the receiver directly using their name: "{data.receiver_name}"
- DO NOT use placeholders like [Name], [Your Name], or generic greetings
- The letter MUST begin by directly addressing {data.receiver_name}

Today is {valentine_day}.
Subtly and naturally reference this in the letter.

Relationship type: {data.relationship}
Tone: {data.tone}
Emotion intensity: {emotion}

Language: {data.language}
Important:
- Write naturally in the chosen language (not a literal translation)
- Make it sound human and emotional
- Avoid clichés
- Length: 150–250 words
"""

    response = call_llm(prompt)

    letter_text = response.text
    return {
        "letter": letter_text
    }







