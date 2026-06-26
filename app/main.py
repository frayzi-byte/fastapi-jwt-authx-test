from fastapi import FastAPI
from app.routes.user_routes import router as users_router
from app.core.database import Base, engine

app = FastAPI(
    title= "API with FastAPI + SQLite + Dockeer + JWT",
    description= "Simple API for User registration",
    version= "No Version",
)
app.include_router(users_router)

Base.metadata.create_all(bind=engine)

app.include_router(users_router)

@app.get("/")
def root():
    return {"status": "ok"}