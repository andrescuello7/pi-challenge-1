from pydantic import BaseModel

class TaskSchema(BaseModel):
    id: int
    state: int
    title: str
    description: str
    user_id: int