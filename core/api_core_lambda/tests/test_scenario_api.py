# coding: utf-8

from fastapi.testclient import TestClient


from api_python_server.models.create_scenario_request import CreateScenarioRequest  # noqa: F401
from api_python_server.models.get_scenario_ranges200_response_inner import GetScenarioRanges200ResponseInner  # noqa: F401
from api_python_server.models.get_scenario_ranges300_response_inner import GetScenarioRanges300ResponseInner  # noqa: F401
from api_python_server.models.list_clients500_response import ListClients500Response  # noqa: F401
from api_python_server.models.list_scenarios200_response_inner import ListScenarios200ResponseInner  # noqa: F401


def test_create_scenario(client: TestClient):
    """Test case for create_scenario

    Create a new scenario
    """
    create_scenario_request = {"title":"Installation of a solar water heater"}

    headers = {
        "admin_api_key": "special-key",
        "client_api_key": "special-key",
    }
    response = client.request(
        "POST",
        "/scenarios",
        headers=headers,
        json=create_scenario_request,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_delete_scenario(client: TestClient):
    """Test case for delete_scenario

    Delete a scenario
    """

    headers = {
        "admin_api_key": "special-key",
        "client_api_key": "special-key",
    }
    response = client.request(
        "DELETE",
        "/scenarios/{scenarioId}".format(scenarioId='deadbeef-1234-abcd-5678-1234567890ab'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_data(client: TestClient):
    """Test case for get_data

    Get a cube of data from the default scenario.
    """
    params = [("time_ranges", '[{\"start\":\"2023-01-01T00:00:00+02:00\",\"end\":\"2023-01-02T00:00:00+02:00\"},{\"start\":\"2023-02-01T00:00:00+02:00\",\"end\":\"2023-02-02T00:00:00+02:00\"}]'),     ("scale", '1d'),     ("protocol", 'begesv5')]
    headers = {
        "client_api_key": "special-key",
    }
    response = client.request(
        "GET",
        "/data/ranges",
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_scenario(client: TestClient):
    """Test case for get_scenario

    Get a specific scenario
    """

    headers = {
        "admin_api_key": "special-key",
        "client_api_key": "special-key",
    }
    response = client.request(
        "GET",
        "/scenarios/{scenarioId}".format(scenarioId='deadbeef-1234-abcd-5678-1234567890ab'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_scenario_ranges(client: TestClient):
    """Test case for get_scenario_ranges

    Get a range of data from the scenario.
    """
    params = [("time_ranges", '[{\"start\":\"2023-01-01T00:00:00+02:00\",\"end\":\"2023-01-02T00:00:00+02:00\"},{\"start\":\"2023-02-01T00:00:00+02:00\",\"end\":\"2023-02-02T00:00:00+02:00\"}]'),     ("scale", '1d'),     ("protocol", 'ghgprotocol')]
    headers = {
        "range": 'Range: 1m=2021-01-01T00:00:00+0100-2022-01-01T00:00:00+0100',
        "accept": 'Accept: application/vnd.ntxr.co2track.v1+json; version=ghgprotocol',
        "client_api_key": "special-key",
    }
    response = client.request(
        "GET",
        "/scenarios/{scenarioId}/ranges".format(scenarioId='deadbeef-1234-abcd-5678-1234567890ab'),
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_scenarios(client: TestClient):
    """Test case for list_scenarios

    List all scenarios
    """

    headers = {
        "admin_api_key": "special-key",
        "client_api_key": "special-key",
    }
    response = client.request(
        "GET",
        "/scenarios",
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

