import asyncio
import logging

from faststream import FastStream
from faststream.rabbit import RabbitBroker

from app.schema import DataSchema
from app.config.settings import project_settings

broker = RabbitBroker(project_settings.RABBITMQ_DSN)
app = FastStream(broker)

logging.basicConfig(
    format="%(asctime)s %(message)s ID: %(equipment_id)s",
    level=logging.INFO
)
log = logging.getLogger(__name__)

@broker.subscriber("configure")
@broker.publisher("api")
async def configure(data: DataSchema):
    await asyncio.sleep(data.timeoutInSeconds) # вызов сервиса А
    log.info(f"Equipment is configured", extra={"equipment_id": data.equipment_id})
    return {
        "task_id": data.task_id,
        "status": "completed"
    }
