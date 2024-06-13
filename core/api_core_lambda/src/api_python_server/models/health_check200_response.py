# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class HealthCheck200Response(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    HealthCheck200Response - a model defined in OpenAPI

        status: The status of this HealthCheck200Response [Optional].
    """

    status: Optional[str] = Field(alias="status", default=None)

HealthCheck200Response.update_forward_refs()
