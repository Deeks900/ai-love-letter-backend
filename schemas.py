from pydantic import BaseModel


# ---------- Request Schema ----------
class LetterRequest(BaseModel):
    sender_name: str
    receiver_name: str
    relationship: str
    tone: str
    emotion_level: int
    language: str


# ---------- Emotion Mapping ----------
def emotion_description(level: int) -> str:
    if level <= 20:
        return "light, playful, and safe"
    elif level <= 40:
        return "sweet and caring"
    elif level <= 60:
        return "romantic and emotionally honest"
    elif level <= 80:
        return "deep, intense, and vulnerable"
    else:
        return "passionate, devoted, and deeply in love"

