from pydantic import BaseModel
from typing import Optional

# Schema for Auth with endpoint id body schema
class auth_schema(BaseModel):
    id: Optional[int]
    user_name: str
    password: str
