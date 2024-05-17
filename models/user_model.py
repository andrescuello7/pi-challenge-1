from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from db_config import Base
from datetime import datetime

# CharacterModel implementation
class UserModel(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    photo = Column(String(255), default='')
    user_name = Column(String(255), nullable=False)
    full_name = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)
    role = Column(Integer, default=0, nullable=True)
    created_at = Column(DateTime, default=lambda: datetime.now(), nullable=True)
