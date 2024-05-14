from fastapi import APIRouter, Depends, HTTPException, Header
from fastapi.params import Depends, Depends

from datetime import datetime
from src.config.database import Session, get_db
from enums.http_enum import HttpStatus
from enums.user_enum import UserRole

from src.models.user_model import UserModel
from src.models.task_model import TaskModel
from src.schemas.task_schema import TaskSchema

from enums.routes_enum import RoutesEnum
from interfaces.i_request import RequestResponse

from utils.auth import auth_token

router = APIRouter()
path = RoutesEnum()
requestResponse = RequestResponse()

# Get for all eye_colors
@router.get(path.get_tasks)
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
@router.get(path.get_task_by_id)
def get_users(user_id: int, db: Session = Depends(get_db)): # type: ignore
    try: 
        response = db.query(TaskModel).filter_by(user_id=user_id).all()
        return response
    except Exception as e:
        return requestResponse.error(f"find tasks, detail: {e}", HttpStatus.BAD_REQUEST)
    
# Create Character with model of schema
@router.post(path.post_tasks)
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
@router.put(path.put_tasks)
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
@router.patch(path.patch_tasks)
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
@router.delete(path.delete_tasks)
def delete_tasks(task_id: int, authorization: str = Header(...), db: Session = Depends(get_db)): # type: ignore
    try:
        user_auth = auth_token(authorization)
        if user_auth['role'] != UserRole().ADMIN:
            raise HTTPException(HttpStatus.BAD_REQUEST, detail='Not authorized')
        
        task = db.query(TaskModel).filter_by(id=task_id).first()
        if task:
            db.delete(task)
            
        db.commit()
        return {"message": "Task deleted successfully", "task": task}
    except Exception as e:
        return requestResponse.error(f"delete user, detail: {e}", HttpStatus.BAD_REQUEST)