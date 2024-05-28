from pydantic import BaseModel
from typing import Optional

class user_schema(BaseModel):
    id: int
    photo: str
    user_name: str
    full_name: str
    password: str
    role: Optional[int]
