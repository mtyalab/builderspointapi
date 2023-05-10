from pydantic import BaseModel


class CreditCardEdit(BaseModel):
    card_name: str = None
    expiry_date: str = None
    cvv: str = None
    card_number: str = None
    user_id: str = None
