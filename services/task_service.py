from fastapi import HTTPException, status
from models.task_model import TaskModel
from models.user_model import UserModel
from models.comment_model import CommentModel
from schemas.task_schema import task_schema, User, Comment
from sqlalchemy import or_, and_
from datetime import datetime
from typing import List

def get_all_tasks(db) -> List[task_schema]:
    """
    Query of database in the table TasksModel to get all tasks.
    """
    _list = []
    response = db.query(TaskModel).all()
    if db and response:
        for task in response:
            user = db.query(UserModel).filter_by(id=task.user_id).first()
            if user:
                user_schema = User(
                    id=user.id,
                    photo=user.photo,
                    user_name=user.user_name,
                    full_name=user.full_name,
                    password=user.password,
                    role=user.role,
                )

                comments = db.query(CommentModel).filter_by(
                    task_id=task.id).all()
                comment_schemas = [Comment(
                    id=comment.id,
                    task_id=comment.task_id,
                    comment=comment.comment,
                ) for comment in comments]

                schema = task_schema(
                    id=task.id,
                    state=task.state,
                    title=task.title,
                    description=task.description,
                    user_id=task.user_id,
                    user=user_schema,
                    comments=comment_schemas,
                )
                _list.append(schema)

        return _list
    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="find all tasks in database"
        )

def get_tasks_by_id(db, user_id, status_task):
    '''
    Query of database in the table TasksModel to get by id
    '''
    _list = []
    if db:
        query = db.query(TaskModel)
        if user_id is not None and status_task is not None:
            query = query.filter(and_(TaskModel.user_id == user_id, TaskModel.state == status_task))
        elif user_id is not None:
            query = query.filter(TaskModel.user_id == user_id)
        elif status_task is not None:
            query = query.filter(TaskModel.state == status_task)
        
        # Ejecutar la consulta y devolver los resultados
        response = query.all()
        if db and response:
            for task in response:
                user = db.query(UserModel).filter_by(id=task.user_id).first()
                if user:
                    user_schema = User(
                        id=user.id,
                        photo=user.photo,
                        user_name=user.user_name,
                        full_name=user.full_name,
                        password=user.password,
                        role=user.role,
                    )

                    comments = db.query(CommentModel).filter_by(
                        task_id=task.id).all()
                    comment_schemas = [Comment(
                        id=comment.id,
                        task_id=comment.task_id,
                        comment=comment.comment,
                    ) for comment in comments]

                    schema = task_schema(
                        id=task.id,
                        state=task.state,
                        title=task.title,
                        description=task.description,
                        user_id=task.user_id,
                        user=user_schema,
                        comments=comment_schemas,
                    )
                    _list.append(schema)
        return _list
    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="find all tasks in database"
        )


def create_new_task(db, req):
    '''
    Query for Add in the table TasksModel database
    '''
    if db and req:
        model = TaskModel(
            state=req.state,
            title=req.title,
            user_id=req.user_id,
            description=req.description,
        )
        db.add(model)
        db.commit()
        db.refresh(model)

        return model
    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="database or model task null"
        )

def update_task(db, task_id, req):
    '''
    Query for UPDATE in the table TasksModel in the database
    Identify for task_id
    '''
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
    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="update task, in get datos for update"
        )

def patch_task(db, task_id, state):
    '''
    Query for UDPATE a task for state in the table TasksModel in the database
    Identify for task_id

    STATES [Todo, In Progress and Done]
    '''
    if task_id:
        model = db.query(TaskModel).filter_by(id=task_id).first()
        model.state = state
        model.update_at = datetime.now()

        db.add(model)
        db.commit()
        db.refresh(model)

        return model
    else:
        raise HTTPException(
            status_code=status.HTTP_400_INTERNAL_SERVER_ERROR,
            detail="task_id null or error in udpate task"
        )

def delete_tasks(db, task_id):
    '''
    Query for DELETE a task in the table TasksModel in the database
    Identify for task_id
    '''
    if task_id:
        task = db.query(TaskModel).filter_by(id=task_id).first()
        db.delete(task)
        db.commit()
        return task
    else:
        raise HTTPException(
            status_code=status.HTTP_400_INTERNAL_SERVER_ERROR,
            detail="task_id is null"
        )

def add_comment_task(db, req):
    '''
    Query for DELETE a task in the table TasksModel in the database
    Identify for task_id
    '''
    if req and db:
        model = CommentModel(
            task_id=req.task_id,
            comment=req.comment,
        )
        db.add(model)
        db.commit()
        db.refresh(model)

        return model
    else:
        raise HTTPException(
            status_code=status.HTTP_400_INTERNAL_SERVER_ERROR,
            detail="error creting comment"
        )
