from pydantic import BaseModel
from typing import List
from datetime import datetime


class FocusQuestionRequest(BaseModel):
    userId: int
    recordId: int
    topic: str


class QuestionResponseItem(BaseModel):
    id: int
    recordId: int
    userId: int
    topic: str
    questionText: str
    createdAt: datetime


class FocusQuestionResponse(BaseModel):
    questions: List[QuestionResponseItem]