import uvicorn
from fastapi import FastAPI
from src.config.database import engine
from src.routes.character_router import router as character_router
from src.routes.question_router import router as question_router
from src.models.character_model import Base
from src.config.openai import ConfigOpenAI

# set up clients for Cognitive Search and Storage
ConfigOpenAI.setApiCredentials()

# Include Routes for methods HTTP
app = FastAPI()
app.include_router(character_router)
app.include_router(question_router)

# Server running from FastAPI
if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)