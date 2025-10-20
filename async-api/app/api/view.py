import logging
from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Depends, Path, HTTPException

from app.api.schema import DataSchema
from app.api.service import TaskService

router = APIRouter(prefix="/async/api/v1")
logging.basicConfig(format="%(asctime)s %(message)s ID: %(task_id)s", level=logging.INFO)
log = logging.getLogger(__name__)

@router.post("/equipment/cpe/{equipment_id}")
async def activate(
        equipment_id: Annotated[
            str,
            Path(title="The ID of the equipment", pattern=r"^[a-zA-Z0-9]{6,}$")
        ],
        data: DataSchema,
        service: TaskService = Depends()
):
    task_id = await service.send(equipment_id, data.model_dump())
    log.info("Task is created", extra={"task_id": task_id})
    return {
        "code": 200,
        "taskId": task_id,
    }

@router.get("/equipment/cpe/{equipment_id}/task/{task_id}")
async def activate(
        equipment_id: Annotated[
            str,
            Path(title="The ID of the equipment", pattern=r"^[a-zA-Z0-9]{6,}$")
        ],
        task_id: Annotated[
            UUID,
            Path(title="The UUID of the task")
        ],
        service: TaskService = Depends()
):
    status = await service.get_status(equipment_id, str(task_id))
    if status == "running":
        return {
            "code": 204,
            "message": "Task is still running",
        }
    elif status == "completed":
        return {
            "code": 200,
            "message": "Completed",
        }
    else:
        raise HTTPException(status_code=500)