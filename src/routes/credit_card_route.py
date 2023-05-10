import os
import uuid

from bson import ObjectId
from fastapi import APIRouter

from src.db.db import get_credit_card_collection, get_db

from src.models.order import Order
from src.schemas.credit_card_edit import CreditCardEdit
from src.utils.json_serialize import json_serialize

router = APIRouter()

db = get_db()

credit_card_collection = get_credit_card_collection()


@router.post("/card/add")
async def add_credit_card_record(credit_card_data: Order):
    try:
        credit_card_collection.insert_one(credit_card_data.dict())

        return {"code": 200, "message": "Successfully added"}
    except Exception as e:
        return {"code": 500, "message": str(e)}


# UPDATE - Update a specific card record by ID
@router.put("/card/{id}")
async def update_credit_card_record_by_id(card_id: str, credit_card_edit: CreditCardEdit):
    credit_card_collection.update_one({"_id": ObjectId(card_id)}, {"$set": credit_card_edit.dict()})
    return {"code": 200, "message": "Record successfully updated"}


# DELETE - Delete a specific card record
@router.delete("/card/{id}")
async def delete_credit_card_record(card_id: str):
    credit_card_collection.find_one_and_delete({"_id": ObjectId(card_id)})
    return {"status": "OK"}


@router.get("/card/all")
async def list_credit_cards():
    try:
        credit_cards = list(credit_card_collection.find())
        return json_serialize(credit_cards)
    except Exception as e:
        return {"code": 500, "message": "Failed to retrieve orders", "error": str(e)}


@router.get("/card/user_id")
async def list_credit_card_by_selected_user(user_id: str):
    try:
        credit_cards = list(credit_card_collection.find_one({"user_id": ObjectId(user_id)}))
        return json_serialize(credit_cards)
    except Exception as e:
        return {"code": 500, "message": "Failed to retrieve users' credit cards", "error": str(e)}
