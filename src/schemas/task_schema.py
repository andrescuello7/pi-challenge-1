from pydantic import BaseModel
from typing import Optional

# Schema for endpoints for characters methods http
class TaskSchema(BaseModel):
    id: int
    state: int
    title: str
    description: str
    user_id: int