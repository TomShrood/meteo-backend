from sqlalchemy import Column, Integer, Float, String, DateTime
from sqlalchemy.sql import func
from database import Base

class DateMeteo(Base):
    __tablename__ = "date_meteo"
    id = Column(Integer, primary_key=True, index=True)
    statie_id = Column(String)
    temperatura = Column(Float)
    umiditate = Column(Float)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
