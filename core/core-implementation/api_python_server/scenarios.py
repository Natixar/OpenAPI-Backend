""" Module scenario 

    

    Created on 13/06/2024
    By Jean-Marc Le Peuvédic
    © CalCool Studios SAS 2021-2024
"""
# Import system libraries

# Import public libraries
from fastapi import HTTPException, status

# Import application modules
from api_python_server.models.get_scenario_ranges200_response_inner import GetScenarioRanges200ResponseInner
from api_python_server.models.list_scenarios200_response_inner import ListScenarios200ResponseInner
from api_python_server.models.extra_models import TokenModel
from api_python_server.models.create_scenario_request import CreateScenarioRequest


# -----------------------------------------------------
# Scenario management API

async def create_scenario(
    create_scenario_request: CreateScenarioRequest,
    token_admin_api_key: TokenModel, token_client_api_key: TokenModel
) -> ListScenarios200ResponseInner:
    """ Create a new scenario """
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED)


async def delete_scenario(
    scenarioId: str, token_admin_api_key: TokenModel, token_client_api_key: TokenModel
) -> None:
    """ Delete a scenario """
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED)


async def get_scenario(
    scenarioId: str, token_admin_api_key: TokenModel, token_client_api_key: TokenModel
) -> ListScenarios200ResponseInner:
    """ Get a scenario """
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED)


async def get_scenario_ranges(
    scenarioId: str, range: str, accept: str, time_ranges: str, scale: str, protocol: str,
    token_client_api_key: TokenModel
) -> list[GetScenarioRanges200ResponseInner]:
    """ Get the ranges of a scenario """
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED)


async def list_scenarios(
    token_admin_api_key: TokenModel, token_client_api_key: TokenModel
) -> list[ListScenarios200ResponseInner]:
    """ List all scenarios """
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED)


# async def get_scenario_status(scenarioId: str) -> dict:
#     """ Get the status of a scenario """
#     raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED)

# -----------------------------------------------------
# Old Scenario data API

async def get_data(
    time_ranges: str, scale: str, protocol: str, token_client_api_key: TokenModel
) -> list[GetScenarioRanges200ResponseInner]:
    """ Get the data of a scenario """
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED)
