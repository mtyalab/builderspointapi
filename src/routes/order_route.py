import os
import uuid

from bson import ObjectId
from fastapi import APIRouter

from src.db.db import get_order_collection, get_db

from src.models.order import Order
from src.schemas.order_edit import OrderEdit
from src.utils.json_serialize import json_serialize

router = APIRouter()

db = get_db()

order_collection = get_order_collection()


@router.post("/order/add")
async def add_order_record(order_data: Order):
    try:
        order_collection.insert_one(order_data.dict())

        return {"code": 200, "message": "Successfully added"}
    except Exception as e:
        return {"code": 500, "message": str(e)}


# UPDATE - Update a specific order record by ID
@router.put("/order/{id}")
async def update_order_record_by_id(order_id: str, order_edit: OrderEdit):
    order_collection.update_one({"_id": ObjectId(order_id)}, {"$set": order_edit.dict()})
    return {"code": 200, "message": "Record successfully updated"}


# DELETE - Delete a specific order record
@router.delete("/order/{id}")
async def delete_order_record(order_id: str):
    order_collection.find_one_and_delete({"_id": ObjectId(order_id)})
    return {"status": "OK"}


@router.get("/order/all")
async def list_orders():
    try:
        orders = list(order_collection.find())
        return json_serialize(orders)
    except Exception as e:
        return {"code": 500, "message": "Failed to retrieve orders", "error": str(e)}


@router.get("/order/user_id")
async def list_orders_by_selected_user(user_id: str):
    try:
        orders = list(order_collection.find_one({"user_id": ObjectId(user_id)}))
        return json_serialize(orders)
    except Exception as e:
        return {"code": 500, "message": "Failed to retrieve users' orders", "error": str(e)}
