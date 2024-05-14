from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from src.schemas.eye_color_schema import EyeColorSchema

# Schema for Character with endpoint id body schema
class CharacterSchema(BaseModel):
    id: int
    name: str
    height: float
    mass: float
    hair_color: str
    skin_color: str
    eye_color_id: Optional[int]
    eye_color: EyeColorSchema
