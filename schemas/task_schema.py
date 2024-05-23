from pydantic import BaseModel

class task_schema(BaseModel):
    id: int
    state: int
    title: str
    description: str
    user_id: int
