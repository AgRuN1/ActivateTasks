import json
import logging

from faststream import FastStream
from faststream.rabbit import RabbitBroker
from redis.asyncio import Redis

from app.schema import TaskSchema
from app.config.settings import project_settings

redis = Redis.from_url(project_settings.REDIS_DSN)
broker = RabbitBroker(project_settings.RABBITMQ_DSN)
app = FastStream(broker)

logging.basicConfig(format="%(asctime)s %(message)s ID: %(task_id)s %(status)s", level=logging.INFO)
log = logging.getLogger(__name__)


@broker.subscriber("api")
async def update(data: TaskSchema):
    task = await redis.get(data.task_id)
    if not task:
        log.error("Task not found", extra={"task_id": data.task_id})
        return
    task = json.loads(task)
    task["status"] = data.status
    await redis.set(data.task_id, json.dumps(task))
    log.info("Task is updated", extra={"task_id": data.task_id, "status": data.status})
