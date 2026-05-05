import os
import json
import time
from dotenv import load_dotenv
from google import genai

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=GEMINI_API_KEY) if GEMINI_API_KEY else None


def build_question_prompt(current_record: dict, linked_records: list[dict]) -> str:
    if linked_records:
        linked_text = "\n".join([
            f'- recordId: {record["recordId"]}\n'
            f'  내용: {record["content"]}\n'
            f'  키워드: {", ".join(record["keywords"])}'
            for record in linked_records
        ])
    else:
        linked_text = "연결된 기록 없음. 현재 선택한 기록만 기반으로 질문을 생성한다."

    return f"""
너는 사용자의 산만한 생각을 정리하고 집중 몰입을 돕는 질문 생성 AI다.

[규칙]
1. 질문은 반드시 2~3개만 생성한다.
2. 연결된 기록이 있으면 현재 기록과 연결된 기록을 함께 참고한다.
3. 연결된 기록이 없으면 현재 기록의 content, topic, keywords만 참고한다.
4. 질문은 사용자가 바로 답변할 수 있도록 구체적으로 작성한다.
5. 사용자를 평가하거나 비판하지 않는다.
6. 반드시 한국어로 작성한다.
7. 반드시 JSON 형식만 반환한다.
8. 마크다운 코드블록은 절대 사용하지 않는다.

[현재 선택한 기록]
recordId: {current_record["recordId"]}
topic: {current_record["topic"]}
content: {current_record["content"]}
keywords: {", ".join(current_record["keywords"])}

[연결된 기록들]
{linked_text}

[출력 형식]
{{
  "questions": [
    {{
      "type": "구체화",
      "question": "..."
    }},
    {{
      "type": "연결",
      "question": "..."
    }},
    {{
      "type": "확장",
      "question": "..."
    }}
  ]
}}
"""


def clean_json_text(text: str) -> str:
    text = text.strip()

    if text.startswith("```json"):
        text = text.replace("```json", "", 1).replace("```", "").strip()
    elif text.startswith("```"):
        text = text.replace("```", "").strip()

    return text

def generate_questions_with_gemini(current_record: dict, linked_records: list[dict]):
    if not client:
        return generate_mock_questions(current_record, linked_records)

    prompt = build_question_prompt(current_record, linked_records)

    models = [
    "gemini-3-flash-preview"
    ]
    

    for model_name in models:
        for attempt in range(3):
            try:
                response = client.models.generate_content(
                    model=model_name,
                    contents=prompt
                )

                text = clean_json_text(response.text)
                data = json.loads(text)

                return data.get(
                    "questions",
                    generate_mock_questions(current_record, linked_records)
                )

            except Exception as e:
                print(f"Gemini error / model={model_name} / attempt={attempt + 1}:", e)
                time.sleep(1.5 * (attempt + 1))

    return generate_mock_questions(current_record, linked_records)

def generate_mock_questions(current_record: dict, linked_records: list[dict]):
    return [
        {
            "type": "구체화",
            "question": f"'{current_record['topic']}'에 대해 지금 가장 먼저 정리하고 싶은 생각은 무엇인가요?"
        },
        {
            "type": "연결",
            "question": "현재 기록과 연결된 기록들 사이에서 반복적으로 등장하는 문제나 키워드는 무엇인가요?"
        },
        {
            "type": "확장",
            "question": "이 생각을 실제 행동이나 아이디어로 발전시킨다면 가장 먼저 시도할 수 있는 것은 무엇인가요?"
        }
    ]