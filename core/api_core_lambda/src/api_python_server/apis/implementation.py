""" Module implementation 

    MANUALLY WRITTEN IMPLEMENTATION FILE: DO NOT ERASE !
    Unlike most of the files in the folder api_lambda/src, this file is not automatically generated.
    It implements the API.

    Created on 07/06/2024
    By Jean-Marc Le Peuvédic
    © CalCool Studios SAS 2021-2024
"""

# TODO List

# Import system libraries
from typing import List

# Import public libraries
from fastapi import HTTPException, status

from api_python_server.models.create_scenario_request import CreateScenarioRequest
# Import application modules
from api_python_server.models.list_clients200_response_inner import ListClients200ResponseInner
from api_python_server.models.get_scenario_ranges200_response_inner import GetScenarioRanges200ResponseInner
from api_python_server.models.list_scenarios200_response_inner import ListScenarios200ResponseInner


# -----------------------------------------------------
# Client management API

async def create_client(list_clients200_response_inner: ListClients200ResponseInner) -> ListClients200ResponseInner:
    """ Create a new client """
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED)

async def delete_client(clientId: str) -> None:
    """ Delete a client """
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED)

async def get_client(clientId: str) -> ListClients200ResponseInner:
    """ Get a client """
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED)

async def list_clients() -> List[ListClients200ResponseInner]:
    """ List all clients """
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED)

async def update_client(clientId: str, list_clients200_response_inner: ListClients200ResponseInner) -> ListClients200ResponseInner:
    """ Update a client """
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED)

# -----------------------------------------------------
# Scenario management API

async def create_scenario(create_scenario_request: CreateScenarioRequest) -> ListScenarios200ResponseInner:
    """ Create a new scenario """
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED)

async def delete_scenario(scenarioId: str) -> None:
    """ Delete a scenario """
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED)

async def get_scenario(scenarioId: str) -> ListScenarios200ResponseInner:
    """ Get a scenario """
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED)

async def get_scenario_ranges(scenarioId: str, range: str, accept: str,
                              time_ranges: str, scale: str, protocol: str) -> List[GetScenarioRanges200ResponseInner]:
    """ Get the ranges of a scenario """
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED)

async def list_scenarios() -> List[ListScenarios200ResponseInner]:
    """ List all scenarios """
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED)

# async def get_scenario_status(scenarioId: str) -> dict:
#     """ Get the status of a scenario """
#     raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED)

# -----------------------------------------------------
# Old Scenario data API

async def get_data(time_ranges: str, scale: str, protocol: str) -> List[GetScenarioRanges200ResponseInner]:
    """ Get the data of a scenario """
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED)