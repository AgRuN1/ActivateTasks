import logging

import uvicorn
from fastapi import FastAPI

from app.api.view import router as api_router
from app.consumer.subscriber import router as consumer_router
from app.config.settings import project_settings


logging.basicConfig(level=logging.INFO)
app = FastAPI(
    title=project_settings.PROJECT_NAME,
    version=project_settings.VERSION,
    debug=project_settings.DEBUG,
    openapi_url="",
    lifespan=consumer_router.lifespan_context,
)
app.include_router(api_router)
app.include_router(consumer_router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)