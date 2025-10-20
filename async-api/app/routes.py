from fastapi import APIRouter

from app.api import view


def get_apps_router():
    router = APIRouter(prefix='/async/api/v1')
    router.include_router(view.router)
    return router