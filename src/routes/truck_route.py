
from fastapi import APIRouter, HTTPException

from src.db.db import get_trucks_collection
from bson import ObjectId
from src.models.truck import Truck
from src.schemas.truck_schema import TruckEdit
from src.utils import json_serialize

router = APIRouter()

trucks_collection = get_trucks_collection()


# Truck endpoints
# CREATE - Create a new truck record
@router.post("/truck/post")
async def add_truck_record(truck: Truck):
    try:
        result = trucks_collection.insert_one(truck.dict())
        truck_d = result.inserted_id
        return {"code": 201, "message": "Truck created successfully", "truck_id": str(truck_d)}
    except Exception as e:
        return {"code": 400, "message": "Truck creation failed", "error": str(e)}


# READ - Get all truck records
@router.get("/truck/all")
async def get_truck_records():
    try:
        trucks = list(trucks_collection.find())
        return json_serialize(trucks)
    except Exception as e:
        return {"code": 500, "message": "Failed to retrieve trucks", "error": str(e)}


# READ - Get request to calculate and return total amount
@router.get("/truck/total")
async def get_truck_totals():
    try:
        trucks = list(trucks_collection.find())
        total_trucks = len(trucks)
        return {"totalTrucks": total_trucks}
    except Exception as e:
        return {"code": 500, "message": "Failed to retrieve total trucks", "error": str(e)}


# READ - a specific truck record by ID
@router.get("/truck/{id}")
async def get_truck_record_by_id(id: str):
    try:
        truck = trucks_collection.find_one({'_id': ObjectId(id)})
        if not truck:
            raise HTTPException(status_code=404, detail="Truck not found")
        return json_serialize(truck)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# UPDATE - Update a specific truck record by ID
@router.put("/truck/{id}")
async def update_truck_record_by_id(id: str, truck_edit: TruckEdit):
    trucks_collection.update_one({"_id": ObjectId(id)}, {"$set": truck_edit.dict()})
    return {"code": 200, "message": "Record successfully updated"}


# READ - Get a report of a selected truck
@router.get("/truck/{id}/report")
async def get_truck_report_by_id():
    return {}


# DELETE - Delete a specific truck record
@router.delete("/truck/{id}")
async def delete_truck_record(id: str):
    trucks_collection.find_one_and_delete({"_id": ObjectId(id)})
    return {"status": "OK"}
