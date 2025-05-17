from pydantic import BaseModel

class DateInput(BaseModel):
    statie_id: str
    temperatura: float
    umiditate: float
    luminozitate: float
    presiune: float
    prognoza: str
    sezon: str
    locatie: str