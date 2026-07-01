import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")


def generate_code(plan):

    prompt = f"""
Generate a simple FastAPI application for this task:

{plan[:1500]}

Return only Python code.
"""

    print("Calling Gemini Coder...")

    response = model.generate_content(prompt)

    print("Gemini Coder Response Received")

    return response.text