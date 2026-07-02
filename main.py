from dotenv import load_dotenv

load_dotenv()

from graph.workflow import workflow
from tools.file_tools import save_code

result = workflow.invoke(
    {
        "task": "Build a REST API for employee management",
        "retries": 0
    }
)

print("\n================ FINAL RESULT ================\n")

print(result["review"][:1500])

save_code(
    "generated_code.py",
    result["review"]
)