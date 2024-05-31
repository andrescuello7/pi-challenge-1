import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, APIRouter
from starlette.responses import RedirectResponse
from routes import router
# from services import openai

app = FastAPI()
router = APIRouter()
# app.include_router(router)
# openai.config_openAI.set_api_credentials(self='')

@router.get("/")
def main():
    return RedirectResponse(url="/docs/")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "PATCH"],
    allow_headers=["*"],
)

# if __name__ == "__main__":
#     uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=False)
