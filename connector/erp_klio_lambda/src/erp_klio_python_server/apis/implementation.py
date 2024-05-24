""" Module implementation 

    MANUALLY WRITTEN IMPLEMENTATION FILE: DO NOT ERASE !
    Unlike most of the files in the folder erp_klio_lambda/src, this file is not automatically generated.
    It implements the API.

    Created on 23/05/2024
    By Jean-Marc Le Peuvédic
    © CalCool Studios SAS 2021-2024
"""
# Import system libraries

# Import public libraries

# Import application modules
from fastapi import HTTPException, status
from erp_klio_python_server.models.post_erp_data_request import PostErpDataRequest


async def get_last_id(scenarioId: str) -> int:
    # Example implementation
    return 1


async def post_erp_data(scenarioId: str, post_erp_data_request: PostErpDataRequest) -> str:
    # Example implementation
    return "Data successfully posted"
