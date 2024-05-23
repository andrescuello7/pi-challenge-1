import os
import bcrypt

from jwt import encode
from fastapi import HTTPException, status
from models.user_model import UserModel

def create_auth(db, req):
    '''
    Query for Add in the table UserModel database
    '''
    if db and req:
        user = db.query(UserModel).filter_by(user_name=req.user_name).first()
        if user:
            if not bcrypt.checkpw(
                req.password.encode('utf-8'), user.password.encode('utf-8')
            ):
                raise HTTPException(401, detail="passwords do not match")

            token = encode({
                'user': {
                    'id': user.id,
                    'role': user.role,
                    'full_name': user.full_name,
                    'user_name': user.user_name,
                    'photo': user.photo
                }
            }, os.getenv('JWT_SECRET'), algorithm='HS256')
        return {'x-auth-token': token}
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
            detail="database or model user null")
