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


class Model1(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def pce() -> typing.Type['Pce']:
                return Pce
        
            @staticmethod
            def periode() -> typing.Type['Periode']:
                return Periode
        
            @staticmethod
            def releve_debut() -> typing.Type['ReleveDebut']:
                return ReleveDebut
        
            @staticmethod
            def releve_fin() -> typing.Type['ReleveFin']:
                return ReleveFin
        
            @staticmethod
            def consommation() -> typing.Type['Consommation']:
                return Consommation
        
            @staticmethod
            def bordereau_publication() -> typing.Type['BordereauPublication']:
                return BordereauPublication
            statut_restitution = schemas.DictSchema
            __annotations__ = {
                "pce": pce,
                "periode": periode,
                "releve_debut": releve_debut,
                "releve_fin": releve_fin,
                "consommation": consommation,
                "bordereau_publication": bordereau_publication,
                "statut_restitution": statut_restitution,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pce"]) -> 'Pce': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["periode"]) -> 'Periode': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["releve_debut"]) -> 'ReleveDebut': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["releve_fin"]) -> 'ReleveFin': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["consommation"]) -> 'Consommation': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["bordereau_publication"]) -> 'BordereauPublication': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["statut_restitution"]) -> MetaOapg.properties.statut_restitution: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["pce", "periode", "releve_debut", "releve_fin", "consommation", "bordereau_publication", "statut_restitution", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pce"]) -> typing.Union['Pce', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["periode"]) -> typing.Union['Periode', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["releve_debut"]) -> typing.Union['ReleveDebut', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["releve_fin"]) -> typing.Union['ReleveFin', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["consommation"]) -> typing.Union['Consommation', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["bordereau_publication"]) -> typing.Union['BordereauPublication', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["statut_restitution"]) -> typing.Union[MetaOapg.properties.statut_restitution, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["pce", "periode", "releve_debut", "releve_fin", "consommation", "bordereau_publication", "statut_restitution", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        pce: typing.Union['Pce', schemas.Unset] = schemas.unset,
        periode: typing.Union['Periode', schemas.Unset] = schemas.unset,
        releve_debut: typing.Union['ReleveDebut', schemas.Unset] = schemas.unset,
        releve_fin: typing.Union['ReleveFin', schemas.Unset] = schemas.unset,
        consommation: typing.Union['Consommation', schemas.Unset] = schemas.unset,
        bordereau_publication: typing.Union['BordereauPublication', schemas.Unset] = schemas.unset,
        statut_restitution: typing.Union[MetaOapg.properties.statut_restitution, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Model1':
        return super().__new__(
            cls,
            *args,
            pce=pce,
            periode=periode,
            releve_debut=releve_debut,
            releve_fin=releve_fin,
            consommation=consommation,
            bordereau_publication=bordereau_publication,
            statut_restitution=statut_restitution,
            _configuration=_configuration,
            **kwargs,
        )

from grdf_client.model.bordereau_publication import BordereauPublication
from grdf_client.model.consommation import Consommation
from grdf_client.model.pce import Pce
from grdf_client.model.periode import Periode
from grdf_client.model.releve_debut import ReleveDebut
from grdf_client.model.releve_fin import ReleveFin
