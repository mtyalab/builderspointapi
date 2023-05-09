from pydantic import BaseModel


class Material(BaseModel):
    title: str
    rating: float
    delivery_time: str
    thumbnail_url: str
    cost_price: float
    discount: float
    additional_fees: float
