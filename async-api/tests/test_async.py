import asyncio
import copy
import json

import pytest
from faststream.rabbit import TestRabbitBroker
from app.consumer.subscriber import router

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
    response = test_client.post(f"/async/api/v1/equipment/cpe/{equipment_id}", json=data)
    assert response.status_code == 422
    res = response.json()
    assert res["code"] == 422

@pytest.mark.asyncio
async def test_data(test_client):
    new_data = copy.deepcopy(data)
    new_data.pop("parameters")
    response = test_client.post(f"/async/api/v1/equipment/cpe/123456", json=new_data)
    assert response.status_code == 422
    res = response.json()
    assert res["code"] == 422

@pytest.mark.asyncio
async def test_success(test_client):
    response = test_client.post(f"/async/api/v1/equipment/cpe/123456", json=data)
    assert response.status_code == 200
    res = response.json()
    assert res["code"] == 200
    assert 'taskId' in res
    task_id = res["taskId"]
    assert await test_client.app.state.redis.exists(task_id)

@pytest.mark.asyncio
async def test_update(test_client):
    task_id = "1bbe376d-4da0-49b1-b932-d38c1f9ec954"
    await test_client.app.state.redis.set(
        task_id,
        json.dumps({
            'status': 'running'
        })
    )
    async with TestRabbitBroker(router.broker) as broker:
        await broker.publish(
            dict(task_id=task_id, status="completed", result="ok"),
            "api"
        )
        task = await test_client.app.state.redis.get(task_id)
        status = json.loads(task)["status"]
        assert status == "completed"