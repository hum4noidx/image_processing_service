from app.services.process_image import process_input_image
from fastapi import APIRouter, File

router = APIRouter(
    prefix="/image_process",
    tags=["image_process"],
)


@router.post("/process")
async def process_image(
    image: bytes = File(...),
):
    filename = "test.jpg"
    result = await process_input_image(image=image, filename=filename)
    return result
