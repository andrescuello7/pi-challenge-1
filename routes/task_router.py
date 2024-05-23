from fastapi import APIRouter, HTTPException, Header, status
from fastapi.params import Depends
from db_config import session, get_db
from enums.user_enum import user_role
from schemas.task_schema import task_schema
from services import task_service as controller
from utils.auth import auth_token

router = APIRouter()

@router.get('/api/tasks/getAll')
def get_all_tasks(db: session = Depends(get_db)):
    try:
        response = controller.get_all_tasks(db)
        return response
    except Exception as e:
        return {'error': f"get all tasks, detail: {e}"}

@router.get('/api/find/tasks')
def get_tasks_by_id(user_id: int, db: session = Depends(get_db)):
    try: 
        response = controller.get_tasks_by_id(db, user_id)
        return response
    except Exception as e:
        return {'error': f"find tasks: {e}"}

@router.post('/api/create/task')
def create_new_task(
    req: task_schema,
    authorization: str = Header(...),
    db: session = Depends(get_db)):
    try:
        user_auth = auth_token(authorization)
        if auth_token(authorization)['role'] != user_role().ADMIN:
            raise HTTPException(status.HTTP_401_UNAUTHORIZED,
                detail='Not authorized')

        model = controller.create_new_task(db, req, user_auth['id'])
        return model
    except Exception as e:
        return {'error': f"create user, detail: {e}"}

@router.put('/api/update/task/{task_id}')
def update_task(
    task_id: int,
    req: task_schema,
    authorization: str = Header(...),
    db: session = Depends(get_db)):
    try:
        if auth_token(authorization)['role'] != user_role().ADMIN:
            raise HTTPException(status.HTTP_401_UNAUTHORIZED,
                detail='Not authorized')
     
        model = controller.update_task(db, task_id, req)
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
            raise HTTPException(status.HTTP_401_UNAUTHORIZED,
                detail='Not authorized')

        model = controller.patch_task(db, task_id, state)
        return model
    except Exception as e:
        return {'error': f"update state task, detail: {e}"}

@router.delete('/api/delete/task/{task_id}')
def delete_tasks(
    task_id: int,
    authorization: str = Header(...),
    db: session = Depends(get_db)):
    try:
        user_auth = auth_token(authorization)
        if user_auth['role'] != user_role().ADMIN:
            raise HTTPException(status.HTTP_401_UNAUTHORIZED,
                detail='Not authorized')

        task = controller.delete_tasks(db, task_id)
        return {"message": "Task deleted successfully", "task": task}
    except Exception as e:
        return {'error': f"delete task, detail: {e}"}
