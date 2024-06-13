from api_python_server.implementation import create_client as create_client_impl
from api_python_server.implementation import delete_client as delete_client_impl
from api_python_server.implementation import get_client as get_client_impl
from api_python_server.implementation import list_clients as list_clients_impl
from api_python_server.implementation import update_client as update_client_impl
from typing import Dict, List
from fastapi import APIRouter, Body, Cookie, Depends, Form, Header, Path, Query, Response, Security, status
from api_python_server.models.extra_models import TokenModel
from api_python_server.models.list_clients200_response_inner import ListClients200ResponseInner
from api_python_server.models.list_clients500_response import ListClients500Response
from api_python_server.security_api import get_token_admin_api_key
router = APIRouter()


@router.post(
    '/clients',
    responses={
        (201): {
            'model':
            ListClients200ResponseInner,
            'description':
            'Successfully created a client. URN is returned in the Location header'
        },
        (400): {
            'model': ListClients500Response,
            'description': 'Invalid input provided'
        },
        (401): {
            'model': ListClients500Response,
            'description': 'Unauthorized'
        },
        (500): {
            'model': ListClients500Response,
            'description': 'Internal Server Error'
        }
    },
    tags=['Clients'],
    summary='Create a new client',
    response_model_by_alias=True)
async def create_client(
        list_clients200_response_inner: ListClients200ResponseInner = Body(
            None, description=''),
        token_admin_api_key: TokenModel = Security(get_token_admin_api_key)
) -> ListClients200ResponseInner:
    """Create a new client with the provided name and description"""
    return await create_client_impl(
        list_clients200_response_inner=list_clients200_response_inner,
        token_admin_api_key=token_admin_api_key)


@router.delete('/clients/{clientId}',
               responses={
                   (204): {
                       'description': 'Successfully deleted the client'
                   },
                   (404): {
                       'description': 'Client not found'
                   },
                   (500): {
                       'model': ListClients500Response,
                       'description': 'Internal Server Error'
                   }
               },
               tags=['Clients'],
               summary='Delete a client by ID',
               response_model_by_alias=True)
async def delete_client(clientId: str = Path(..., description=''),
                        token_admin_api_key: TokenModel = Security(
                            get_token_admin_api_key)) -> None:
    """Delete a client by ID. If the client does not exist, a 404 error is returned."""
    return await delete_client_impl(clientId=clientId,
                                    token_admin_api_key=token_admin_api_key)


@router.get('/clients/{clientId}',
            responses={
                (200): {
                    'model': ListClients200ResponseInner,
                    'description': 'A client object'
                },
                (404): {
                    'model': ListClients500Response,
                    'description': 'Client Not Found'
                },
                (500): {
                    'model': ListClients500Response,
                    'description': 'Internal Server Error'
                }
            },
            tags=['Clients'],
            summary='Get a client by ID',
            response_model_by_alias=True)
async def get_client(
        clientId: str = Path(..., description=''),
        token_admin_api_key: TokenModel = Security(get_token_admin_api_key)
) -> ListClients200ResponseInner:
    """Get a client by ID. If the client does not exist, a 404 error is returned."""
    return await get_client_impl(clientId=clientId,
                                 token_admin_api_key=token_admin_api_key)


@router.get('/clients',
            responses={
                (200): {
                    'model': List[ListClients200ResponseInner],
                    'description': 'A list of clients'
                },
                (500): {
                    'model': ListClients500Response,
                    'description': 'Internal Server Error'
                }
            },
            tags=['Clients'],
            summary='List all clients',
            response_model_by_alias=True)
async def list_clients(token_admin_api_key: TokenModel = Security(
        get_token_admin_api_key)) -> List[ListClients200ResponseInner]:
    """List all clients. The clients are returned in a list."""
    return await list_clients_impl(token_admin_api_key=token_admin_api_key)


@router.put('/clients/{clientId}',
            responses={
                (200): {
                    'model': ListClients200ResponseInner,
                    'description': 'Successfully updated the client'
                },
                (400): {
                    'description': 'Invalid input provided'
                },
                (404): {
                    'model': ListClients500Response,
                    'description': 'Client Not Found'
                },
                (500): {
                    'model': ListClients500Response,
                    'description': 'Internal Server Error'
                }
            },
            tags=['Clients'],
            summary='Update a client by ID',
            response_model_by_alias=True)
async def update_client(
        clientId: str = Path(..., description=''),
        list_clients200_response_inner: ListClients200ResponseInner = Body(
            None, description=''),
        token_admin_api_key: TokenModel = Security(get_token_admin_api_key)
) -> ListClients200ResponseInner:
    """Update a client by ID. If the client does not exist, a 404 error is returned."""
    return await update_client_impl(
        clientId=clientId,
        list_clients200_response_inner=list_clients200_response_inner,
        token_admin_api_key=token_admin_api_key)
