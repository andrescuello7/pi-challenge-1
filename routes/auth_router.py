import os
import bcrypt

from jwt import encode
from fastapi import HTTPException
from fastapi.params import Depends
from fastapi import APIRouter, Header, HTTPException, status
from schemas.auth_schema import auth_schema
from models.user_model import UserModel
from db_config import session, get_db
from utils.auth import auth_token
from services import auth_service as controller

router = APIRouter()

@router.get('/api/auth/user')
def get_auth(authorization: str = Header(...)):
    try:
        response = auth_token(authorization)
        return response
    except Exception as e:
        return {'error': f'user not authenticated, details: {str(e)}'}

@router.post('/api/auth/user')
def create_auth(
    req: auth_schema,
    db: session = Depends(get_db)):
    try:
        response = controller.create_auth(db, req)
        return response
    except Exception:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, detail="user not authenticated}")
