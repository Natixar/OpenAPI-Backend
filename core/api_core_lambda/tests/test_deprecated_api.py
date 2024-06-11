# coding: utf-8

from fastapi.testclient import TestClient


from api_python_server.models.get_scenario_ranges200_response_inner import GetScenarioRanges200ResponseInner  # noqa: F401


def test_get_data(client: TestClient):
    """Test case for get_data

    Get a cube of data from the default scenario.
    """
    params = [("time_ranges", '[{\"start\":\"2023-01-01T00:00:00+02:00\",\"end\":\"2023-01-02T00:00:00+02:00\"},{\"start\":\"2023-02-01T00:00:00+02:00\",\"end\":\"2023-02-02T00:00:00+02:00\"}]'),     ("scale", '1d'),     ("protocol", 'begesv5')]
    headers = {
    }
    response = client.request(
        "GET",
        "/data/ranges",
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

