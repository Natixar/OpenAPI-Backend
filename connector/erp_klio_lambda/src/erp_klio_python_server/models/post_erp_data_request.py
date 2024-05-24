# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class PostErpDataRequest(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    PostErpDataRequest - a model defined in OpenAPI

        id: The id of this PostErpDataRequest.
        date_bl: The date_bl of this PostErpDataRequest.
        date_creation: The date_creation of this PostErpDataRequest.
        num_livraison: The num_livraison of this PostErpDataRequest.
        num_ligne_bon_livraison: The num_ligne_bon_livraison of this PostErpDataRequest.
        code_article: The code_article of this PostErpDataRequest.
        des1: The des1 of this PostErpDataRequest.
        des2: The des2 of this PostErpDataRequest.
        quantite: The quantite of this PostErpDataRequest.
        unite: The unite of this PostErpDataRequest.
        lot: The lot of this PostErpDataRequest.
        fournisseur_cde: The fournisseur_cde of this PostErpDataRequest.
        adresse_cde: The adresse_cde of this PostErpDataRequest.
        pays_cde: The pays_cde of this PostErpDataRequest.
        cp_cde: The cp_cde of this PostErpDataRequest.
        ville_cde: The ville_cde of this PostErpDataRequest.
    """

    id: int = Field(alias="id")
    date_bl: str = Field(alias="date_bl")
    date_creation: str = Field(alias="date_creation")
    num_livraison: int = Field(alias="num_livraison")
    num_ligne_bon_livraison: int = Field(alias="num_ligne_bon_livraison")
    code_article: str = Field(alias="code_article")
    des1: str = Field(alias="des1")
    des2: str = Field(alias="des2")
    quantite: float = Field(alias="quantite")
    unite: str = Field(alias="unite")
    lot: str = Field(alias="lot")
    fournisseur_cde: str = Field(alias="fournisseur_cde")
    adresse_cde: str = Field(alias="adresse_cde")
    pays_cde: str = Field(alias="pays_cde")
    cp_cde: str = Field(alias="cp_cde")
    ville_cde: str = Field(alias="ville_cde")

PostErpDataRequest.update_forward_refs()
