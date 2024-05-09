from fastapi import APIRouter
from fastapi.params import Depends, Depends
from starlette.responses import RedirectResponse

from enums.routes_enum import RoutesEnum
from enums.http_enum import HttpStatus

from src.models.keyphrase_model import KeyphraseModel
from src.models.character_model import CharacterModel
from src.schemas.keyphrase_schema import KeyphraseSchema

from src.orc.orchestrator import get_answer
from src.config.database import Session, get_db

from interfaces.i_request import RequestResponse

router = APIRouter()
path = RoutesEnum()
requestResponse = RequestResponse()

# Route '/' redirect for swagger
@router.get("/")
def main():
    return RedirectResponse(url="/docs/")

# GET keyphrase
@router.get(path.get_gpt_keyphrase)
def gpt_quetions(text: str):
    try:
        response = get_answer({"question": text})["answer"]
        response = response.split('\n- ')
        response[0] = response[0].replace('- ', '')
        return {"response": response}
    except Exception as e:
        return {"error": str(e)}
    
# GET keyphrase byId
@router.get(path.get_gpt_keyphrase_by_id)
def gpt_quetions(user_id: int, db: Session = Depends(get_db)): # type: ignore
    _result = []
    try:
        _query = db.query(KeyphraseModel).filter_by(user_id=user_id).all()

        for item in _query:
            new_item = item.keyphrase.split('\n- ')
            new_item[0] = new_item[0].replace('- ', '')
            _result.append(new_item)

        return {"response": _result}
    except Exception as e:
        return {"error": str(e)}
    
# POST keyphrase
@router.post(path.post_gpt_keyphrase)
def gpt_quetions(req: KeyphraseSchema, db: Session = Depends(get_db)): # type: ignore
    try:
        if req.user_id:
            _user = db.query(CharacterModel).filter_by(id=req.user_id).first()
            
            if _user:
                result = get_answer({"question": req.keyphrase})["answer"]
                model = KeyphraseModel(
                    user_id=req.user_id,
                    keyphrase=result
                )
                db.add(model)
                db.commit()

                _keyphrase = model.keyphrase.split('\n- ')
                _keyphrase[0] = _keyphrase[0].replace('- ', '')

                return {
                    "response": { 
                        "user": model.user_id,
                        "user_id": _user.name,
                        "keyphrase": _keyphrase
                    }
                }
    except Exception as e:
        return requestResponse.error({"error": 'No se pudo realizar la identiciacion de la frases'}, HttpStatus.NOT_FOUND)
