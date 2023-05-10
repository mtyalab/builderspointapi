from pydantic import BaseModel


class CreditCard(BaseModel):
    card_name: str
    expiry_date: str
    cvv: str
    card_number: str
    user_id: str
