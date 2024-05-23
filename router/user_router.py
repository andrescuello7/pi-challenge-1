from fastapi.params import Depends, Depends
from fastapi import APIRouter, Depends, HTTPException, Header
from starlette.responses import RedirectResponse
from enums.user_enum import user_role
from models.user_model import UserModel
from schemas.user_schema import user_schema
from db_config import session, get_db
from utils.auth import auth_token
from utils.bcrypt import hash_password

router = APIRouter()

@router.get("/")
def main():
    return RedirectResponse(url="/docs/")

@router.get('/api/users/getAll')
def get_users(db: session = Depends(get_db)):
    try: 
        response = db.query(UserModel).all()
        return response
    except Exception as e:
        return {'error': f"get all users, detail: {e}"}

@router.post('/api/create/user')
def create_user(
    req: user_schema,
    authorization: str = Header(...),
    db: session = Depends(get_db)):
    try:
        user_auth = auth_token(authorization)
        if user_auth['role'] != user_role().ADMIN:
            raise HTTPException(400, detail='Not authorized')
        response = UserModel(
            photo=req.photo,
            user_name=req.user_name,
            full_name=req.full_name,
            password=hash_password(req.password),
        )
        db.add(response)
        db.commit()
        db.refresh(response)
        return response
    except Exception as e:
        return {'error': f"create user, detail: {e}"}

@router.put('/api/update/user/{user_id}')
def update_task(
    req: user_schema,
    user_id: int,
    authorization: str = Header(...),
    db: session = Depends(get_db)):
    try:
        user_auth = auth_token(authorization)
        if user_auth['role'] != user_role().ADMIN:
            raise HTTPException(400, detail='Not authorized')
        user = db.query(UserModel).filter_by(id=user_id).first()
        if user:
            user.photo = req.photo
            user.user_name = req.user_name
            user.full_name = req.full_name
            user.password = hash_password(req.password)
            user.role = req.role

            db.commit()
            db.refresh(user)
            return user
    except Exception as e:
        return {'error': "update user"}

@router.delete('/api/delete/user/{user_id}')
def delete_character(
    user_id: int,
    authorization: str = Header(...),
    db: session = Depends(get_db)):
    try:
        user_auth = auth_token(authorization)
        if user_auth['role'] != user_role().ADMIN:
            raise HTTPException(400, detail='Not authorized')
        user = db.query(UserModel).filter_by(id=user_id).first()
        if user:
            db.delete(user)
            db.commit()
            return {"message": "User deleted successfully", "user": user}
    except Exception as e:
        return {'error': "delete user"}
