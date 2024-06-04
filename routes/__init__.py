from fastapi import APIRouter
from routes.user_router import router as user_router
from routes.auth_router import router as auth_router
from routes.task_router import router as task_router
# from routes.character_router import router as character_router
# from routes.keyphrase_router import router as keyphrase_router

# Include Routes
list_router: list[APIRouter] = [
    auth_router,
    user_router,
    task_router,
    # character_router,
    # keyphrase_router
]
router = APIRouter()

for item in list_router:
    router.include_router(item)
