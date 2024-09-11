""" Module implementation 

    MANUALLY WRITTEN IMPLEMENTATION FILE: DO NOT ERASE !
    Unlike most of the files in the folder api_lambda/src, this file is not automatically generated.
    It implements the API.

    Created on 07/06/2024
    By Jean-Marc Le Peuvédic
    © CalCool Studios SAS 2021-2024
"""

# Import implementation functions: gather them all in this implementation namespace.
from api_python_server.clients import create_client, delete_client, get_client, list_clients, update_client # noqa: F401
from api_python_server.scenarios import create_scenario, delete_scenario, get_scenario, get_scenario_ranges, list_scenarios, get_data  # noqa: F401
from api_python_server.security import get_token_admin_api_key, get_token_client_api_key, health_check   # noqa: F401
from api_python_server.db_conn import get_db  # noqa: F401