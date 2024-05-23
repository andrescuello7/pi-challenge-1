from pydantic import BaseModel

class eye_color_schema(BaseModel):
    id: int
    color: str
