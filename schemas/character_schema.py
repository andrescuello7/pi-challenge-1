from pydantic import BaseModel
from typing import Optional
from schemas.eye_color_schema import eye_color_schema

class character_schema(BaseModel):
    id: int
    name: str
    height: float
    mass: float
    hair_color: str
    skin_color: str
    eye_color_id: Optional[int]
    eye_color: eye_color_schema
