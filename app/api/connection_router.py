from fastapi import APIRouter
from app.schemas import RecommendRequest, RecommendResponse
from app.services.connection_service import recommend_connection

router = APIRouter(
    prefix="/connections",
    tags=["Connection"]
)

@router.post("/recommend", response_model=RecommendResponse)
def recommend_connection_api(request: RecommendRequest):
    return recommend_connection(request)