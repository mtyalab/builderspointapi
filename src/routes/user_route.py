import random
import string

from fastapi import APIRouter, HTTPException
from starlette.responses import JSONResponse

from src.models.reset_password import ResetPasswordRequest, ResetPasswordConfirm
from src.models.user import User, UserLogin
from src.db.db import get_user_collection
from src.utils.json_serialize import json_serialize
from src.utils.send_notifications import registration_success_notification, send_reset_code
import bcrypt

router = APIRouter()

user_collection = get_user_collection()


@router.post("/user/register")
async def register_user(user: User):
    # Hash the user's password using bcrypt
    hashed_password = bcrypt.hashpw(user.password.encode("utf-8"), bcrypt.gensalt())

    # Replace the plaintext password with the hashed password in the user object
    user_dict = user.dict()
    user_dict["password"] = hashed_password

    # Insert user document into the "users" collection
    result = user_collection.insert_one(user_dict)
    if result.acknowledged:
        # Send a notification email to the user
        registration_success_notification(user.email)
        return {"code": 200, "message": "User registered successfully"}
    else:
        return {"code": 400, "message": "Failed to register user"}


@router.post("/user/login")
async def login_user(user_login: UserLogin):
    # find the user document with the matching email address
    user_dict = user_collection.find_one({"email": user_login.email})

    if user_dict:
        # Verify that the provided password matches the hashed password in the user document
        hashed_password = user_dict["password"]
        if bcrypt.checkpw(user_login.password.encode("utf-8"), hashed_password):
            # Create a new User object from the user_dict and return it
            user = User(**user_dict)
            return JSONResponse(content={user.dict()})
        else:
            return HTTPException(status_code=400, detail="Invalid password")
    else:
        return HTTPException(status_code=400, detail="User not found")


@router.post("/user/reset_password")
async def reset_password(req: ResetPasswordRequest):
    user = user_collection.find_one({"email": req.email})
    if not user:
        return {"code": 400, "message": "User not found"}

    code = "".join(random.choices(string.digits, k=5))

    send_reset_code(req.email, code)

    return {"code": 200, "message": "Reset code was sent successfully"}


@router.post("/user/reset_password_confirm")
async def reset_password_confirm(req: ResetPasswordConfirm):
    user = user_collection.find_one({"email": req.email})
    if not user:
        return {"code": 400, "message": "User not found"}

    if "reset_code" not in user:
        return {"code": 400, "message": "Reset code not sent"}

    hashed_password = bcrypt.hashpw(req.new_password.encode("utf-8"), bcrypt.gensalt())
    user_collection.update_one({"_id": user["_id"]}, {"$set": {"password": hashed_password, "reset_code": ""}})

    return json_serialize(user)


@router.get("/user/all")
async def get_all_users():
    try:
        users = list(user_collection.find())
        return json_serialize(users)
    except Exception as e:
        return {"code": 500, "message": "Failed to retrieve trucks", "error": str(e)}
