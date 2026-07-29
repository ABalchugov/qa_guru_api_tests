import requests

def test_search_clubs():
    payload = {"search": "The Monkey's Raincoat"}
    response = requests.get("https://book-club.qa.guru/api/v1/clubs/", params=payload)

    print("\nStatus code:", response.status_code)
    print("Headers:", response.headers)
    print("Body:", response.text)

    assert response.status_code == 200

    body = response.json()

    assert body["count"] == 1
    assert body["results"][0]["bookTitle"] == payload["search"]