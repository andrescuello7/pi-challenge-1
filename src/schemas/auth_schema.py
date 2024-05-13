from pydantic import BaseModel
from typing import Optional

# Schema for endpoints for characters methods http
class AuthSchema(BaseModel):
    id: Optional[int]
    user_name: str
    password: str