from typing import Optional, List

from pydantic import BaseModel


class Parameters(BaseModel):
    username: str
    password: str
    vlan: Optional[int] = None
    interfaces: List[int] = []


class DataSchema(BaseModel):
    timeoutInSeconds: int
    task_id: str
    equipment_id: str
    parameters: Parameters