from data.mock_records import MOCK_RECORDS
from data.mock_links import MOCK_LINKS


def get_record_by_id(user_id: int, record_id: int):
    for record in MOCK_RECORDS:
        if record["userId"] == user_id and record["recordId"] == record_id:
            return record
    return None


def get_linked_records_by_source_id(user_id: int, source_id: int):
    target_ids = [
        link["targetId"]
        for link in MOCK_LINKS
        if link["sourceId"] == source_id
    ]

    return [
        record for record in MOCK_RECORDS
        if record["userId"] == user_id
        and record["recordId"] in target_ids
    ]