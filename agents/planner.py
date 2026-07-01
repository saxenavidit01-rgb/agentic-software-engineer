import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")


def create_plan(task):
    prompt = f"""
You are an expert Software Architect.

Break the following task into implementation steps.

Task:
{task}
"""

    response = model.generate_content(prompt)
    return response.text