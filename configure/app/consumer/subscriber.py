import asyncio
import logging

from faststream.rabbit.fastapi import RabbitRouter

from app.consumer.schema import DataSchema
from app.config.settings import project_settings

router = RabbitRouter(project_settings.RABBITMQ_DSN)

logging.basicConfig(
    format="%(asctime)s %(message)s ID: %(equipment_id)s",
    level=logging.INFO
)
log = logging.getLogger(__name__)

@router.subscriber("configure")
@router.publisher("api")
async def configure(data: DataSchema):
    await asyncio.sleep(data.timeoutInSeconds) # вызов сервиса А
    log.info(f"Equipment is configured", extra={"equipment_id": data.equipment_id})
    return {
        "task_id": data.task_id,
        "status": "completed"
    }
