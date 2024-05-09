from pydantic import BaseModel

# Schema for endpoints for characters methods http
class QuestionSchema(BaseModel):
    id: int
    question: str
