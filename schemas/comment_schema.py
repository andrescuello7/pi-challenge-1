from pydantic import BaseModel

class comment_schema(BaseModel):
    id: int
    task_id: int
    comment: str
