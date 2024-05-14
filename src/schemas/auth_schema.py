from pydantic import BaseModel
from typing import Optional

# Schema for Auth with endpoint id body schema
class AuthSchema(BaseModel):
    id: Optional[int]
    user_name: str
    password: str