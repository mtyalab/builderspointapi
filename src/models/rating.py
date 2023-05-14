from pydantic import BaseModel


class Rating(BaseModel):
    count: float
    truck_id: str
