import asyncio
import logging

from fastapi import APIRouter
from starlette.requests import Request

from app.config.settings import project_settings

from app.api.schema import DataSchema

router = APIRouter(prefix="/equipment")
logging.basicConfig(format="%(asctime)s %(message)s ID: %(equipment_id)s", level=logging.INFO)
log = logging.getLogger(__name__)

@router.post("/cpe/{equipment_id}")
async def configure(equipment_id: str, data: DataSchema):
    await asyncio.sleep(data.timeoutInSeconds) # вызов сервиса А
    log.info("Equipment is configured", extra={"equipment_id": equipment_id})
    return {"message": "success"}