# coding: utf-8

"""
    API B2B ADICT V2

    Cette API vous permet de gérer vos droits d'accès aux données des PCE et de consulter leurs données contractuelles, techniques, de consommation publiées / informatives et d'injections publiées.  # noqa: E501

    The version of the OpenAPI document: v2
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from grdf_client import schemas  # noqa: F401


class PceKo(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "id_pce",
        }
        
        class properties:
            id_pce = schemas.StrSchema
            __annotations__ = {
                "id_pce": id_pce,
            }
    
    id_pce: MetaOapg.properties.id_pce
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id_pce"]) -> MetaOapg.properties.id_pce: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id_pce", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id_pce"]) -> MetaOapg.properties.id_pce: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id_pce", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        id_pce: typing.Union[MetaOapg.properties.id_pce, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PceKo':
        return super().__new__(
            cls,
            *args,
            id_pce=id_pce,
            _configuration=_configuration,
            **kwargs,
        )