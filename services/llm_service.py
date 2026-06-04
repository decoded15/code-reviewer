import google.generativeai as genai
import os

from dotenv import load_dotenv

load_dotenv()

genai.configure(
    api_key=os.getenv("GOOGLE_API_KEY")
)

model = genai.GenerativeModel("gemini-2.5-flash")

def stream_review(prompt):

    response = model.generate_content(
        prompt,
        stream=True
    )

    for chunk in response:
        yield chunk.text

