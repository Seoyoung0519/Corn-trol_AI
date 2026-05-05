from fastapi import APIRouter, HTTPException
from models.focus_schema import FocusQuestionRequest, FocusQuestionResponse
from services.question_service import create_focus_questions

router = APIRouter()


@router.post("/questions", response_model=FocusQuestionResponse)
def generate_focus_questions(request: FocusQuestionRequest):
    result = create_focus_questions(
        user_id=request.userId,
        record_id=request.recordId,
        topic=request.topic
    )

    if result is None:
        raise HTTPException(
            status_code=404,
            detail="해당 recordId에 해당하는 기록을 찾을 수 없습니다."
        )

    return result