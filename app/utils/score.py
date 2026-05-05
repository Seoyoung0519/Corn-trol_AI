# 키워드 점수, 최종 점수 계산
def calculate_keyword_score(source_keywords, target_keywords):
    source_set = set(source_keywords)
    target_set = set(target_keywords)

    if not source_set or not target_set:
        return 0.0

    return len(source_set & target_set) / len(source_set | target_set)


def calculate_final_score(similarity_score, keyword_score):
    return round(similarity_score * 0.7 + keyword_score * 0.3, 4)