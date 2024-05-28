from sqlalchemy import Column, Integer, String
from db_config import Base

class CommentModel(Base):
    __tablename__ = "comment"
    id = Column(Integer, primary_key=True, index=True)
    task_id = Column(Integer, nullable=False, default=None)
    comment = Column(String(255), nullable=False)
