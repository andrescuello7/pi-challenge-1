from fastapi import APIRouter, HTTPException, Header, status
from services import task_service as controller
from db_config import session, get_db
from utils.auth import auth_token
from fastapi.params import Depends
from enums.user_enum import USER_ROLE
from schemas.task_schema import task_schema
from schemas.comment_schema import comment_schema
router = APIRouter()


@router.get('/api/tasks/getAll')
def get_all_tasks(db: session = Depends(get_db)):
    try:
        response = controller.get_all_tasks(db)
        return response
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"get all tasks, detail: {e}",
        )


@router.get('/api/find/tasks')
def get_tasks_by_id(
        user_id: int = None,
        status: int = None,
        authorization: str = Header(...),
        db: session = Depends(get_db)):
    try:
        user = auth_token(authorization)
        response = controller.get_tasks_by_id(
            db=db,
            user=user,
            status_task=status,
            user_id=user_id
        )
        return response
    except Exception as e:
        raise HTTPException(
            status_code=e.status_code,
            detail=e.detail
        )


@router.post('/api/create/task')
def create_new_task(
        req: task_schema,
        authorization: str = Header(...),
        db: session = Depends(get_db)):
    try:
        if auth_token(authorization)['role'] != USER_ROLE.ADMIN:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail='Error user not authorized'
            )

        model = controller.create_new_task(db, req)
        return model
    except Exception as e:
        raise HTTPException(
            status_code=e.status_code,
            detail=e.detail
        )


@router.put('/api/update/task/{task_id}')
def update_task(
        task_id: int,
        req: task_schema,
        authorization: str = Header(...),
        db: session = Depends(get_db)):
    try:
        role = auth_token(authorization)['role']
        if role != USER_ROLE.USER:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail='Error user not authorized'
            )

        model = controller.update_task(db, task_id, req)
        return model
    except Exception as e:
        raise HTTPException(
            status_code=e.status_code,
            detail=e.detail
        )


@router.patch('/api/move/task')
def patch_task(
        task_id: int,
        state: int,
        authorization: str = Header(...),
        db: session = Depends(get_db)):
    try:
        auth_token(authorization)
        model = controller.patch_task(db, task_id, state)
        return model
    except Exception as e:
        raise HTTPException(
            status_code=e.status_code,
            detail=e.detail
        )


@router.delete('/api/delete/task/{task_id}')
def delete_tasks(
        task_id: int,
        authorization: str = Header(...),
        db: session = Depends(get_db)):
    try:
        if auth_token(authorization)['role'] != USER_ROLE.ADMIN:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail='Error user not authorized')

        task = controller.delete_tasks(db, task_id)
        return {"message": "Task deleted successfully", "task": task}
    except Exception as e:
        raise HTTPException(
            status_code=e.status_code,
            detail=e.detail
        )


@router.post('/api/add/comment')
def add_comment_task(
        req: comment_schema,
        authorization: str = Header(...),
        db: session = Depends(get_db)):
    try:
        role = auth_token(authorization)['role']
        if role != USER_ROLE.USER:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail='Error user not authorized'
            )

        task = controller.add_comment_task(db, req)
        return {"message": "Added comment successfully", "task": task}
    except Exception as e:
        raise HTTPException(
            status_code=e.status_code,
            detail=e.detail
        )
