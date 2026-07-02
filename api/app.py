from fastapi import FastAPI
from dotenv import load_dotenv

from graph.workflow import workflow
from tools.file_tools import save_code
from api.models import TaskRequest, TaskResponse

load_dotenv()

app = FastAPI(
    title="Agentic Software Engineering API",
    description="AI-powered Software Engineering Assistant using LangGraph",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Agentic AI is Running"
    }


@app.post("/generate", response_model=TaskResponse)
def generate(request: TaskRequest):

    result = workflow.invoke(
        {
            "task": request.task,
            "retries": 0
        }
    )

    filepath = save_code(
        "generated_code.py",
        result["review"]
    )

    return TaskResponse(
        plan=result["plan"],
        code=result["code"],
        review=result["review"],
        generated_file=filepath
    )