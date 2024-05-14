import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.config.database import engine
from src.routes.user_router import router as user_router
from src.routes.auth_router import router as auth_router
from src.routes.task_router import router as task_router
from src.routes.character_router import router as character_router
from src.routes.keyphrase_router import router as keyphrase_router
from src.models.character_model import Base
from src.config.openai import ConfigOpenAI

# set up clients for Cognitive Search and Storage
ConfigOpenAI.setApiCredentials()

# Configuración de políticas CORS
origins = [
    "http://127.0.0.1:5500",
    "http://127.0.0.1:8000"
]

# Include Routes for methods HTTP
app = FastAPI()
app.include_router(auth_router)
app.include_router(user_router)
app.include_router(task_router)
app.include_router(character_router)
app.include_router(keyphrase_router)

# Cors
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "PATCH"],
    allow_headers=["*"],
)

# Server running from FastAPI
if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)