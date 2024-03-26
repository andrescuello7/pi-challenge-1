from pydantic import BaseModel
from typing import Optional

class EyeColorSchema(BaseModel):
    id: int
    color: str
