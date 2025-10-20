from fastapi import HTTPException


class TaskNotFound(HTTPException):
    def __init__(self):
        super().__init__(404, detail="The requested task is not found")


class EquipmentNotFound(HTTPException):
    def __init__(self):
        super().__init__(404, detail="The requested equipment is not found")