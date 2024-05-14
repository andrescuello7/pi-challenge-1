from pydantic import BaseModel

# Schema for EyeColor with endpoint id body schema
class EyeColorSchema(BaseModel):
    id: int
    color: str
