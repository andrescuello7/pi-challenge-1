from pydantic import BaseModel

# Schema for Keyphrase with endpoint id body schema
class KeyphraseSchema(BaseModel):
    id: int
    user_id: int
    keyphrase: str
