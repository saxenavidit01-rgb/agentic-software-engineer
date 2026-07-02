from services.gemini_service import ask_gemini


def generate_code(plan):

    prompt = f"""
Generate a simple FastAPI application for this task:

{plan[:1500]}

Return only Python code.
"""

    print("Calling Gemini Coder...")

    return ask_gemini(prompt)