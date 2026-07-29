import requests

def test_page_size_clubs():
    payload = {"page_size": 2}
    response = requests.get("https://book-club.qa.guru/api/v1/clubs/", params=payload)

    print("\nStatus code:", response.status_code)
    print("Headers:", response.headers)
    print("Body:", response.text)

    assert response.status_code == 200

    body = response.json()

    assert len(body["results"]) == payload["page_size"]