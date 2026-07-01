import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")


def review_code(code):

    prompt = f"""
You are a Senior Python Code Reviewer.

Review the following Python code.

Look for:
- Bugs
- Security issues
- Performance improvements
- Best practices
- Code readability

Return the improved version of the code.

Code:

{code}
"""

    print("Reviewing Code...")

    response = model.generate_content(prompt)

    print("Review Completed")

    return response.text