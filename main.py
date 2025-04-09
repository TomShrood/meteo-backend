from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import Base, DateMeteo
from schemas import DateInput  # <-- import nou

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
def primeste_date(data: DateInput, db: Session = Depends(get_db)):
    date = DateMeteo(
        statie_id=data.statie_id,
        temperatura=data.temperatura,
        umiditate=data.umiditate
    )
    db.add(date)
    db.commit()
    return {"status": "Date salvate!"}
    
@app.get("/api/date")
def get_date(db: Session = Depends(get_db)):
    return db.query(DateMeteo).all()
