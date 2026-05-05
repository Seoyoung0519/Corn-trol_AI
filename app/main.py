from fastapi import FastAPI

from app.api.connection_router import router as connection_router
from app.config import settings

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION
)

app.include_router(connection_router)


@app.get("/")
def root():
    return {
        "message": "Corn-trol AI Server is running",
        "env": settings.ENV
    }


@app.get("/health")
def health_check():
    return {
        "status": "ok"
    }