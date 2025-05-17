from sqlalchemy import Column, Integer, String, Float
from database import Base

class DateMeteo(Base):
    __tablename__ = "date_meteo"
    id = Column(Integer, primary_key=True, index=True)
    statie_id = Column(String)
    temperatura = Column(Float)
    umiditate = Column(Float)
    luminozitate = Column(Float)
    presiune = Column(Float)
    prognoza = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)
    sezon = Column(String)
    locatie = Column(String)