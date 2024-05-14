from fastapi.params import Depends, Depends
from fastapi import APIRouter, Depends, HTTPException, Header

from src.models.user_model import UserModel
from src.schemas.user_schema import UserSchema
from src.config.database import Session, get_db

from enums.user_enum import UserRole
from enums.http_enum import HttpStatus
from enums.routes_enum import ROUTES_ENUM
from interfaces.i_request import RequestResponse

from utils.auth import auth_token
from utils.bcrypt import hash_password

router = APIRouter()
requestResponse = RequestResponse()

# Get for all eye_colors
@router.get(ROUTES_ENUM.GET_USER)
def get_users(db: Session = Depends(get_db)): # type: ignore
    try: 
        response = db.query(UserModel).all()
        return response
    except Exception as e:
        return requestResponse.error(f"get all users, detail: {e}", HttpStatus.BAD_REQUEST)
    
# Create Character with model of schema
@router.post(ROUTES_ENUM.POST_USER)
def create_user(req: UserSchema, authorization: str = Header(...), db: Session = Depends(get_db)): # type: ignore
    try:
        user_auth = auth_token(authorization)
        if user_auth['role'] != UserRole().ADMIN:
            raise HTTPException(HttpStatus.BAD_REQUEST, detail='Not authorized')
        
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
        return requestResponse.error(f"create user, detail: {e}", HttpStatus.BAD_REQUEST)

# Create Character with model of schema
@router.put(ROUTES_ENUM.PUT_USER)
def update_task(req: UserSchema, user_id: int, authorization: str = Header(...), db: Session = Depends(get_db)): # type: ignore
    try:
        user_auth = auth_token(authorization)
        if user_auth['role'] != UserRole().ADMIN:
            raise HTTPException(HttpStatus.BAD_REQUEST, detail='Not authorized')
        
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
        return requestResponse.error(f"create user, detail: {e}", HttpStatus.BAD_REQUEST)


# Delete Character for ID of url parameter
@router.delete(ROUTES_ENUM.DELETE_USER)
def delete_character(user_id: int, authorization: str = Header(...), db: Session = Depends(get_db)): # type: ignore
    try:
        user_auth = auth_token(authorization)
        if user_auth['role'] != UserRole().ADMIN:
            raise HTTPException(HttpStatus.BAD_REQUEST, detail='Not authorized')
        
        user = db.query(UserModel).filter_by(id=user_id).first()
        if user:
            db.delete(user)
            
        db.commit()
        return {"message": "User deleted successfully", "user": user}
    except Exception as e:
        return requestResponse.error(f"delete user, detail: {e}", HttpStatus.BAD_REQUEST)
