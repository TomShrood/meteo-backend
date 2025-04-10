from fastapi import FastAPI, Depends, Request
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import Base, DateMeteo
from schemas import DateInput
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.openapi.utils import get_openapi

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API Meteo",
    description="Colectare și afișare date meteo",
    version="1.0",
    openapi_url="/openapi.json",  # docs_url și redoc_url scoase pentru a le redefini manual
    docs_url=None,
    redoc_url=None
)

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

# ✅ Documentație Swagger (custom pentru Render)
@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html(req: Request):
    root_path = req.scope.get("root_path", "").rstrip("/")
    openapi_url = root_path + app.openapi_url
    return get_swagger_ui_html(openapi_url=openapi_url, title=app.title)

# ✅ Redoc manual
from fastapi.openapi.docs import get_redoc_html

@app.get("/redoc", include_in_schema=False)
async def redoc_html(req: Request):
    root_path = req.scope.get("root_path", "").rstrip("/")
    openapi_url = root_path + app.openapi_url
    return get_redoc_html(openapi_url=openapi_url, title=app.title)
