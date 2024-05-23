from pydantic import BaseModel

class keyphrase_schema(BaseModel):
    id: int
    user_id: int
    keyphrase: str
