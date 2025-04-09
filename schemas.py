from pydantic import BaseModel

class DateInput(BaseModel):
    statie_id: str
    temperatura: float
    umiditate: float
