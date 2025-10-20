from fastapi import HTTPException
from starlette.requests import Request


class EquipmentService:
    def __init__(self, request: Request):
        self._session = request.app.state.client

    async def send(self, equipment_id: str, data: dict):
        print(data)
        response = await self._session.post(
            f"/equipment/cpe/{equipment_id}",
            json=data,
        )
        if response.status != 200:
            raise HTTPException(status_code=500)