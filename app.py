import uvicorn

from fastapi import FastAPI
from routes import router
from services.openai import config_openAI
from fastapi.middleware.cors import CORSMiddleware

# Settings
app = FastAPI()
app.include_router(router)
config_openAI.set_api_credentials(self='')

# Cors
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:5500",
        "https://pi-challenge-fr.vercel.app",
    ],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "PATCH"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)
