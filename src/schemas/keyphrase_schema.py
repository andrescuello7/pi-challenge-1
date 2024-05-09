from pydantic import BaseModel

# Schema for endpoints for characters methods http
class KeyphraseSchema(BaseModel):
    id: int
    user_id: int
    keyphrase: str
