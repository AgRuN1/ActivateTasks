import copy

import pytest


data = {
    "timeoutInSeconds": 0,
    "parameters": {
        "username": "admin",
        "password": "admin",
        "vlan": 534,
        "interfaces": [1, 2, 3, 4]
    }
}

@pytest.mark.asyncio
@pytest.mark.parametrize("equipment_id", [
    "12345",
    "123456.",
    "abcdшf12",
    "abc-def",
    "a"
])
async def test_equipment_id(test_client, equipment_id):
    response = test_client.post(f"/sync/api/v1/equipment/cpe/{equipment_id}", json=data)
    assert response.status_code == 422
    res = response.json()
    assert res["code"] == 422

@pytest.mark.asyncio
async def test_data(test_client):
    new_data = copy.deepcopy(data)
    new_data.pop("parameters")
    response = test_client.post(f"/sync/api/v1/equipment/cpe/123456", json=new_data)
    assert response.status_code == 422
    res = response.json()
    assert res["code"] == 422

@pytest.mark.asyncio
async def test_success(test_client):
    response = test_client.post(f"/sync/api/v1/equipment/cpe/123456", json=data)
    assert response.status_code == 200
    assert response.json() == {"code": 200, "message": "success"}

@pytest.mark.asyncio
async def test_not_found(test_client):
    response = test_client.post(f"/sync/api/v1/equipment/cpe/", json=data)
    assert response.status_code == 404
    assert response.json() == {"code": 404, "message": "The requested equipment is not found"}