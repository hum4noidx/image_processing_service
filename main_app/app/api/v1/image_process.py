import logging

import aiohttp
from fastapi import APIRouter, File, UploadFile

from app.core.config import settings

logger = logging.getLogger(__name__)

router = APIRouter(
    prefix="/process_image",
    tags=["image_process"],
)


@router.post("/")
async def process_image(
    image: UploadFile = File(...),
):
    data = {
        "image": await image.read(),
    }
    async with aiohttp.ClientSession() as session:
        result = await session.post(
            url=f"{settings.IMAGE_PROCESSING_URL}/api/v1/image_process/process",
            data=data,
        )
        logger.info(f"result: {result}")
        return await result.json()
