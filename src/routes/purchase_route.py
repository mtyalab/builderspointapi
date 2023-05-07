import os
import uuid

from bson import ObjectId
from fastapi import APIRouter

from src.db.db import get_purchase_collection, get_db

from src.models.purchase import Purchase
from src.schemas.purchase_edit import PurchaseEdit
from src.utils.json_serialize import json_serialize

router = APIRouter()

db = get_db()

purchase_collection = get_purchase_collection()


@router.post("/purchase/add")
async def add_purchase_record(purchase_data: Purchase):
    try:
        purchase_collection.insert_one(purchase_data.dict())

        return {"code": 200, "message": "Successfully added"}
    except Exception as e:
        return {"code": 500, "message": str(e)}


# UPDATE - Update a specific purchase record by ID
@router.put("/purchase/{id}")
async def update_purchase_record_by_id(purchase_id: str, purchase_edit: PurchaseEdit):
    purchase_collection.update_one({"_id": ObjectId(purchase_id)}, {"$set": purchase_edit.dict()})
    return {"code": 200, "message": "Record successfully updated"}


# DELETE - Delete a specific purchase record
@router.delete("/purchase/{id}")
async def delete_purchase_record(purchase_id: str):
    purchase_collection.find_one_and_delete({"_id": ObjectId(purchase_id)})
    return {"status": "OK"}


@router.get("/purchase/all")
async def list_purchases():
    try:
        purchases = list(purchase_collection.find())
        return json_serialize(purchases)
    except Exception as e:
        return {"code": 500, "message": "Failed to retrieve purchases", "error": str(e)}


@router.get("/purchase/user_id")
async def list_purchases_by_selected_user(user_id: str):
    try:
        purchases = list(purchase_collection.find_one({"user_id": ObjectId(user_id)}))
        return json_serialize(purchases)
    except Exception as e:
        return {"code": 500, "message": "Failed to retrieve users' purchases", "error": str(e)}
