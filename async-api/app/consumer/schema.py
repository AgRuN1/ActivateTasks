from pydantic import BaseModel


class TaskSchema(BaseModel):
    task_id: str
    status: str