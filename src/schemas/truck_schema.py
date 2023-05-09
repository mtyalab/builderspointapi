from pydantic import BaseModel


class TruckEdit(BaseModel):
    make: str = None
    model: str = None
    year: int = None
    color: str = None
    mileage: int = None
    numberPlate: str = None


