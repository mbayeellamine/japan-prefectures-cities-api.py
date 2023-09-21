from fastapi.openapi.utils import get_openapi
from fastapi import FastAPI, HTTPException, Query, APIRouter
from pydantic import BaseModel
from mangum import Mangum
from typing import List
import os, json

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

# Load JSON data
data_dir = "data"  # Update this to your data directory path

with open('data/prefectures.json', 'r', encoding='utf-8') as prefectures_file:
    prefectures_data = json.load(prefectures_file)

with open('data/cities.json', 'r', encoding='utf-8') as cities_file:
    cities_data = json.load(cities_file)

with open('data/prefectures-stations.json', 'r', encoding='utf-8') as file:
    prefecture_train_stations_data = json.load(file)

@router.get("/", response_model=dict)
def read_root():
    return {"message": "pong"}

@router.get("/cities-by-prefecture-id", response_model=dict)
def get_cities_by_prefecture_id(prefecture_id: str = Query(...)):
    # Check if the prefecture_id is provided and valid
    if not prefecture_id:
        raise HTTPException(status_code=400, detail="prefecture_id is required")

    # Get cities for the specified prefecture_id
    filtered_cities = [city for city in cities_data if str(city["prefecture_id"]) == prefecture_id]

    return {"cities": filtered_cities}

@router.get("/prefectures", response_model=dict)
def get_prefectures():
    return {"prefectures": prefectures_data}
    
@router.get("/lines-by-pref", response_model=dict)
def get_lines_by_pref(prefecture_id: str = Query(...)):
    if not prefecture_id:
        raise HTTPException(status_code=400, detail="prefecture_id is required")

    lines_for_prefecture = [prefecture for prefecture in prefecture_train_stations_data if str(prefecture["id"]) == str(prefecture_id)]

    return {"prefecture_lines": lines_for_prefecture}

app.include_router(router, prefix="/api")
