import requests

from jsonschema import validate
from schemas.get_clubs_schema import get_clubs_schema


def test_total_count_with_schema_validation():
    response = requests.get("https://book-club.qa.guru/api/v1/clubs/")

    print("\nStatus code:", response.status_code)
    print("Headers:", response.headers)
    print("Body:", response.text)

    assert response.status_code == 200

    body = response.json()
    total_count = body["count"]

    response_all = requests.get("https://book-club.qa.guru/api/v1/clubs/", params={"page_size": total_count})

    print("\nStatus code:", response.status_code)
    print("Headers:", response.headers)
    print("Body:", response.text)

    assert response_all.status_code == 200

    body_all = response_all.json()
    validate(body_all, schema=get_clubs_schema)
    assert body_all["count"] == len(body_all["results"])