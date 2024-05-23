from db_config import engine
from models.comment_model import Base

# Set up database where database not have data
Base.metadata.create_all(bind=engine)
