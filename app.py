import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse
from fastapi import FastAPI
from routes import router
from services import openai

# Settings
app = FastAPI(
    title="Challenge Python",
    description="This is Challenge for Python Level 1. 🚀",
    version="0.0.4",
    contact={
        "name": "Andres Cuello",
        "url": "https://andrescuello.netlify.app/",
        "email": "andrescuellotrabajo@gmail.com",
    }
)
app.include_router(router)
openai.config_openAI.set_api_credentials(self='')

# Documentation
@router.get("/")
def main():
    return RedirectResponse(url="/docs/")

# Cors
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "PATCH"],
    allow_headers=["*"],
)

# Server
if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)
