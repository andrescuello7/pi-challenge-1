from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.config.database import engine
from src.config.openai import ConfigOpenAI
from src.models.character_model import Base
from src.routes.user_router import router as user_router
from src.routes.auth_router import router as auth_router
from src.routes.task_router import router as task_router
from src.routes.character_router import router as character_router
from src.routes.keyphrase_router import router as keyphrase_router

# Setting Cognitive Search and Storage for GPT
ConfigOpenAI.setApiCredentials()

# Include Routes for methods HTTP
app = FastAPI()
app.include_router(auth_router)
app.include_router(user_router)
app.include_router(task_router)
app.include_router(character_router)
app.include_router(keyphrase_router)

# Cors for methods HTTP
app.add_middleware(
    CORSMiddleware,
    # allow_origins for backwards compatibility
    allow_origins=["http://127.0.0.1:5500", "https://pi-challenge-fr.vercel.app"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "PATCH"],
    allow_headers=["*"],
)

# Set up database where database not have data
Base.metadata.create_all(bind=engine)