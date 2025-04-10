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
    docs_url=None,  # Dezactivează documentația implicită
    redoc_url=None,
    openapi_url="/openapi.json"
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

# ✅ Docs route fix pentru Render
@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html(request: Request):
    root_path = request.scope.get("root_path", "").rstrip("/")
    return get_swagger_ui_html(
        openapi_url=f"{root_path}/openapi.json",
        title=f"{app.title} - Swagger UI",
        oauth2_redirect_url=None,
        swagger_favicon_url=None
    )

# ✅ Redoc route fix pentru Render
@app.get("/redoc", include_in_schema=False)
async def custom_redoc_html(request: Request):
    root_path = request.scope.get("root_path", "").rstrip("/")
    return get_redoc_html(
        openapi_url=f"{root_path}/openapi.json",
        title=f"{app.title} - ReDoc"
    )
