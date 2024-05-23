from uvicorn import run
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import router
from services import openai

# Settings
app = FastAPI()
app.include_router(router)
openai.config_openAI.set_api_credentials(self='')

# Cors
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "PATCH"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    run("app:app", host="127.0.0.1", port=8000, reload=True)
