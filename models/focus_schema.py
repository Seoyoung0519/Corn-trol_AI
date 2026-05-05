from pydantic import BaseModel, Field
from typing import List
from datetime import datetime


class CurrentRecord(BaseModel):
    content: str
    keywords: List[str] = Field(default_factory=list)


class LinkedRecord(BaseModel):
    recordId: int
    content: str
    keywords: List[str] = Field(default_factory=list)


class FocusQuestionRequest(BaseModel):
    userId: int
    recordId: int
    topic: str
    currentRecord: CurrentRecord
    linkedRecords: List[LinkedRecord] = Field(default_factory=list)


class QuestionResponseItem(BaseModel):
    id: int
    recordId: int
    userId: int
    topic: str
    questionText: str
    createdAt: datetime


class FocusQuestionResponse(BaseModel):
    questions: List[QuestionResponseItem]