from datetime import datetime

from pydantic import BaseModel


class OrderEdit(BaseModel):
    first_name: str = None
    last_name: str = None
    location: str = None
    email: str = None
    phone_number: str = None
    title: str = None
    rating: int = None
    delivery_time: str = None
    additional_fee: float = None
    order_no: str = None
    truck_no: str = None
    cost_price: float = None
    discount: float = None
    user_id: str = None
    purchase_date: datetime = datetime.now()
