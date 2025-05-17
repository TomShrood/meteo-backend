from pydantic import BaseModel

class DateInput(BaseModel):
    locatie: str
    data: str
    sezon: str
    ora: str
    statie_id: str
    temperatura: float
    umiditate: float
    presiune: float
    luminozitate: float
    prognoza: str