import uvicorn
from fastapi import FastAPI

from app.routes import get_apps_router
from app.config.settings import project_settings


def get_application() -> FastAPI:
    application = FastAPI(
        title=project_settings.PROJECT_NAME,
        version=project_settings.VERSION,
        openapi_url=""
    )
    application.include_router(get_apps_router())

    return application

app = get_application()

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8081, reload=True)
