import logging

from fastapi import APIRouter, Depends

from app.api.schema import DataSchema
from app.services.AService import AService

router = APIRouter(prefix="/equipment")
log = logging.getLogger(__name__)

@router.post("/cpe/{equipment_id}")
async def configure(equipment_id: str, data: DataSchema, service: AService = Depends()):
    result = await service.run(equipment_id, data.parameters.model_dump(), data.timeoutInSeconds)
    log.info(f"Equipment is configured ID: {equipment_id}, result: {result}")
    return {"message": "success"}