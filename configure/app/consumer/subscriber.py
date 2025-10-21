import logging

from fastapi import Depends
from faststream.rabbit.fastapi import RabbitRouter

from app.consumer.schema import DataSchema
from app.config.settings import project_settings

from app.services.AService import AService

router = RabbitRouter(project_settings.RABBITMQ_DSN)
log = logging.getLogger(__name__)

@router.subscriber("configure")
@router.publisher("api")
async def configure(data: DataSchema, service: AService = Depends()):
    result = await service.run(
        data.equipment_id,
        data.parameters.model_dump(),
        data.timeoutInSeconds
    )
    log.info(f"Equipment is configured ID: {data.equipment_id}")
    return {
        "task_id": data.task_id,
        "status": "completed",
        "result": result
    }
