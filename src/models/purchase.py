from datetime import datetime

from pydantic import BaseModel


class Purchase(BaseModel):
    first_name: str
    last_name: str
    location: str
    email: str
    phone_number: str
    title: str
    rating: int
    delivery_time: str
    cost_price: float
    discount: float
    user_id: str
    purchase_date: datetime = datetime.now()
