import logging
from contextlib import asynccontextmanager
from typing import AsyncGenerator

import aiohttp
import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.exceptions import RequestValidationError
from starlette.requests import Request
from starlette.responses import JSONResponse

from app.api.view import router
from app.config.settings import project_settings


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    app.state.client = aiohttp.ClientSession(base_url=project_settings.CONFIGURE_ADDR)
    yield
    await app.state.client.close()

logging.basicConfig(level=logging.INFO)
app = FastAPI(
    title=project_settings.PROJECT_NAME,
    version=project_settings.VERSION,
    debug=project_settings.DEBUG,
    lifespan=lifespan,
    openapi_url=""
)
app.include_router(router)

@app.exception_handler(404)
async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        {
            "code": 404,
            "message": "The requested equipment is not found"
        }, status_code=404
    )

@app.exception_handler(500)
async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        {
            "code": 500,
            "message": "Internal provisioning exception"
        }, status_code=500
    )

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
            {
                "code": 422,
                "message": "Data format is incorrect"
            }, status_code=422
        )

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)
