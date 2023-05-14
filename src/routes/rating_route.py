from fastapi import APIRouter, HTTPException

from src.db.db import get_rating_collection
from bson import ObjectId
from src.models.rating import Rating
from src.utils import json_serialize

router = APIRouter()

rating_collection = get_rating_collection()


# Truck endpoints
# CREATE - Create a new rating record
@router.post("/rating/post")
async def add_truck_record(truck: Rating):
    try:
        result = rating_collection.insert_one(truck.dict())
        rating_d = result.inserted_id
        return {"code": 201, "message": "Rating created successfully", "rating_id": str(rating_d)}
    except Exception as e:
        return {"code": 400, "message": "Rating creation failed", "error": str(e)}


# READ - Get all truck records
@router.get("/rating/all")
async def get_truck_records():
    try:
        ratings = list(rating_collection.find())
        return json_serialize(ratings)
    except Exception as e:
        return {"code": 500, "message": "Failed to retrieve ratings", "error": str(e)}


# DELETE - Delete a specific rating record
@router.delete("/rating/{id}")
async def delete_rating_record(id: str):
    rating_collection.find_one_and_delete({"_id": ObjectId(id)})
    return {"status": "OK"}
