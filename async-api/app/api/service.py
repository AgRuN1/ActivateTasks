import json
from datetime import datetime, UTC
from uuid import uuid4

from starlette.requests import Request

from app.api.exceptions import TaskNotFound, EquipmentNotFound


class TaskService:
    def __init__(self, request: Request):
        self.redis = request.app.state.redis
        self.broker = request.app.state.broker

    async def send(self, equipment_id: str, data: dict):
        task_id = str(uuid4())
        task = {
            'parameters': data['parameters'],
            'equipment_id': equipment_id,
            'timestamp': datetime.now(UTC).timestamp(),
            'status': 'running'
        }
        await self.redis.set(task_id, json.dumps(task))
        data['equipment_id'] = equipment_id
        data['task_id'] = task_id
        async with self.broker as broker:
            await broker.publish(data, "configure")
        return task_id

    async def get_status(self, equipment_id: str, task_id: str):
        task = await self.redis.get(task_id)
        if task is None:
            raise TaskNotFound()
        task = json.loads(task)
        if task['equipment_id'] != equipment_id:
            raise EquipmentNotFound()
        return task['status']