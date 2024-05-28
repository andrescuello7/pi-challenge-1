from pydantic import BaseModel
from typing import Optional, List

class User(BaseModel):
    id: int
    photo: str
    user_name: str
    full_name: str
    password: str
    role: Optional[int]

class Comment(BaseModel):
    id: int
    task_id: int
    comment: str

class task_schema(BaseModel):
    id: int
    state: int
    title: str
    description: str
    user_id: int
    user: Optional[User]
    comments: List[Comment] = []
