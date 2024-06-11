# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class ListClients500Response(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    ListClients500Response - a model defined in OpenAPI

        code: The code of this ListClients500Response.
        message: The message of this ListClients500Response.
    """

    code: str = Field(alias="code")
    message: str = Field(alias="message")

ListClients500Response.update_forward_refs()
