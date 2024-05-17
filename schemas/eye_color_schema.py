from pydantic import BaseModel

class EyeColorSchema(BaseModel):
    id: int
    color: str
