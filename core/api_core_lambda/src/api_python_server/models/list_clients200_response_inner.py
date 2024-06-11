# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class ListClients200ResponseInner(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    ListClients200ResponseInner - a model defined in OpenAPI

        id: The id of this ListClients200ResponseInner.
        name: The name of this ListClients200ResponseInner.
        email: The email of this ListClients200ResponseInner [Optional].
        phone: The phone of this ListClients200ResponseInner [Optional].
        default_scenario: The default_scenario of this ListClients200ResponseInner [Optional].
    """

    id: str = Field(alias="id")
    name: str = Field(alias="name")
    email: Optional[EmailStr] = Field(alias="email", default=None)
    phone: Optional[str] = Field(alias="phone", default=None)
    default_scenario: Optional[str] = Field(alias="defaultScenario", default=None)

ListClients200ResponseInner.update_forward_refs()
