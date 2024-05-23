from fastapi import APIRouter, Depends, HTTPException, Header
from fastapi.params import Depends, Depends
from datetime import datetime
from db_config import session, get_db
from enums.user_enum import user_role
from models.user_model import UserModel
from models.task_model import TaskModel
from schemas.task_schema import task_schema
from utils.auth import auth_token

router = APIRouter()

@router.get('/api/tasks/getAll')
def get_users(db: session = Depends(get_db)):
    try:
        _list = []
        response = db.query(TaskModel).all()
        for task in response:
            user = db.query(UserModel).filter_by(id=task.user_id).first()
            if user:
                _list.append({'user': user, 'task': task})

        return _list
    except Exception as e:
        return {'error': f"get all tasks, detail: {e}"}

@router.get('/api/find/tasks')
def get_users(user_id: int, db: session = Depends(get_db)):
    try: 
        response = db.query(TaskModel).filter_by(user_id=user_id).all()
        return response
    except Exception as e:
        return {'error': f"find tasks: {e}"}

@router.post('/api/create/task')
def create_user(req: task_schema, authorization: str = Header(...), db: session = Depends(get_db)):
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
        return {'error': f"create user, detail: {e}"}

@router.put('/api/update/task/{task_id}')
def update_task(task_id: int, req: task_schema, authorization: str = Header(...), db: session = Depends(get_db)):
    try:
        user_auth = auth_token(authorization)
        if user_auth['role'] != user_role().ADMIN:
            raise HTTPException(400, detail='Not authorized')

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
        return {'error': f"update user, detail: {e}"}

@router.patch('/api/move/task')
def patch_task(
    task_id: int,
    state: int,
    authorization: str = Header(...),
    db: session = Depends(get_db)):
    try:
        user_auth = auth_token(authorization)
        if user_auth['role'] != user_role().ADMIN:
            raise HTTPException(400, detail='Not authorized')

        model = db.query(TaskModel).filter_by(id=task_id).first()
        model.state = state
        model.update_at = datetime.now()
        db.add(model)
        db.commit()
        db.refresh(model)

        return model
    except Exception as e:
        return {'error': f"update state task, detail: {e}"}

@router.delete('/api/delete/task/{task_id}')
def delete_tasks(task_id: int, authorization: str = Header(...), db: session = Depends(get_db)):
    try:
        user_auth = auth_token(authorization)
        if user_auth['role'] != user_role().ADMIN:
            raise HTTPException(400, detail='Not authorized')

        task = db.query(TaskModel).filter_by(id=task_id).first()
        if task:
            db.delete(task)
            db.commit()
            return {"message": "Task deleted successfully", "task": task}
    except Exception as e:
        return {'error': f"delete task, detail: {e}"}
