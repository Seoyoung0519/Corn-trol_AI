from datetime import datetime
from services.record_service import (
    get_record_by_id,
    get_linked_records_by_source_id
)
from services.llm_service import generate_questions_with_gemini


def create_focus_questions(user_id: int, record_id: int, topic: str):
    current_record = get_record_by_id(user_id, record_id)

    if not current_record:
        return None

    linked_records = get_linked_records_by_source_id(
        user_id=user_id,
        source_id=record_id
    )

    raw_questions = generate_questions_with_gemini(
        current_record=current_record,
        linked_records=linked_records
    )

    # 🔥 DB 형태로 변환
    result = []
    now = datetime.now()

    for idx, q in enumerate(raw_questions, start=1):
        result.append({
            "id": idx,  # 실제 DB에서는 auto increment
            "recordId": record_id,
            "userId": user_id,
            "topic": topic,
            "questionText": q["question"],
            "createdAt": now
        })

    return {"questions": result}