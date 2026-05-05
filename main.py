from fastapi import FastAPI
from routers.focus import router as focus_router

app = FastAPI(
    title="Corn-trol Focus Question API",
    description="집중 모드 질문 생성 API",
    version="1.0.0"
)

app.include_router(focus_router, prefix="/focus", tags=["Focus"])


@app.get("/")
def root():
    return {
        "message": "Corn-trol Focus Question API is running"
    }