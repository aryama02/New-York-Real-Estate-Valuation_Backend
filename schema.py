from pydantic import BaseModel


class predict_input(BaseModel):
    BathroomsFull: int
    BathroomsHalf: int
    BedroomsTotal: int
    LivingArea: float