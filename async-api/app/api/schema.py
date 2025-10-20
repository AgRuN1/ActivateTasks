from typing import Optional, List

from pydantic import BaseModel


class Parameters(BaseModel):
    username: str
    password: str
    vlan: Optional[int] = None
    interfaces: List[int] = []


class DataSchema(BaseModel):
    timeoutInSeconds: int
    parameters: Parameters