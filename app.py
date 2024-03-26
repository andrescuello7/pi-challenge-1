import uvicorn
from fastapi import FastAPI
from src.services.database import engine
from src.routes.character_router import router
from src.models.character_model import Base

# Server running from FastAPI
app = FastAPI()

# Include Routes for methods HTTP
app.include_router(router)

# Create Models in Database
Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)