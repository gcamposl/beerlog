from beerlog.api import api
from fastapi.testclient import TestClient

client = TestClient(api)


def test_create_beer_via_api():
    response = client.post(
        "/beers",
        json={
            "name": "bahia",
            "style": "KornIPA",
            "flavor": 1,
            "image": 1,
            "cost": 2,
        },
    )
    assert response.status_code == 201
    result = response.json()
    assert result["name"] == "bahia"
    assert result["id"] == 1
