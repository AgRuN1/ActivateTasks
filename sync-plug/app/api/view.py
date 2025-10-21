import asyncio
import logging
from typing import Annotated

import aiohttp
from fastapi import APIRouter, Depends, Path, HTTPException

from app.api.schema import DataSchema
from app.api.service import EquipmentService
from app.config.settings import project_settings

router = APIRouter(prefix="/sync/api/v1", tags=["equipment"])
log = logging.getLogger(__name__)

@router.post("/equipment/cpe/{equipment_id}")
async def activate(
        equipment_id: Annotated[
            str,
            Path(title="The ID of the equipment", pattern=r"^[a-zA-Z0-9]{6,}$")
        ],
        data: DataSchema,
        service: EquipmentService = Depends()
):
    try:
        await service.send(equipment_id, data.model_dump())
    except aiohttp.ClientConnectorError:
        log.error(f"Connection error ID: {equipment_id}")
        raise HTTPException(status_code=500)
    except aiohttp.ClientResponseError:
        log.error(f"Response error ID: {equipment_id}")
        raise HTTPException(status_code=500)
    except asyncio.TimeoutError:
        log.error(f"Timeout error ID: {equipment_id}")
        raise HTTPException(status_code=500)
    finally:
        await asyncio.sleep(project_settings.DELAY)
    log.info(f"Equipment is configured ID: {equipment_id}")
    return {
        "code": 200,
        "message": "success",
    }