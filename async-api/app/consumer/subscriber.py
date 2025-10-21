import json
import logging

from faststream.rabbit.fastapi import RabbitRouter
from starlette.requests import Request

from app.consumer.schema import TaskSchema
from app.config.settings import project_settings

router = RabbitRouter(project_settings.RABBITMQ_DSN)
log = logging.getLogger(__name__)


@router.subscriber("api")
async def update(data: TaskSchema, request: Request):
    task = await request.app.state.redis.get(data.task_id)
    if not task:
        log.error(f"Task not found ID: {data.task_id}")
        return
    task = json.loads(task)
    task["status"] = data.status
    await request.app.state.redis.set(data.task_id, json.dumps(task))
    log.info(f"Task is updated ID: {data.task_id}, status: {data.status}, result: {data.result}")
