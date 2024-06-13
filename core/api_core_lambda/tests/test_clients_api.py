# coding: utf-8

from fastapi.testclient import TestClient


from api_python_server.models.list_clients200_response_inner import ListClients200ResponseInner  # noqa: F401
from api_python_server.models.list_clients500_response import ListClients500Response  # noqa: F401


def test_create_client(client: TestClient):
    """Test case for create_client

    Create a new client
    """
    list_clients200_response_inner = {"name":"Agro Novae Industrie, SAS","id":1}

    headers = {
        "admin_api_key": "special-key",
    }
    response = client.request(
        "POST",
        "/clients",
        headers=headers,
        json=list_clients200_response_inner,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_delete_client(client: TestClient):
    """Test case for delete_client

    Delete a client by ID
    """

    headers = {
        "admin_api_key": "special-key",
    }
    response = client.request(
        "DELETE",
        "/clients/{clientId}".format(clientId='client_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_client(client: TestClient):
    """Test case for get_client

    Get a client by ID
    """

    headers = {
        "admin_api_key": "special-key",
    }
    response = client.request(
        "GET",
        "/clients/{clientId}".format(clientId='client_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_clients(client: TestClient):
    """Test case for list_clients

    List all clients
    """

    headers = {
        "admin_api_key": "special-key",
    }
    response = client.request(
        "GET",
        "/clients",
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_update_client(client: TestClient):
    """Test case for update_client

    Update a client by ID
    """
    list_clients200_response_inner = {"name":"Agro Novae Industrie, SAS","id":1}

    headers = {
        "admin_api_key": "special-key",
    }
    response = client.request(
        "PUT",
        "/clients/{clientId}".format(clientId='client_id_example'),
        headers=headers,
        json=list_clients200_response_inner,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

