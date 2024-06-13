from api_python_server.implementation import health_check as health_check_impl
from typing import Dict, List
from fastapi import APIRouter, Body, Cookie, Depends, Form, Header, Path, Query, Response, Security, status
from api_python_server.models.extra_models import TokenModel
from api_python_server.models.health_check200_response import HealthCheck200Response
router = APIRouter()


@router.get('/health',
            responses={
                (200): {
                    'model': HealthCheck200Response,
                    'description': 'Server is healthy'
                }
            },
            tags=['Health'],
            summary='Health check',
            response_model_by_alias=True)
async def health_check() -> HealthCheck200Response:
    """Return server health information"""
    return await health_check_impl()
