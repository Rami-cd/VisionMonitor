from fastapi import FastAPI
from routes import router
from core.config import settings

app = FastAPI(
    title="Urban Video Analytics API"
)

@app.get("/model-info") 
def get_info():
    return {
        "model": settings.tracker_system.name,
        "version": settings.tracker_system.version
    }

app.include_router(router)