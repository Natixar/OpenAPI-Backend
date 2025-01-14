# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class GetScenarioRanges300ResponseInner(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    GetScenarioRanges300ResponseInner - a model defined in OpenAPI

        name: The name of this GetScenarioRanges300ResponseInner [Optional].
        href: The href of this GetScenarioRanges300ResponseInner [Optional].
        content_type: The content_type of this GetScenarioRanges300ResponseInner [Optional].
        q: The q of this GetScenarioRanges300ResponseInner [Optional].
    """

    name: Optional[str] = Field(alias="name", default=None)
    href: Optional[AnyUrl] = Field(alias="href", default=None)
    content_type: Optional[str] = Field(alias="Content-Type", default=None)
    q: Optional[float] = Field(alias="q", default=None)

GetScenarioRanges300ResponseInner.update_forward_refs()
