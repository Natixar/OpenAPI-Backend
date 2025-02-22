# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class CreateScenarioRequest(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    CreateScenarioRequest - a model defined in OpenAPI

        title: The title of this CreateScenarioRequest.
        description: The description of this CreateScenarioRequest [Optional].
        uuid: The uuid of this CreateScenarioRequest [Optional].
        parent_scenario_id: The parent_scenario_id of this CreateScenarioRequest [Optional].
    """

    title: str = Field(alias="title")
    description: Optional[str] = Field(alias="description", default=None)
    uuid: Optional[str] = Field(alias="uuid", default=None)
    parent_scenario_id: Optional[str] = Field(alias="parentScenarioId", default=None)

CreateScenarioRequest.update_forward_refs()
