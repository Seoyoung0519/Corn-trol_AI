# 연결 추천 핵심 로직
from app.schemas import RecommendRequest
from app.utils.similarity import cosine_similarity
from app.utils.score import calculate_keyword_score, calculate_final_score


def recommend_connection(request: RecommendRequest):
    source = request.sourceRecord

    if not request.candidateRecords:
        return {
            "userId": request.userId,
            "sourceRecordId": source.recordId,
            "targetRecordId": None,
            "topic": source.topic,
            "similarityScore": 0.0,
            "keywordScore": 0.0,
            "finalScore": 0.0
        }

    best_result = None

    for target in request.candidateRecords:
        similarity_score = round(
            cosine_similarity(source.embedding, target.embedding),
            4
        )

        keyword_score = round(
            calculate_keyword_score(source.keywords, target.keywords),
            4
        )

        final_score = calculate_final_score(similarity_score, keyword_score)

        result = {
            "userId": request.userId,
            "sourceRecordId": source.recordId,
            "targetRecordId": target.recordId,
            "topic": source.topic,
            "similarityScore": similarity_score,
            "keywordScore": keyword_score,
            "finalScore": final_score
        }

        if best_result is None or final_score > best_result["finalScore"]:
            best_result = result

    return best_result