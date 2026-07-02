from pydantic import BaseModel


class TaskRequest(BaseModel):
    task: str


class TaskResponse(BaseModel):
    plan: str
    code: str
    review: str
    generated_file: str