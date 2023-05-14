from pymongo import MongoClient
from pymongo.collection import Collection

# DB_URL = "mongodb://127.0.0.1:27017"
DB_URL = "mongodb+srv://kmuytab:kaweereze2023Dayz@cluster0.mwciw0w.mongodb.net/test"
DB_NAME = "builders_point_db"
client = MongoClient(DB_URL, maxPoolSize=50)


def get_db():
    db_client = MongoClient("mongodb://127.0.0.1:27017")
    db = db_client[DB_NAME]
    return db


def get_user_collection() -> Collection:
    return client[DB_NAME]["users"]


def get_material_collection() -> Collection:
    return client[DB_NAME]["materials"]


def get_credit_card_collection() -> Collection:
    return client[DB_NAME]["credit_cards"]


def get_purchase_collection() -> Collection:
    return client[DB_NAME]["purchases"]


def get_order_collection() -> Collection:
    return client[DB_NAME]["orders"]


def get_reset_password_request_collection() -> Collection:
    return client[DB_NAME]["reset_password_request"]


def get_reset_password_confirm_collection() -> Collection:
    return client[DB_NAME]["reset_password_confirm"]


def get_rating_collection() -> Collection:
    return client[DB_NAME]["rating"]


def get_trucks_collection() -> Collection:
    return client[DB_NAME]["trucks"]
