from datetime import datetime
from services.llm_service import generate_questions_with_gemini


def create_focus_questions(request):
    current_record = request.currentRecord.model_dump()
    linked_records = [
        record.model_dump()
        for record in request.linkedRecords
    ]

    raw_questions = generate_questions_with_gemini(
        user_id=request.userId,
        record_id=request.recordId,
        topic=request.topic,
        current_record=current_record,
        linked_records=linked_records
    )

    now = datetime.now()
    result = []

    for idx, q in enumerate(raw_questions, start=1):
        result.append({
            "id": idx,
            "recordId": request.recordId,
            "userId": request.userId,
            "topic": request.topic,
            "questionText": q.get("question", ""),
            "createdAt": now
        })

    return {
        "questions": result
    }