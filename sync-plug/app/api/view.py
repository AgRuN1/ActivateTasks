import asyncio
import logging
from typing import Annotated

import aiohttp
from fastapi import APIRouter, Depends, Path, HTTPException

from app.api.schema import DataSchema
from app.api.service import EquipmentService
from app.config.settings import project_settings

router = APIRouter(prefix="/sync/api/v1", tags=["equipment"])

logging.basicConfig(format="%(asctime)s %(message)s ID: %(equipment_id)s", level=logging.INFO)
log = logging.getLogger(__name__)

@router.post("/equipment/cpe/{equipment_id}")
async def activate(
        equipment_id: Annotated[
            str,
            Path(title="The ID of the equipment", pattern=r"^[a-zA-Z0-9]+$")
        ],
        data: DataSchema,
        service: EquipmentService = Depends()
):
    try:
        await service.send(equipment_id, data.model_dump())
    except aiohttp.ClientConnectorError:
        log.error("Connection error", extra={"equipment_id": equipment_id})
        raise HTTPException(status_code=500)
    except aiohttp.ClientResponseError:
        log.error("Response error", extra={"equipment_id": equipment_id})
        raise HTTPException(status_code=500)
    except asyncio.TimeoutError:
        log.error("Timeout error", extra={"equipment_id": equipment_id})
        raise HTTPException(status_code=500)
    finally:
        await asyncio.sleep(project_settings.DELAY)
    log.info("Equipment is configured", extra={"equipment_id": equipment_id})
    return {
        "code": 200,
        "message": "success",
    }