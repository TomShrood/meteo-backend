from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import Base, DateMeteo

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def root():
    return {"message": "API-ul meteo funcționează! 🔥"}

@app.post("/api/date")
def primeste_date(statie_id: str, temperatura: float, umiditate: float, db: Session = Depends(get_db)):
    date = DateMeteo(
        statie_id=statie_id,
        temperatura=temperatura,
        umiditate=umiditate
    )
    db.add(date)
    db.commit()
    return {"status": "Date salvate!"}
