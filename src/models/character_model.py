from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from src.config.database import Base
from datetime import datetime

# CharacterModel implementation
class CharacterModel(Base):
    __tablename__ = "characters"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    height = Column(Integer)
    mass = Column(Integer)
    hair_color = Column(String(255))
    skin_color = Column(String(255))
    created_at = Column(DateTime, default=lambda: datetime.now(), nullable=True)

    eye_color_id = Column(Integer, ForeignKey('eye_color.id'), nullable=False)
    eye_color = relationship("EyeColorModel")
    # eye_color = relationship("eye_color", foreign_keys="characters.eye_color_id")

