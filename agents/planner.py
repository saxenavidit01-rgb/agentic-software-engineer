from services.gemini_service import ask_gemini


def create_plan(task):

    prompt = f"""
You are an expert Software Architect.

Break the following task into implementation steps.

Task:
{task}
"""

    return ask_gemini(prompt)