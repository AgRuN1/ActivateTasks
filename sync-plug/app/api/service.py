from fastapi import HTTPException
from starlette.requests import Request


class EquipmentService:
    def __init__(self, request: Request):
        print(request.app.state.client)
        self._session = request.app.state.client

    async def send(self, equipment_id: str, data: dict):
        response = await self._session.post(
            f"/equipment/cpe/{equipment_id}",
            json=data,
        )
        # print(self._session)
        if response.status != 200:
            raise HTTPException(status_code=500)