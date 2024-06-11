from .implementation import get_last_id as get_last_id_impl
from .implementation import post_erp_data as post_erp_data_impl
from typing import Dict, List
from fastapi import APIRouter, Body, Cookie, Depends, Form, Header, Path, Query, Response, Security, status
from erp_klio_python_server.models.extra_models import TokenModel
from erp_klio_python_server.models.get_last_id400_response import GetLastId400Response
from erp_klio_python_server.models.post_erp_data_request import PostErpDataRequest
router = APIRouter()


@router.get('/{scenarioId}/last-id',
            responses={
                (200): {
                    'model': int,
                    'description': 'OK'
                },
                (400): {
                    'model': GetLastId400Response,
                    'description': 'Bad Request'
                },
                (404): {
                    'model': GetLastId400Response,
                    'description': 'Not Found'
                }
            },
            tags=['default'],
            summary='Get the last-id in the scenario.',
            response_model_by_alias=True)
async def get_last_id(scenarioId: str = Path(
        ...,
        description='UUID of a scenario inserted as a path element of an URI.')
                      ) -> int:
    """### Function This request enables a starting client to get the last id.  ### Usage Call this endpoint with the scenario UUID as the only parameter (in the path). Recover the returned &#x60;last-ID&#x60; and start posting new data with &#x60;id&#x60; set to &#x60;&#x60;last-ID + 1&#x60;&#x60;  ### Returns The response body must be parsed as an integer, which is the last id of the scenario. ### Remarks The &#x60;id&#x60; is a sequential number which must be increased by one for each successful POST operation. """
    return await get_last_id_impl(scenarioId=scenarioId)


@router.post(
    '/{scenarioId}',
    responses={
        (201): {
            'model': str,
            'description': 'Created'
        },
        (400): {
            'model': GetLastId400Response,
            'description': 'Bad Request'
        },
        (404): {
            'model': GetLastId400Response,
            'description': 'Not Found'
        }
    },
    tags=['default'],
    summary='Post data to a specific scenario via the Klio ERP connector.',
    response_model_by_alias=True)
async def post_erp_data(scenarioId: str = Path(
        ...,
        description='UUID of a scenario inserted as a path element of an URI.'
),
                        post_erp_data_request: PostErpDataRequest = Body(
                            None, description='')) -> str:
    """### Function Extends the time-series data of a scenario with a new delivery event tracked by the Cardiff Klio ERP.  ### Usage Call this endpoint as soon as possible when a new delivery of goods occurs.  ### Syntax The syntax of all the string-typed fields is identical to the database extraction supplied as an exemple of ERP data. ### Returns The &#39;Location&#39; response header gives the URI of the new record. ### Remarks The POST operation is idempotent thanks to the &#x60;id&#x60; field."""
    return await post_erp_data_impl(
        scenarioId=scenarioId, post_erp_data_request=post_erp_data_request)
