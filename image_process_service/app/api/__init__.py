from fastapi import APIRouter

from app.api.v1 import image_process

api_router = APIRouter()

api_router.include_router(image_process.router, tags=["image_process"])
