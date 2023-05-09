from pydantic import BaseModel


class Truck(BaseModel):
    make: str
    model: str
    year: int
    color: str
    mileage: int
    numberPlate: str
