from api_python_server.implementation import create_scenario as create_scenario_impl
from api_python_server.implementation import delete_scenario as delete_scenario_impl
from api_python_server.implementation import get_data as get_data_impl
from api_python_server.implementation import get_scenario as get_scenario_impl
from api_python_server.implementation import get_scenario_ranges as get_scenario_ranges_impl
from api_python_server.implementation import list_scenarios as list_scenarios_impl
from api_python_server.implementation import get_db
from typing import Dict, List
from fastapi import APIRouter, Body, Cookie, Depends, Form, Header, Path, Query, Response, Security, status
from api_python_server.models.extra_models import TokenModel
from api_python_server.models.create_scenario_request import CreateScenarioRequest
from api_python_server.models.get_scenario_ranges200_response_inner import GetScenarioRanges200ResponseInner
from api_python_server.models.get_scenario_ranges300_response_inner import GetScenarioRanges300ResponseInner
from api_python_server.models.list_clients500_response import ListClients500Response
from api_python_server.models.list_scenarios200_response_inner import ListScenarios200ResponseInner
from api_python_server.security_api import get_token_client_api_key

# Get an API router
router = APIRouter()


@router.post('/scenarios',
             responses={
                 (201): {
                     'model': ListScenarios200ResponseInner,
                     'description': 'Created scenario'
                 },
                 (500): {
                     'model': ListClients500Response,
                     'description': 'Internal Server Error'
                 }
             },
             tags=['Scenario'],
             summary='Create a new scenario',
             response_model_by_alias=True)
async def create_scenario(
        create_scenario_request: CreateScenarioRequest = Body(None,
                                                              description=''),
        token_client_api_key: TokenModel = Security(get_token_client_api_key)
) -> ListScenarios200ResponseInner:
    """### Definition A scenario represents a particular time line, with time series data on the activity.  ### Architecture A scenario may be a derivative of another one at a given date. A such, it acts as another layer of impact causes."""
    return await create_scenario_impl(
        create_scenario_request=create_scenario_request,
        token_client_api_key=token_client_api_key)


@router.delete('/scenarios/{scenarioId}',
               responses={
                   (204): {
                       'description': 'Scenario deleted'
                   },
                   (404): {
                       'model': ListClients500Response,
                       'description': 'Not Found'
                   },
                   (500): {
                       'model': ListClients500Response,
                       'description': 'Internal Server Error'
                   }
               },
               tags=['Scenario'],
               summary='Delete a scenario',
               response_model_by_alias=True)
async def delete_scenario(scenarioId: str = Path(
        ...,
        description='UUID of a scenario inserted as a path element of an URI.'
),
                          token_client_api_key: TokenModel = Security(
                              get_token_client_api_key)) -> None:
    """Delete a secondary scenario. The default one cannot be deleted."""
    return await delete_scenario_impl(
        scenarioId=scenarioId, token_client_api_key=token_client_api_key)


@router.get('/data/ranges',
            responses={
                (200): {
                    'model': List[GetScenarioRanges200ResponseInner],
                    'description': 'Successful response'
                }
            },
            tags=['Scenario'],
            summary='Get a cube of data from the default scenario.',
            response_model_by_alias=True)
async def get_data(
    time_ranges: str = Query(
        None,
        description='JSON array of time range objects, each specifying a start and an end time.'
    ),
    scale: str = Query(None, description='Specifies the scale of data aggregation.'),
    protocol: str = Query(None, description='Specifies the data protocol used.'),
    token_client_api_key: TokenModel = Security(get_token_client_api_key)
) -> List[GetScenarioRanges200ResponseInner]:
    """### Function Retrieve the environmental impact data displayed by the dashboards. The data is discretized at the requested timescale and categorized according to the requested taxonomy.  ### Usage Example: &#x60;&#x60;&#x60; GET /core/v0/data/ranges?time_ranges&#x3D;%5B%7B%22start%22%3A%222023-01-01T00%3A00%3A00+02%3A00%22%2C%22end%22%3A%222023-01-02T00%3A00%3A00+02%3A00%22%7D%2C%7B%22start%22%3A%222023-02-01T00%3A00%3A00+02%3A00%22%2C%22end%22%3A%222023-02-02T00%3A00%3A00+02%3A00%22%7D%5D&amp;scale&#x3D;1d&amp;protocol&#x3D;begesv5 Host: api.natixar.pro  user-agent: curl/7.68.0 accept: */* &#x60;&#x60;&#x60; ### Returns The endpoint returns exactly the same JSON object as /scenarios/{scenarioId}/ranges.  ### Remarks Deprecated. Superseded by /scenarios/{scenarioId}/ranges."""
    return await get_data_impl(time_ranges=time_ranges,
               scale=scale,
               protocol=protocol,
               token_client_api_key=token_client_api_key)


@router.get('/scenarios/{scenarioId}',
            responses={
                (200): {
                    'model': ListScenarios200ResponseInner,
                    'description': 'A specific scenario'
                },
                (404): {
                    'model': ListClients500Response,
                    'description': 'Not Found'
                },
                (500): {
                    'model': ListClients500Response,
                    'description': 'Internal Server Error'
                }
            },
            tags=['Scenario'],
            summary='Get a specific scenario',
            response_model_by_alias=True)
async def get_scenario(scenarioId: str = Path(
        ...,
        description='UUID of a scenario inserted as a path element of an URI.'
),
                       token_client_api_key: TokenModel = Security(
                           get_token_client_api_key)
                       ) -> ListScenarios200ResponseInner:
    """### Definition A scenario represents a particular time line, with time series data on the activity.  ### Architecture A scenario may be a derivative of another one at a given date. A such, it acts as another layer of impact causes. For example, a child scenario depicting the installation of a solar water heater could include negative natural gas consumptions equivalent to the heat acquired by solar irradiation, based on a meteorological model.  ### Naming Scheme  A scenario id is an UUID4, equivalent to 40 hexadecimal digits."""
    return await get_scenario_impl(scenarioId=scenarioId,
                                   token_client_api_key=token_client_api_key)


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
    tags=['Scenario'],
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
        ),
        token_client_api_key: TokenModel = Security(get_token_client_api_key)
) -> List[GetScenarioRanges200ResponseInner]:
    """### Function Retrieve the environmental impact data displayed by the dashboards. The data for the requested time **range** is discretized at the requested time **scale** and categorized according to the requested **protocol**.  if the time range and the scale are not defined, the back-end will return the whole date at a suitable time scale, but if the protocol isn&#39;t defined, the answer will be HTTP 300, Multiple Choices, to elicit a choice.  ### Usage Example: &#x60;&#x60;&#x60; GET /core/v1/scenarios/7fd937d5-1eb2-4028-859d-44cfd4e98a12/ranges?time_ranges&#x3D;%5B%7B%22start%22%3A%222023-01-01T00%3A00%3A00+02%3A00%22%2C%22end%22%3A%222023-01-02T00%3A00%3A00+02%3A00%22%7D%2C%7B%22start%22%3A%222023-02-01T00%3A00%3A00+02%3A00%22%2C%22end%22%3A%222023-02-02T00%3A00%3A00+02%3A00%22%7D%5D&amp;scale&#x3D;1d&amp;protocol&#x3D;begesv5 Host: api.natixar.pro  user-agent: curl/7.68.0 accept: */* &#x60;&#x60;&#x60; ### Returns The endpoint returns a JSON array of one large object per requested time range, in the same order as the request.  ### Remarks Supersedes /scenarios/{scenarioId}/ranges."""
    return await get_scenario_ranges_impl(
        scenarioId=scenarioId,
        range=range,
        accept=accept,
        time_ranges=time_ranges,
        scale=scale,
        protocol=protocol,
        token_client_api_key=token_client_api_key)


@router.get('/scenarios',
            responses={
                (200): {
                    'model': List[ListScenarios200ResponseInner],
                    'description': 'A list of scenarios'
                },
                (500): {
                    'model': ListClients500Response,
                    'description': 'Internal Server Error'
                }
            },
            tags=['Scenario'],
            summary='List all scenarios',
            response_model_by_alias=True)
async def list_scenarios(token_client_api_key: TokenModel = Security(
        get_token_client_api_key)) -> List[ListScenarios200ResponseInner]:
    """### Function List all scenarios. When called with a client API key, only list that client&#39;s scenarios.  ### Format The scenarios are returned in a list of objects following the Scenario schema."""
    return await list_scenarios_impl(token_client_api_key=token_client_api_key)
