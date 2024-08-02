from unittest.mock import patch

import pytest as pytest
from starlette.testclient import TestClient

from app.main import app


@pytest.fixture(name="fx_app_client")
def fixture_app_client():
    return TestClient(app)


@patch("app.routers.user.fake_db", {1: {"userId": 1, "name": "John"}})
def test_get_users(fx_app_client):
    response = fx_app_client.get("/users")
    assert response.status_code == 200
    assert response.json() == [{"userId": 1, "name": "John"}]


@pytest.mark.parametrize(
    argnames=["user_id", "expected_response"],
    argvalues=[
        [1, (200, {"userId": 1, "name": "John"})],
        [2, (404, {"message": "User not found."})],
    ],
    ids=["OK", "User Not Found"],
)
@patch("app.routers.user.fake_db", {1: {"userId": 1, "name": "John"}})
def test_get_user(fx_app_client, user_id, expected_response):
    response = fx_app_client.get(f"/users/{user_id}")
    assert response.status_code == expected_response[0]
    assert response.json() == expected_response[1]


@pytest.mark.parametrize(
    argnames=["user", "expected_response"],
    argvalues=[
        [{"userId": 1, "name": "John"}, (200, {"userId": 1, "name": "John"})],
        [{"name": "Jane"}, (400, {"message": "Missing key: 'userId'"})],
    ],
    ids=["OK", "Invalid Schema"],
)
def test_create_user(fx_app_client, user, expected_response):
    response = fx_app_client.post("/users", json=user)
    assert response.status_code == expected_response[0]
    assert response.json() == expected_response[1]


@pytest.mark.parametrize(
    argnames=["user_id", "update_expected_response", "get_expected_response"],
    argvalues=[
        [
            1,
            (200, {"userId": 1, "name": "John Updated", "age": 69}),
            (200, {"userId": 1, "name": "John Updated", "age": 69}),
        ],
        [2, (404, {"message": "User not found."}), (404, {"message": "User not found."})],
    ],
    ids=["OK", "User Not Found"],
)
@patch("app.routers.user.fake_db", {1: {"userId": 1, "name": "John", "age": 69}})
def test_update_user(fx_app_client, user_id, update_expected_response, get_expected_response):
    # Update user
    response = fx_app_client.put(f"/users/{user_id}", json={"userId": 1, "name": "John Updated"})
    assert response.status_code == update_expected_response[0]
    assert response.json() == update_expected_response[1]

    # Re-check if user has been updated
    response = fx_app_client.get(f"/users/{user_id}")
    assert response.status_code == get_expected_response[0]
    assert response.json() == get_expected_response[1]


@pytest.mark.parametrize(
    argnames=["user_id", "delete_expected_response"],
    argvalues=[
        [1, (200, {"message": "OK"})],
        [2, (404, {"message": "User not found."})],
    ],
    ids=["OK", "User Not Found"],
)
@patch("app.routers.user.fake_db", {1: {"userId": 1, "name": "John"}})
def test_delete_user(fx_app_client, user_id, delete_expected_response):
    # Delete user
    response = fx_app_client.delete(f"/users/{user_id}")
    assert response.status_code == delete_expected_response[0]
    assert response.json() == delete_expected_response[1]

    # Re-check if user has been updated
    response = fx_app_client.get(f"/users/{user_id}")
    assert response.status_code == 404
    assert response.json() == {"message": "User not found."}
