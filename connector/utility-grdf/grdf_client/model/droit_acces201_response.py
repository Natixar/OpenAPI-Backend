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


class DroitAcces201Response(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def demander_acces_out() -> typing.Type['DemanderAccesOut']:
                return DemanderAccesOut
        
            @staticmethod
            def retour_201_demander_acces() -> typing.Type['Retour201DemanderAcces']:
                return Retour201DemanderAcces
            __annotations__ = {
                "demander_acces_out": demander_acces_out,
                "retour_201_demander_acces": retour_201_demander_acces,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["demander_acces_out"]) -> 'DemanderAccesOut': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["retour_201_demander_acces"]) -> 'Retour201DemanderAcces': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["demander_acces_out", "retour_201_demander_acces", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["demander_acces_out"]) -> typing.Union['DemanderAccesOut', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["retour_201_demander_acces"]) -> typing.Union['Retour201DemanderAcces', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["demander_acces_out", "retour_201_demander_acces", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        demander_acces_out: typing.Union['DemanderAccesOut', schemas.Unset] = schemas.unset,
        retour_201_demander_acces: typing.Union['Retour201DemanderAcces', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'DroitAcces201Response':
        return super().__new__(
            cls,
            *args,
            demander_acces_out=demander_acces_out,
            retour_201_demander_acces=retour_201_demander_acces,
            _configuration=_configuration,
            **kwargs,
        )

from grdf_client.model.demander_acces_out import DemanderAccesOut
from grdf_client.model.retour201_demander_acces import Retour201DemanderAcces
