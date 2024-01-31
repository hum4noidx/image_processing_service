import logging
import random

logger = logging.getLogger(__name__)


async def process_input_image(image: bytes, filename: str):
    logger.debug(f"Processing image: {filename}")
    car_found = random.choice([True, False])  # Imitate ML model to find car

    if car_found:
        logger.debug(f"Car found in image: {filename}")
        return {
            "car_found": True,
            "coordinates": [
                random.randint(0, 100),  # top left_x
                random.randint(0, 100),  # top left_y
                random.randint(0, 100),  # w
                random.randint(0, 100),  # h
                random.random(),  # conf
                1  # label, if 1 then car, if 0 then not car
            ]  # top left_x, top left_y, w, h, conf, label
        }

    logger.debug(f"Car not found in image: {filename}")
    return {
        "car_found": False,
        "coordinates": []
    }
