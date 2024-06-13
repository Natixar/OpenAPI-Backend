""" Module client 

    

    Created on 13/06/2024
    By Jean-Marc Le Peuvédic
    © CalCool Studios SAS 2021-2024
"""

# Import system libraries

# Import public libraries
from fastapi import HTTPException, status

# Import application modules
from api_python_server.models.list_clients200_response_inner import ListClients200ResponseInner
from api_python_server.models.extra_models import TokenModel


# -----------------------------------------------------
# Client management API
# Services
async def create_client(
    list_clients200_response_inner: ListClients200ResponseInner,
    token_admin_api_key: TokenModel
) -> ListClients200ResponseInner:
    """Create a new client with the provided name and description"""
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED)


async def delete_client(clientId: str, token_admin_api_key: TokenModel) -> None:
    """ Delete a client """
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED)


async def get_client(clientId: str, token_admin_api_key: TokenModel) -> ListClients200ResponseInner:
    """ Get a client """
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED)


async def list_clients(token_admin_api_key: TokenModel) -> list[ListClients200ResponseInner]:
    """ List all clients """
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED)


async def update_client(
    clientId: str,
    list_clients200_response_inner:
    ListClients200ResponseInner,
    token_admin_api_key: TokenModel
) -> ListClients200ResponseInner:
    """ Update a client """
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED)
