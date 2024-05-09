from fastapi import APIRouter

from starlette.responses import RedirectResponse
from src.schemas.question_schema import QuestionSchema
from src.orc.orchestrator import get_answer
from enums.routes_enum import RoutesEnum
from interfaces.i_request import RequestResponse

router = APIRouter()
path = RoutesEnum()
requestResponse = RequestResponse()

# Route '/' redirect for swagger
@router.get("/")
def main():
    return RedirectResponse(url="/docs/")

# Delete Character for ID of url parameter
@router.post(path.gpt_quetions)
def gpt_quetions(req: QuestionSchema):
    try:
        response = get_answer({"question": req.question})
        return {"message": response["answer"]}
    except Exception as e:
        return {"error": str(e)}
