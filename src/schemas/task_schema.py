from pydantic import BaseModel
from typing import Optional

# Schema for TaskS with endpoint id body schema
class TaskSchema(BaseModel):
    id: int
    state: int
    title: str
    description: str
    user_id: int