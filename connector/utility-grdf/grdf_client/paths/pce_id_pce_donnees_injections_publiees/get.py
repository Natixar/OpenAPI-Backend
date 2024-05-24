# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from urllib3._collections import HTTPHeaderDict

from grdf_client import api_client, exceptions
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

from grdf_client.model.model5 import Model5
from grdf_client.model.injection_restit500 import InjectionRestit500
from grdf_client.model.injection_restit400 import InjectionRestit400

from . import path

# query params


class PeriodeSchema(
    schemas.StrSchema
):


    class MetaOapg:
        regex=[{
            'pattern': r'(^\d{4}$)|(^PN-\d{4}$)|(^\d{4}-\d{2}$)|(^PN-\d{4}-\d{2}$)|(^\d{4}-W\d{2}$)|(^PN-\d{4}-W\d{2}$)|(^PN-\d{4}-W\d{2}-\d{1}$)|(^\d{4}-\d{3})$',  # noqa: E501
        }]


class DateDebutSchema(
    schemas.DateSchema
):


    class MetaOapg:
        format = 'date'
        regex=[{
            'pattern': r'YYYY-MM-DD',  # noqa: E501
        }]


class DateFinSchema(
    schemas.DateSchema
):


    class MetaOapg:
        format = 'date'
        regex=[{
            'pattern': r'YYYY-MM-DD',  # noqa: E501
        }]
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'periode': typing.Union[PeriodeSchema, str, ],
        'date_debut': typing.Union[DateDebutSchema, str, date, ],
        'date_fin': typing.Union[DateFinSchema, str, date, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_periode = api_client.QueryParameter(
    name="periode",
    schema=PeriodeSchema,
)
request_query_date_debut = api_client.QueryParameter(
    name="date_debut",
    schema=DateDebutSchema,
)
request_query_date_fin = api_client.QueryParameter(
    name="date_fin",
    schema=DateFinSchema,
)
# path params


class IdPceSchema(
    schemas.StrSchema
):


    class MetaOapg:
        regex=[{
            'pattern': r'(^GI\d{6}$|^\d{14}$)',  # noqa: E501
        }]
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'id_pce': typing.Union[IdPceSchema, str, ],
    }
)
RequestOptionalPathParams = typing_extensions.TypedDict(
    'RequestOptionalPathParams',
    {
    },
    total=False
)


class RequestPathParams(RequestRequiredPathParams, RequestOptionalPathParams):
    pass


request_path_id_pce = api_client.PathParameter(
    name="id_pce",
    schema=IdPceSchema,
    required=True,
)
_auth = [
    'OAuth (External)AccessCode',
    'OAuth (External)Implicit',
]
SchemaFor200ResponseBodyApplicationXNdjson = Model5


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
        SchemaFor200ResponseBodyApplicationXNdjson,
    ]
    headers: schemas.Unset = schemas.unset


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    content={
        'application/x-ndjson': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationXNdjson),
    },
)
SchemaFor400ResponseBodyApplicationXNdjson = InjectionRestit400


@dataclass
class ApiResponseFor400(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
        SchemaFor400ResponseBodyApplicationXNdjson,
    ]
    headers: schemas.Unset = schemas.unset


_response_for_400 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor400,
    content={
        'application/x-ndjson': api_client.MediaType(
            schema=SchemaFor400ResponseBodyApplicationXNdjson),
    },
)
SchemaFor500ResponseBodyApplicationXNdjson = InjectionRestit500


@dataclass
class ApiResponseFor500(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
        SchemaFor500ResponseBodyApplicationXNdjson,
    ]
    headers: schemas.Unset = schemas.unset


_response_for_500 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor500,
    content={
        'application/x-ndjson': api_client.MediaType(
            schema=SchemaFor500ResponseBodyApplicationXNdjson),
    },
)
_status_code_to_response = {
    '200': _response_for_200,
    '400': _response_for_400,
    '500': _response_for_500,
}
_all_accept_content_types = (
    'application/x-ndjson',
)


class BaseApi(api_client.Api):

    def _get_pce_id_pce_donnees_injections_publiees_oapg(
        self: api_client.Api,
        query_params: RequestQueryParams = frozendict.frozendict(),
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization
    ]:
        """
        Consulter les injections publiées du PCE demandé
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value

        _path_params = {}
        for parameter in (
            request_path_id_pce,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)

        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)

        prefix_separator_iterator = None
        for parameter in (
            request_query_periode,
            request_query_date_debut,
            request_query_date_fin,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value

        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)

        response = self.api_client.call_api(
            resource_path=used_path,
            method='get'.upper(),
            headers=_headers,
            auth_settings=_auth,
            stream=stream,
            timeout=timeout,
        )

        if skip_deserialization:
            api_response = api_client.ApiResponseWithoutDeserialization(response=response)
        else:
            response_for_status = _status_code_to_response.get(str(response.status))
            if response_for_status:
                api_response = response_for_status.deserialize(response, self.api_client.configuration)
            else:
                api_response = api_client.ApiResponseWithoutDeserialization(response=response)

        if not 200 <= response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)

        return api_response


class GetPceIdPceDonneesInjectionsPubliees(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    def get_pce_id_pce_donnees_injections_publiees(
        self: BaseApi,
        query_params: RequestQueryParams = frozendict.frozendict(),
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization
    ]:
        return self._get_pce_id_pce_donnees_injections_publiees_oapg(
            query_params=query_params,
            path_params=path_params,
            accept_content_types=accept_content_types,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    def get(
        self: BaseApi,
        query_params: RequestQueryParams = frozendict.frozendict(),
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization
    ]:
        return self._get_pce_id_pce_donnees_injections_publiees_oapg(
            query_params=query_params,
            path_params=path_params,
            accept_content_types=accept_content_types,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )


