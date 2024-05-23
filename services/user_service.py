from fastapi import HTTPException, status
from models.user_model import UserModel
from utils.bcrypt import hash_password


def get_all(db):
    '''
    Query of database in the table UserModel to get all
    '''
    if db:
        response = db.query(UserModel).all()
        return response
    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="find all users in database"
        )


def create_new_user(db, req):
    '''
    Query for Add in the table UserModel database
    '''
    if db and req:
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
    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="database or model user null"
        )


def update_user(db, user_id, req):
    '''
    Query for UPDATE in the table UserModel in the database
    Identify for user_id
    '''
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
    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="udpate user, in get datos for update"
        )


def delete_user(db, user_id):
    '''
    Query for DELETE a user in the table UserModel in the database
    Identify for user_id
    '''
    if user_id:
        user = db.query(UserModel).filter_by(id=user_id).first()
        db.delete(user)
        db.commit()
        return user
    else:
        raise HTTPException(
            status_code=status.HTTP_400_INTERNAL_SERVER_ERROR,
            detail="user_id null"
        )
