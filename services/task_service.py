from fastapi import HTTPException, status
from models.task_model import TaskModel
from models.user_model import UserModel
from datetime import datetime

def get_all_tasks(db):
    '''
    Query of database in the table TasksModel to get all
    '''
    _list = []
    response = db.query(TaskModel).all()
    if db and response:
        for task in response:
            user = db.query(UserModel).filter_by(id=task.user_id).first()
            if user:
                _list.append({'user': user, 'task': task})

        return _list
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
            detail="find all tasks in database")

def get_tasks_by_id(db, user_id):
    '''
    Query of database in the table TasksModel to get by id
    '''
    if db:
        response = db.query(TaskModel).filter_by(user_id=user_id).all()
        return response
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
            detail="find all tasks in database")

def create_new_task(db, req, _id):
    '''
    Query for Add in the table TasksModel database
    '''
    if db and req:
        model = TaskModel(
            state=req.state,
            title=req.title,
            user_id=_id,
            description=req.description,
        )
        db.add(model)
        db.commit()
        db.refresh(model)

        return model
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
            detail="database or model task null")


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
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
            detail="udpate task, in get datos for update")


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
        raise HTTPException(status_code=status.HTTP_400_INTERNAL_SERVER_ERROR,
            detail="task_id null or error in udpate task")

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
        raise HTTPException(status_code=status.HTTP_400_INTERNAL_SERVER_ERROR,
            detail="task_id is null")