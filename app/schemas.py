# Request / Response 구조 정의
from typing import List, Optional
from pydantic import BaseModel


class RecordData(BaseModel):
    recordId: int
    topic: str
    keywords: List[str]
    embedding: List[float]


class RecommendRequest(BaseModel):
    userId: int
    sourceRecord: RecordData
    candidateRecords: List[RecordData]


class RecommendResponse(BaseModel):
    userId: int
    sourceRecordId: int
    targetRecordId: Optional[int] = None
    topic: str
    similarityScore: float
    keywordScore: float
    finalScore: float