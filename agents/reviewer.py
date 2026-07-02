from services.gemini_service import ask_gemini


def review_code(code):

    prompt = f"""
You are a Senior Python Code Reviewer.

Review the following Python code.

If the code is acceptable, start your response with exactly:

STATUS: APPROVED

If the code needs improvement, start your response with exactly:

STATUS: REJECTED

Then explain your reasoning and provide an improved version of the code if needed.

Code:

{code}
"""

    print("Reviewing Code...")
    print("Calling Gemini Reviewer...")

    return ask_gemini(prompt)