import uvicorn

from services.openai import config_openAI
from fastapi import APIRouter, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from router.user_router import router as user_router
from router.auth_router import router as auth_router
from router.task_router import router as task_router
from router.character_router import router as character_router
from router.keyphrase_router import router as keyphrase_router

# Settings
app = FastAPI()
config_openAI.set_api_credentials(self='')

# Include Routes
list_router: list[APIRouter] = [
    auth_router,
    user_router,
    task_router,
    character_router,
    keyphrase_router
]

for router in list_router:
    app.include_router(router)

# Cors
app.add_middleware(
    CORSMiddleware,
    # allow_origins for backwards compatibility
    allow_origins=[
        "http://127.0.0.1:5500",
        "https://pi-challenge-fr.vercel.app",
    ],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "PATCH"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000)
