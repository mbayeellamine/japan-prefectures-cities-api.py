from fastapi.openapi.utils import get_openapi
from fastapi import FastAPI, HTTPException, Query, APIRouter
from pydantic import BaseModel
from mangum import Mangum
from typing import List
import os, json
from api.routes import router as api_router
app = FastAPI()
# app = FastAPI(docs_url=None, redoc_url=None, openapi_url=None)
router = APIRouter()

handler = Mangum(app)

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="japan-prefectures-cities-api-service",
        version="2.5.0",
        description="Get Japan prefectures and cities",
        routes=app.routes,
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi

@router.get("/", response_model=dict)
def read_root():
    return {"message": "pong"}

app.include_router(api_router, prefix="/api/v1")
app.include_router(router, prefix="/api")
