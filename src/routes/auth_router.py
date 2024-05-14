import os
import bcrypt
from jwt import encode, decode

from fastapi import APIRouter, Depends, Header, HTTPException
from fastapi.params import Depends, Depends
from fastapi import HTTPException

from src.config.database import Session, get_db
from enums.http_enum import HttpStatus

from src.models.user_model import UserModel
from src.schemas.auth_schema import AuthSchema

from enums.routes_enum import RoutesEnum
from interfaces.i_request import RequestResponse
from utils.auth import auth_token

router = APIRouter()
path = RoutesEnum()
requestResponse = RequestResponse()
AUTH = os.getenv('JWT_SECRET') or 'ADMIN'

# Get for all eye_colors
@router.get(path.get_auth)
def get_auth(authorization: str = Header(...), db: Session = Depends(get_db)): # type: ignore
    try: 
        response = auth_token(authorization)
        return response
    except Exception as e:
        return requestResponse.error(f"authorization, detail: {e}", HttpStatus.UNAUTHORIZED)

# Create Character with model of schema
@router.post(path.post_auth)
def create_auth(req: AuthSchema, db: Session = Depends(get_db)): # type: ignore
    try:
        user = db.query(UserModel).filter_by(user_name=req.user_name).first()
        if user:
            if not bcrypt.checkpw(req.password.encode('utf-8'), user.password.encode('utf-8')):
                raise HTTPException(HttpStatus.UNAUTHORIZED, detail="passwords do not match")

            payload = {
                'user': {
                    'id': user.id,
                    'role': user.role,
                    'full_name': user.full_name,
                    'user_name': user.user_name,
                    'photo': user.photo
                }
            }

            token = encode(payload, AUTH, algorithm='HS256')
        return {'x-auth-token': token}
    except Exception as e:
        return requestResponse.error(e, HttpStatus.UNAUTHORIZED)