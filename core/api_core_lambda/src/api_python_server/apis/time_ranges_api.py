from .implementation import get_data as get_data_impl
from .implementation import get_scenario_ranges as get_scenario_ranges_impl
from typing import Dict, List
from fastapi import APIRouter, Body, Cookie, Depends, Form, Header, Path, Query, Response, Security, status
from api_python_server.models.extra_models import TokenModel
from api_python_server.models.get_scenario_ranges200_response_inner import GetScenarioRanges200ResponseInner
from api_python_server.models.get_scenario_ranges300_response_inner import GetScenarioRanges300ResponseInner
from api_python_server.models.list_clients500_response import ListClients500Response
router = APIRouter()


@router.get('/data/ranges',
            responses={
                (200): {
                    'model': List[GetScenarioRanges200ResponseInner],
                    'description': 'Successful response'
                }
            },
            tags=['Scenario', 'Data', 'Time Ranges', 'Deprecated'],
            summary='Get a cube of data from the default scenario.',
            response_model_by_alias=True)
async def get_data(time_ranges: str = Query(
        None,
        description=
        'JSON array of time range objects, each specifying a start and an end time.'
),
                   scale: str = Query(
                       None,
                       description='Specifies the scale of data aggregation.'),
                   protocol: str = Query(
                       None, description='Specifies the data protocol used.')
                   ) -> List[GetScenarioRanges200ResponseInner]:
    """### Function Retrieve the environmental impact data displayed by the dashboards. The data is discretized at the requested timescale and categorized according to the requested taxonomy.  ### Usage Example: &#x60;&#x60;&#x60; GET /core/v0/data/ranges?time_ranges&#x3D;%5B%7B%22start%22%3A%222023-01-01T00%3A00%3A00+02%3A00%22%2C%22end%22%3A%222023-01-02T00%3A00%3A00+02%3A00%22%7D%2C%7B%22start%22%3A%222023-02-01T00%3A00%3A00+02%3A00%22%2C%22end%22%3A%222023-02-02T00%3A00%3A00+02%3A00%22%7D%5D&amp;scale&#x3D;1d&amp;protocol&#x3D;begesv5 Host: api.natixar.pro  user-agent: curl/7.68.0 accept: */* &#x60;&#x60;&#x60; ### Returns The endpoint returns exactly the same JSON object as /scenarios/{scenarioId}/ranges.  ### Remarks Deprecated. Superseded by /scenarios/{scenarioId}/ranges."""
    return await get_data_impl(time_ranges=time_ranges,
                               scale=scale,
                               protocol=protocol)


@router.get(
    '/scenarios/{scenarioId}/ranges',
    responses={
        (200): {
            'model':
            List[GetScenarioRanges200ResponseInner],
            'description':
            'A representation of the entire data set. Also returned when a specific range is requested using the query parameter time_ranges.'
        },
        (206): {
            'model':
            List[GetScenarioRanges200ResponseInner],
            'description':
            'The ranges were described in the **Range** header(s) and the server returned a representation of requested ranges only. The server always returns code 200 when it successfully serves a request with the **time_ranges** passed as query parameters.'
        },
        (300): {
            'model':
            List[GetScenarioRanges300ResponseInner],
            'description':
            'Multiple choices presents a list of the protocols available in the back-end.  It will typically be returned as the first response to a request with no time range, no time scale and no protocol, which conveys the available protocols to the front-end tool.'
        },
        (302): {
            'description': ''
        },
        (304): {
            'description': ''
        },
        (401): {
            'description': ''
        },
        (403): {
            'description': ''
        },
        (404): {
            'model': ListClients500Response,
            'description': 'Not Found'
        },
        (405): {
            'description': ''
        },
        (406): {
            'description': ''
        },
        (413): {
            'description':
            'Returned when the aggregated range request result in more than 10080 time intervals.'
        },
        (416): {
            'model':
            ListClients500Response,
            'description':
            'Returned by the endpoint /scenarios/{id}/ranges when a range in the Accept header, does not follow the prescribed format.'
        },
        (500): {
            'model': ListClients500Response,
            'description': 'Internal Server Error'
        }
    },
    tags=['Scenario', 'Time Ranges'],
    summary='Get a range of data from the scenario.',
    response_model_by_alias=True)
async def get_scenario_ranges(
        scenarioId: str = Path(
            ...,
            description=
            'UUID of a scenario inserted as a path element of an URI.'),
        range: str = Header(
            None,
            description=
            'Indicates which part of the scenario should be returned.'),
        accept: str = Header(
            None,
            description='Use the Accept header to specify the protocol.'),
        time_ranges: str = Query(
            None,
            description=
            'JSON array of time range objects, each specifying a start and an end time.'
        ),
        scale: str = Query(
            None,
            description=
            'Specifies the scale of data aggregation. Deprecated. Specify the unit in a Range header instead.'
        ),
        protocol: str = Query(
            None,
            description=
            'Use a query parameter to specify the protocol. This method is discouraged in favor of the standard **Accept** header.'
        )) -> List[GetScenarioRanges200ResponseInner]:
    """### Function Retrieve the environmental impact data displayed by the dashboards. The data for the requested time **range** is discretized at the requested time **scale** and categorized according to the requested **protocol**.  if the time range and the scale are not defined, the back-end will return the whole date at a suitable time scale, but if the protocol isn&#39;t defined, the answer will be HTTP 300, Multiple Choices, to elicit a choice.  ### Usage Example: &#x60;&#x60;&#x60; GET /core/v1/scenarios/7fd937d5-1eb2-4028-859d-44cfd4e98a12/ranges?time_ranges&#x3D;%5B%7B%22start%22%3A%222023-01-01T00%3A00%3A00+02%3A00%22%2C%22end%22%3A%222023-01-02T00%3A00%3A00+02%3A00%22%7D%2C%7B%22start%22%3A%222023-02-01T00%3A00%3A00+02%3A00%22%2C%22end%22%3A%222023-02-02T00%3A00%3A00+02%3A00%22%7D%5D&amp;scale&#x3D;1d&amp;protocol&#x3D;begesv5 Host: api.natixar.pro  user-agent: curl/7.68.0 accept: */* &#x60;&#x60;&#x60; ### Returns The endpoint returns a JSON array of one large object per requested time range, in the same order as the request.  ### Remarks Supersedes /scenarios/{scenarioId}/ranges."""
    return await get_scenario_ranges_impl(scenarioId=scenarioId,
                                          range=range,
                                          accept=accept,
                                          time_ranges=time_ranges,
                                          scale=scale,
                                          protocol=protocol)
