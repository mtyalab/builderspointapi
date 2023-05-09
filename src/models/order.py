from datetime import datetime

from pydantic import BaseModel


class Order(BaseModel):
    first_name: str
    last_name: str
    location: str
    email: str
    phone_number: str
    title: str
    rating: int
    delivery_time: str
    cost_price: float
    additional_fee: float
    order_no: str
    truck_no: str
    discount: float
    user_id: str
    purchase_date: datetime = datetime.now()
