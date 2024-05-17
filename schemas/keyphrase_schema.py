from pydantic import BaseModel

class KeyphraseSchema(BaseModel):
    id: int
    user_id: int
    keyphrase: str
