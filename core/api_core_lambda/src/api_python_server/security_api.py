from api_python_server.implementation import get_token_admin_api_key as get_token_admin_api_key_impl
from api_python_server.implementation import get_token_client_api_key as get_token_client_api_key_impl
from typing import List
from fastapi import Depends, Security
from fastapi.openapi.models import OAuthFlowImplicit, OAuthFlows
from fastapi.security import HTTPAuthorizationCredentials, HTTPBasic, HTTPBasicCredentials, HTTPBearer, OAuth2, OAuth2AuthorizationCodeBearer, OAuth2PasswordBearer, SecurityScopes
from fastapi.security.api_key import APIKeyCookie, APIKeyHeader, APIKeyQuery
from api_python_server.models.extra_models import TokenModel


def get_token_admin_api_key(token_api_key_header: str = Security(
        APIKeyHeader(name='x-admin-api-key', auto_error=False))) -> TokenModel:
    """
    Check and retrieve authentication information from api_key.

    :param token_api_key_header API key provided by Authorization[x-admin-api-key] header
    
    
    :type token_api_key_header: str
    :return: Information attached to provided api_key or None if api_key is invalid or does not allow access to called API
    :rtype: TokenModel | None
    """
    return get_token_admin_api_key_impl(
        token_api_key_header=token_api_key_header)


def get_token_client_api_key(token_api_key_header: str = Security(
        APIKeyHeader(name='x-client-api-key',
                     auto_error=False))) -> TokenModel:
    """
    Check and retrieve authentication information from api_key.

    :param token_api_key_header API key provided by Authorization[x-client-api-key] header
    
    
    :type token_api_key_header: str
    :return: Information attached to provided api_key or None if api_key is invalid or does not allow access to called API
    :rtype: TokenModel | None
    """
    return get_token_client_api_key_impl(
        token_api_key_header=token_api_key_header)
