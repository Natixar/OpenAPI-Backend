# coding: utf-8

from fastapi.testclient import TestClient


from erp_klio_python_server.models.erp_event import ERPEvent  # noqa: F401
from erp_klio_python_server.models.error import Error  # noqa: F401


def test_get_last_id(client: TestClient):
    """Test case for get_last_id

    Get the last-id in the scenario.
    """

    headers = {
    }
    response = client.request(
        "GET",
        "/{scenarioId}/last-id".format(scenarioId='scenario_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_post_erp_data(client: TestClient):
    """Test case for post_erp_data

    Post data to a specific scenario via the Klio ERP connector.
    """
    erp_event = {"__ref":"examples-openapi.json#/components/examples/postEventExample"}

    headers = {
    }
    response = client.request(
        "POST",
        "/{scenarioId}".format(scenarioId='scenario_id_example'),
        headers=headers,
        json=erp_event,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

