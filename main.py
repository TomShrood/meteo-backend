from fastapi import FastAPI, Depends, Request
from fastapi.openapi.docs import get_swagger_ui_html, get_redoc_html
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import Base, DateMeteo
from schemas import DateInput

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API Meteo",
    description="Colectare și afișare date meteo",
    version="1.0",
    openapi_url="/openapi.json"
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@app.get("/")
def root(db: Session = Depends(get_db)):
    return db.query(DateMeteo).all()


@app.post("/api/date")
def primeste_date(data: DateInput, db: Session = Depends(get_db)):
    date = DateMeteo(
        statie_id=data.statie_id,
        temperatura=data.temperatura,
        umiditate=data.umiditate,
        luminozitate=data.luminozitate,
        presiune=data.presiune,
        prognoza=data.prognoza,
        sezon=data.sezon,
        locatie=data.locatie,
        ora=data.ora,
        data=data.data,
        viteza_vant=data.viteza_vant
    )
    db.add(date)
    db.commit()
    return {"status": "Date salvate!"}

@app.get("/api/date")
def get_date(db: Session = Depends(get_db)):
    return db.query(DateMeteo).all()
    
@app.get("/api/date/ultimele/{n}")
def get_ultimele_n(n: int, db: Session = Depends(get_db)):
    return db.query(DateMeteo).order_by(DateMeteo.id.desc()).limit(n).all()[::-1]

