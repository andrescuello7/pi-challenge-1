from fastapi import APIRouter, status, HTTPException
from fastapi.params import Depends
from models.keyphrase_model import KeyphraseModel
from models.character_model import CharacterModel
from schemas.keyphrase_schema import keyphrase_schema
from services.orchestrator import get_answer
from db_config import session, get_db

router = APIRouter()


@router.get('/api/keyphrase/{text}')
def gpt_quetions(text: str):
    try:
        response = get_answer({"question": text})["answer"]
        response = response.split('\n- ')
        response[0] = response[0].replace('- ', '')
        return {"response": response}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Error: gpt quetions: {str(e)}",
        )


@router.get('/api/keyphrase/character_id/{user_id}')
def gpt_find_quetions(user_id: int, db: session = Depends(get_db)):
    _result = []
    try:
        _query = db.query(KeyphraseModel).filter_by(user_id=user_id).all()

        for item in _query:
            new_item = item.keyphrase.split('\n- ')
            new_item[0] = new_item[0].replace('- ', '')
            _result.append(new_item)

        return {"response": _result}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Error: find gpt quetions: {str(e)}",
        )


@router.post('/api/keyphrase')
def gpt_post_quetions(req: keyphrase_schema, db: session = Depends(get_db)):
    try:
        if req.user_id:
            _user = db.query(CharacterModel).filter_by(
                id=req.user_id).first()

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
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Error: not identify in the frase: {str(e)}",
        )
