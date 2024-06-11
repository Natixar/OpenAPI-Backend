from .implementation import get_data as get_data_impl
from typing import Dict, List
from fastapi import APIRouter, Body, Cookie, Depends, Form, Header, Path, Query, Response, Security, status
from api_python_server.models.extra_models import TokenModel
from api_python_server.models.get_scenario_ranges200_response_inner import GetScenarioRanges200ResponseInner
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
