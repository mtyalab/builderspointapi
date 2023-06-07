import os
import time
from bson import ObjectId
from fastapi import APIRouter

from src.db.db import get_purchase_collection, get_db

from src.models.purchase import Purchase
from src.schemas.purchase_edit import PurchaseEdit
from src.utils.json_serialize import json_serialize
from rave_python import Rave, RaveExceptions, Misc

router = APIRouter()

db = get_db()

os.environ['PUBLIC_KEY'] = 'FLWPUBK-250e4f80e06facd3ce6d9da317a7140b-X'
os.environ['SECRET_KEY'] = 'FLWSECK-d3652619e3f35b47705973eb80a4b3d8-18850fcbb65vt-X'

public_key = os.getenv('PUBLIC_KEY')
secret_key = os.getenv('SECRET_KEY')

purchase_collection = get_purchase_collection()
rave = Rave(public_key, secret_key,
            production=True, usingEnv=False)


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
        purchases = purchase_collection.find({"user_id": user_id})
        return json_serialize(list(purchases))
    except Exception as e:
        return {"code": 500, "message": "Failed to retrieve users' purchases", "error": str(e)}


@router.post("/purchase/mobile_money_payment/charge")
async def mobile_money_payment(amount: str, phone_number: str, email: str, network: str):
    # Mobile payload
    payload = {
        "phonenumber": phone_number,
        "network": network,
        "amount": amount,
        "email": email,
        "tx_ref": generate_transaction_reference(),
        "IP": ""
    }

    try:
        res = rave.UGMobile.charge(payload)
        tx_ref = generate_transaction_reference()
        print("TX REF:", tx_ref)
        print("RES:", res)
        print("LINK:", res['link'])
        return res

    except RaveExceptions.TransactionChargeError as e:
        return e.err

    except RaveExceptions.TransactionVerificationError as e:
        return e.err["errMsg"]


@router.post("/purchase/card_payment/charge")
async def card_payments(card_no: str, cvv: str, expiry_month: str,
                        expiry_year: str, email: str, phone_number: str, first_name: str, last_name: str, pin: str,
                        billing_zip: str, billing_city: str, billing_address: str, billing_state: str,
                        billing_country: str):
    payload = {
        "cardno": card_no,
        "cvv": cvv,
        "expirymonth": expiry_month,
        "expiryyear": expiry_year,
        "email": email,
        "phonenumber": phone_number,
        "firstname": first_name,
        "lastname": last_name,
        "IP": ""

    }

    try:
        res = rave.Card.charge(payload)

        if res["suggestedAuth"]:
            arg = Misc.getTypeOfArgsRequired(res["suggestedAuth"])

            if arg == "pin":
                Misc.updatePayload(res["suggestedAuth"], payload, pin=pin)
            if arg == "address":
                Misc.updatePayload(res["suggestedAuth"], payload, address={"billingzip": billing_zip,
                                                                           "billingcity": billing_city,
                                                                           "billingaddress": billing_address,
                                                                           "billingstate": billing_state,
                                                                           "billingcountry": billing_country})

                res = rave.Card.charge(payload)

            if res["validationRequired"]:
                rave.Card.validate(res["flwRef", ""])

                res = rave.Card.verify(res["txRef"])
                return res["transactionComplete"]

    except RaveExceptions.CardChargeError as e:
        return e.err["errMsg"]

    except RaveExceptions.TransactionValidationError as e:
        return e.err

    except RaveExceptions.TransactionVerificationError as e:
        return e.err["errMsg"]


def generate_transaction_reference(merchant_id=None):
    rawTime = round(time.time() * 1000)
    timestamp = int(rawTime)
    if merchant_id:
        return merchant_id + "_" + str(timestamp)
    else:
        return "MC-" + str(timestamp)
