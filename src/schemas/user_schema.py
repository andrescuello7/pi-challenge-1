from pydantic import BaseModel
from typing import Optional

# Schema for Users with endpoint id body schema
class UserSchema(BaseModel):
    id: int
    photo: str
    user_name: str
    full_name: str
    password: str
    # Optional role or null if no role
    role: Optional[int]
