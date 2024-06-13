# coding: utf-8

from fastapi.testclient import TestClient


from api_python_server.models.health_get200_response import HealthGet200Response  # noqa: F401


def test_health_get(client: TestClient):
    """Test case for health_get

    Health check
    """

    headers = {
    }
    response = client.request(
        "GET",
        "/health",
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

