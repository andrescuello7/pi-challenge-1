from fastapi import APIRouter, Depends, HTTPException, Header
from fastapi.params import Depends, Depends

from datetime import datetime
from src.config.database import Session, get_db
from enums.http_enum import HttpStatus
from enums.user_enum import UserRole

from src.models.user_model import UserModel
from src.models.task_model import TaskModel
from src.schemas.task_schema import TaskSchema

from enums.routes_enum import ROUTES_ENUM
from interfaces.i_request import RequestResponse

from utils.auth import auth_token

router = APIRouter()
requestResponse = RequestResponse()

# Get for all eye_colors
@router.get(ROUTES_ENUM.GET_TASKS)
def get_users(db: Session = Depends(get_db)): # type: ignore
    try: 
        _list = []
        response = db.query(TaskModel).all()
        for task in response:
            user = db.query(UserModel).filter_by(id=task.user_id).first()
            if user:
                _list.append({'user': user, 'task': task})

        return _list
    except Exception as e:
        return requestResponse.error(f"get all tasks, detail: {e}", HttpStatus.BAD_REQUEST)

# Get for all eye_colors
@router.get(ROUTES_ENUM.GET_TASK_BY_ID)
def get_users(user_id: int, db: Session = Depends(get_db)): # type: ignore
    try: 
        response = db.query(TaskModel).filter_by(user_id=user_id).all()
        return response
    except Exception as e:
        return requestResponse.error(f"find tasks, detail: {e}", HttpStatus.BAD_REQUEST)
    
# Create Character with model of schema
@router.post(ROUTES_ENUM.POST_TASKS)
def create_user(req: TaskSchema, authorization: str = Header(...), db: Session = Depends(get_db)): # type: ignore
    try:
        user_auth = auth_token(authorization)
        if user_auth:
            model = TaskModel(
                state=req.state,
                title=req.title,
                user_id=user_auth['id'],
                description=req.description,
            )
            db.add(model)
            db.commit()
            db.refresh(model)
        
        return model
    except Exception as e:
        return requestResponse.error(f"create user, detail: {e}", HttpStatus.BAD_REQUEST)

# Create Character with model of schema
@router.put(ROUTES_ENUM.PUT_TASKS)
def update_task(task_id: int, req: TaskSchema, authorization: str = Header(...), db: Session = Depends(get_db)): # type: ignore
    try:
        user_auth = auth_token(authorization)
        if user_auth['role'] != UserRole().ADMIN:
            raise HTTPException(HttpStatus.BAD_REQUEST, detail='Not authorized')
        
        model = db.query(TaskModel).filter_by(id=task_id).first()
        if model:
            model.state = req.state
            model.title = req.title
            model.user_id = req.user_id
            model.update_at = datetime.now()
            model.description = req.description

            db.add(model)
            db.commit()
            db.refresh(model)
    
        return model
    except Exception as e:
        return requestResponse.error(f"create user, detail: {e}", HttpStatus.BAD_REQUEST)

# Create Character with model of schema
@router.patch(ROUTES_ENUM.PATCH_TASKS)
def patch_task(
    task_id: int,
    state: int,
    authorization: str = Header(...),
    db: Session = Depends(get_db)): # type: ignore
    try:
        user_auth = auth_token(authorization)
        if user_auth['role'] != UserRole().ADMIN:
            raise HTTPException(HttpStatus.BAD_REQUEST, detail='Not authorized')
            
        model = db.query(TaskModel).filter_by(id=task_id).first()
        model.state = state
        model.update_at = datetime.now()
        db.add(model)
        db.commit()
        db.refresh(model)

        return model
    except Exception as e:
        return requestResponse.error(f"Update state task, detail: {e}", HttpStatus.BAD_REQUEST)

# Delete Character for ID of url parameter
@router.delete(ROUTES_ENUM.DELETE_TASKS)
def delete_tasks(task_id: int, authorization: str = Header(...), db: Session = Depends(get_db)): # type: ignore
    try:
        user_auth = auth_token(authorization)
        if user_auth['role'] != UserRole().ADMIN:
            raise HTTPException(HttpStatus.BAD_REQUEST, detail='Not authorized')
        
        task = db.query(TaskModel).filter_by(id=task_id).first()
        db.delete(task)
        db.commit()

        return {"message": "Task deleted successfully", "task": task}
    except Exception as e:
        return requestResponse.error(f"delete task, detail: {e}", HttpStatus.BAD_REQUEST)