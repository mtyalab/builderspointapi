from pydantic import BaseModel


class User(BaseModel):
    first_name: str
    last_name: str
    middle_name: str
    role: str
    phone_number: str
    email: str
    password: str


class UserLogin(BaseModel):
    email: str
    password: str


