import logging

import aiohttp
from fastapi import APIRouter, File, UploadFile, HTTPException
from starlette import status

from app.core.config import settings
from app.deps.db import CurrentAsyncSession
from app.repo.pipeline_repo import PipelineRepo

logger = logging.getLogger(__name__)

router = APIRouter(
    prefix="/process_image",
    tags=["image_process"],
)


@router.post("/")
async def process_image(
    pipeline_id: int,
    current_session: CurrentAsyncSession,
    image: UploadFile = File(...),
):
    pipeline_repo: PipelineRepo = PipelineRepo(current_session)
    pipeline = await pipeline_repo.get_pipeline_by_id(pipeline_id=pipeline_id)
    if not pipeline:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Pipeline with ID {pipeline_id} not found")

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
