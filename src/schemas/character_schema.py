from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from src.schemas.eye_color_schema import EyeColorSchema

# Schema for endpoints for characters methods http
class CharacterSchema(BaseModel):
    id: int
    name: str
    height: float
    mass: float
    hair_color: str
    skin_color: str
    eye_color_id: Optional[int]
    eye_color: EyeColorSchema
