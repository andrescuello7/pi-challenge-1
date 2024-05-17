from pydantic import BaseModel
from typing import Optional

class UserSchema(BaseModel):
    id: int
    photo: str
    user_name: str
    full_name: str
    password: str
    role: Optional[int]
