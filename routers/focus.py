from fastapi import APIRouter
from models.focus_schema import FocusQuestionRequest, FocusQuestionResponse
from services.question_service import create_focus_questions

router = APIRouter()


@router.post("/questions", response_model=FocusQuestionResponse)
def generate_focus_questions(request: FocusQuestionRequest):
    return create_focus_questions(request)