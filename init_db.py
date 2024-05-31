from db_config import engine
from models.task_model import Base as TaskModelBase
from models.user_model import Base as UserModelBase
from models.comment_model import Base as CommentModelBase

# Set up database where database not have data
TaskModelBase.metadata.create_all(bind=engine)
UserModelBase.metadata.create_all(bind=engine)
CommentModelBase.metadata.create_all(bind=engine)
