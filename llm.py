from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

# The client gets the API key from the environment variable `GEMINI_API_KEY`.
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
def call_llm(prompt):
    response = client.models.generate_content(
        model="gemini-3-flash-preview", contents=f"{prompt}"
    )
    print(response.text)
    return response