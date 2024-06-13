""" Module security.py 

    

    Created on 13/06/2024
    By Jean-Marc Le Peuvédic
    © CalCool Studios SAS 2021-2024
"""
# Import system libraries
import json
import hashlib
import base64
import os
from sys import version_info
from datetime import datetime

# Import public libraries
from fastapi import HTTPException, status, Security
from fastapi.security.api_key import APIKeyHeader

# Import application modules
import api_python_server
from api_python_server.models.extra_models import TokenModel
from api_python_server.models.health_get200_response import HealthGet200Response


# Security

# There is an administrative API key used for back-office operations like creating clients,
# and one client API key per client. Some endpoints like GET /scenarios limit the scope to
# one client when a client API key is used, rather than an administrative API key.

# The database of recently used salts should be complete enough to cover all the still valid API keys.
# It is stored in the package folder.
python_version = f"{version_info.major}.{version_info.minor}"
package_directories = [
    f"/venv/lib/python{python_version}/site-packages/api_python_server",
    f"api_python_server",
    f"../../core-implementation/api_python_server"
]

for directory in package_directories:
    if os.path.exists(os.path.join(directory, "salts.ndjson")):
        package_directory = directory
        break
    else:
        print(f"CWD = {os.path.abspath(os.curdir)}")
else:
    raise FileNotFoundError("Salt database not found in any of the expected locations.")

SALT_DB = [line.strip() for line in open(os.path.join(package_directory, "salts.ndjson"), 'r')]

if not SALT_DB:
    raise ValueError("Salt database is empty. No client can connect!")


def base64_decode(b64encoded_string: str) -> str:
    """ Decode a base64 string to a string """
    # The input is a str, not bytes, so must be first converted to bytes.
    # We decode assuming the original text was utf-8, since it's JSON (or hex digest = ASCII)
    return base64.urlsafe_b64decode((b64encoded_string + '==').encode()).decode('utf-8')


def validate_token(token_api_key_header: str) -> TokenModel:
    """ Check and retrieve authentication information from api_key
    :param token_api_key_header: taken from the x-client-api_key or x-admin-api-key headers.
    :return: a string formatted [tool_name]:[user id] if the token is valid.
    :raises: HTTPException(status_code=status.HTTP_401_UNAUTHORIZED) if the token is invalid.
    """
    if not token_api_key_header:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Missing API Key header in request")
    try:
        # Split payload and signature.
        token_parts = token_api_key_header.split(".")
        if len(token_parts) != 2:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token format")
        client = base64_decode(token_parts[0])
        signature = base64_decode(token_parts[1])
        
        current_timestamp = int(datetime.now().timestamp())
        
        # Check all the active salts
        for salt in SALT_DB:
            # Skip expired salts (we only purge expired salts when we rebuild the server containers)
            if json.loads(salt)['exp'] <= current_timestamp:
                continue
            
            # Compute signed_data in NDJSON format
            signed_data = f"{client}\n{salt.strip()}"
            # Compute signature with this salt
            signature_check = hashlib.sha256(signed_data.encode()).hexdigest()
            
            if signature_check == signature:
                # Convert client data to a dict
                client_dict = json.loads(client)
                # Check if the client API key is not expired
                if client_dict['exp'] > int(datetime.now().timestamp()):
                    # Valid API key
                    tool = json.loads(salt.strip())['tool']
                    return TokenModel(sub=f"{tool}:{client_dict['id']}")
                # We found the matching salt, but the API key is expired. No need to test more salts.
                detail = "Expired API Key"
                break
        else:
            # The key could be long expired and we would have purged the SALT_DB from the matching salt...
            detail = "Invalid or long expired API Key"
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=detail)
    
    except Exception as e:
        # Raise a generic "Unauthorized" error.
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized") from e

def get_token_admin_api_key(token_api_key_header: str) -> TokenModel:
    """ Check and retrieve authentication information from api_key """
    return validate_token(token_api_key_header)


def get_token_client_api_key(token_api_key_header: str) -> TokenModel:
    """ Check and retrieve authentication information from api_key """
    return validate_token(token_api_key_header)


async def health_check(
) -> HealthGet200Response:
    """ Check API health """
    return HealthGet200Response(status="ok")
