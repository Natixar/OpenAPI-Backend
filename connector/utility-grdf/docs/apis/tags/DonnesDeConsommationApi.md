<a name="__pageTop"></a>
# grdf_client.apis.tags.donnes_de_consommation_api.DonnesDeConsommationApi

All URIs are relative to *http://api.grdf.fr/adict/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_pce_id_pce_donnees_consos_informatives**](#get_pce_id_pce_donnees_consos_informatives) | **get** /pce/{id_pce}/donnees_consos_informatives | Consulter les consommations informatives du PCE demandé
[**get_pce_id_pce_donnees_consos_publiees**](#get_pce_id_pce_donnees_consos_publiees) | **get** /pce/{id_pce}/donnees_consos_publiees | Consulter les consommations publiées du PCE demandé

# **get_pce_id_pce_donnees_consos_informatives**
<a name="get_pce_id_pce_donnees_consos_informatives"></a>
> ConsoRestit get_pce_id_pce_donnees_consos_informatives(id_pce)

Consulter les consommations informatives du PCE demandé

Ce service vous permet de consulter les données de consommation informatives d’un  PCE pour une période de restitution demandée.

### Example

* OAuth Authentication (OAuth (External)AccessCode):
* OAuth Authentication (OAuth (External)Implicit):
```python
import grdf_client
from grdf_client.apis.tags import donnes_de_consommation_api
from grdf_client.model.conso_restit400 import ConsoRestit400
from grdf_client.model.conso_restit import ConsoRestit
from grdf_client.model.conso_restit500 import ConsoRestit500
from pprint import pprint
# Defining the host is optional and defaults to http://api.grdf.fr/adict/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = grdf_client.Configuration(
    host = "http://api.grdf.fr/adict/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: OAuth (External)AccessCode
configuration = grdf_client.Configuration(
    host = "http://api.grdf.fr/adict/v2"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: OAuth (External)Implicit
configuration = grdf_client.Configuration(
    host = "http://api.grdf.fr/adict/v2"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Enter a context with an instance of the API client
with grdf_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = donnes_de_consommation_api.DonnesDeConsommationApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id_pce': "48072888001528",
    }
    query_params = {
    }
    try:
        # Consulter les consommations informatives du PCE demandé
        api_response = api_instance.get_pce_id_pce_donnees_consos_informatives(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except grdf_client.ApiException as e:
        print("Exception when calling DonnesDeConsommationApi->get_pce_id_pce_donnees_consos_informatives: %s\n" % e)

    # example passing only optional values
    path_params = {
        'id_pce': "48072888001528",
    }
    query_params = {
        'periode': "PN-4807-W28",
        'date_debut': "1970-01-01",
        'date_fin': "1970-01-01",
    }
    try:
        # Consulter les consommations informatives du PCE demandé
        api_response = api_instance.get_pce_id_pce_donnees_consos_informatives(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except grdf_client.ApiException as e:
        print("Exception when calling DonnesDeConsommationApi->get_pce_id_pce_donnees_consos_informatives: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/x-ndjson', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
periode | PeriodeSchema | | optional
date_debut | DateDebutSchema | | optional
date_fin | DateFinSchema | | optional


# PeriodeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# DateDebutSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, date,  | str,  |  | value must conform to RFC-3339 full-date YYYY-MM-DD

# DateFinSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, date,  | str,  |  | value must conform to RFC-3339 full-date YYYY-MM-DD

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
id_pce | IdPceSchema | | 

# IdPceSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_pce_id_pce_donnees_consos_informatives.ApiResponseFor200) | SUCCESS : Aucun droit d&#x27;accès pour tous les PCE en entrée. / Le client semble avoir déménagé et n&#x27;est plus titulaire de ce PCE, vous ne pouvez donc plus accéder à ses données. / Votre droit d’accès sur ce PCE a expiré. Pour continuer à accéder aux données, vous devez faire une nouvelle demande d&#x27;accès et, le cas échéant, renouveler le consentement du titulaire. / La preuve de consentement fournie lors du contrôle opéré par GRDF n’est pas valide. / GRDF a passé le droit d&#x27;accès à l&#x27;état obsolète. / Votre contrat GRDF ADICT est expiré. Veuillez prendre contact avec GRDF pour le renouveler. / Vos droits d’accès aux données des PCE ont été suspendus en raison d’une mauvaise utilisation de la plateforme. Veuillez prendre contact avec GRDF. / Le client titulaire a révoqué son consentement, vous ne pouvez plus accéder aux données de ce PCE. / GRDF a révoqué votre droit d’accès aux données de ce PCE à la demande du client titulaire. / Vous avez révoqué votre droit d’accès aux données de ce PCE. / Vous n&#x27;êtes pas autorisé à consulter les données de ce PCE. / Vous n&#x27;êtes pas ou plus autorisé à consulter les données de ce PCE. / Il n&#x27;y a pas de données correspondant à ce PCE sur la période demandée. / Le périmètre des données auxquelles vous avez accès pour ce PCE ne couvre pas les données de consommations informatives. / Le serveur a rencontré une erreur lors de l&#x27;exécution de la requête. Veuillez retenter votre appel sur la période mentionnée ci-dessus.
400 | [ApiResponseFor400](#get_pce_id_pce_donnees_consos_informatives.ApiResponseFor400) | BAD REQUEST : L&#x27;identifiant du PCE n&#x27;est pas correctement formaté (GI+6 chiffres ou 14 chiffres). / Le serveur a rencontré une erreur lors de l’exécution de la requête, veuillez réessayer ultérieurement. / Le format du paramètre &#x27;date_debut&#x27; et / ou &#x27;date_fin&#x27; n’est pas au format YYYY-MM-DD. / Le format du paramètre &#x27;periode&#x27; n’est pas à un format attendu valide (YYYY, YYYY-NN, YYYY-WNN, YYYY-NNN, PN-YYYY, PN-YYYY-NN, PN-YYYY-WNN, PN-YYYY-WMM-N). / Le paramètre &#x27;date_fin&#x27; est obligatoire et doit être renseigné au format YYYY-MM-DD. / Le paramètre &#x27;date_debut&#x27; est obligatoire et doit être renseigné au format YYYY-MM-DD. / Le paramètre &#x27;date_debut&#x27; ne doit pas être antérieur à la date du jour - 3 ans. / Seul le paramètre &#x27;periode&#x27; ou les paramètres &#x27;date_debut&#x27; / &#x27;date_fin&#x27; doivent être renseignés. / Le paramètre &#x27;periode&#x27; ou les paramètres &#x27;date_debut&#x27; / &#x27;date_fin&#x27; doivent être renseignés. / La date de début renseignée doit être antérieure à la date de fin. / Le paramètre &#x27;date_fin&#x27; doit être inférieur ou égal à la date du jour. / Donnée(s) obligatoire(s) manquante(s) / Format(s) de donnée(s) incorrect(s)
500 | [ApiResponseFor500](#get_pce_id_pce_donnees_consos_informatives.ApiResponseFor500) | INTERNAL SERVER ERROR : Le serveur a rencontré une erreur lors de l’exécution de la requête, veuillez réessayer ultérieurement.

#### get_pce_id_pce_donnees_consos_informatives.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationXNdjson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationXNdjson
Type | Description  | Notes
------------- | ------------- | -------------
[**ConsoRestit**](../../models/ConsoRestit.md) |  | 


#### get_pce_id_pce_donnees_consos_informatives.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationXNdjson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationXNdjson
Type | Description  | Notes
------------- | ------------- | -------------
[**ConsoRestit400**](../../models/ConsoRestit400.md) |  | 


#### get_pce_id_pce_donnees_consos_informatives.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationXNdjson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationXNdjson
Type | Description  | Notes
------------- | ------------- | -------------
[**ConsoRestit500**](../../models/ConsoRestit500.md) |  | 


### Authorization

[OAuth (External)AccessCode](../../../README.md#OAuth (External)AccessCode), [OAuth (External)Implicit](../../../README.md#OAuth (External)Implicit)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_pce_id_pce_donnees_consos_publiees**
<a name="get_pce_id_pce_donnees_consos_publiees"></a>
> Model1 get_pce_id_pce_donnees_consos_publiees(id_pce)

Consulter les consommations publiées du PCE demandé

Ce service vous permet de consulter les données de consommation publiées d’un PCE  pour une période de restitution demandée.

### Example

* OAuth Authentication (OAuth (External)AccessCode):
* OAuth Authentication (OAuth (External)Implicit):
```python
import grdf_client
from grdf_client.apis.tags import donnes_de_consommation_api
from grdf_client.model.conso_restit400 import ConsoRestit400
from grdf_client.model.conso_restit500 import ConsoRestit500
from grdf_client.model.model1 import Model1
from pprint import pprint
# Defining the host is optional and defaults to http://api.grdf.fr/adict/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = grdf_client.Configuration(
    host = "http://api.grdf.fr/adict/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: OAuth (External)AccessCode
configuration = grdf_client.Configuration(
    host = "http://api.grdf.fr/adict/v2"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: OAuth (External)Implicit
configuration = grdf_client.Configuration(
    host = "http://api.grdf.fr/adict/v2"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Enter a context with an instance of the API client
with grdf_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = donnes_de_consommation_api.DonnesDeConsommationApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id_pce': "48072888001528",
    }
    query_params = {
    }
    try:
        # Consulter les consommations publiées du PCE demandé
        api_response = api_instance.get_pce_id_pce_donnees_consos_publiees(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except grdf_client.ApiException as e:
        print("Exception when calling DonnesDeConsommationApi->get_pce_id_pce_donnees_consos_publiees: %s\n" % e)

    # example passing only optional values
    path_params = {
        'id_pce': "48072888001528",
    }
    query_params = {
        'periode': "PN-4807-W28",
        'date_debut': "1970-01-01",
        'date_fin': "1970-01-01",
    }
    try:
        # Consulter les consommations publiées du PCE demandé
        api_response = api_instance.get_pce_id_pce_donnees_consos_publiees(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except grdf_client.ApiException as e:
        print("Exception when calling DonnesDeConsommationApi->get_pce_id_pce_donnees_consos_publiees: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/x-ndjson', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
periode | PeriodeSchema | | optional
date_debut | DateDebutSchema | | optional
date_fin | DateFinSchema | | optional


# PeriodeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# DateDebutSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, date,  | str,  |  | value must conform to RFC-3339 full-date YYYY-MM-DD

# DateFinSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, date,  | str,  |  | value must conform to RFC-3339 full-date YYYY-MM-DD

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
id_pce | IdPceSchema | | 

# IdPceSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_pce_id_pce_donnees_consos_publiees.ApiResponseFor200) | SUCCESS : Aucun droit d&#x27;accès pour tous les PCE en entrée. / Le client semble avoir déménagé et n&#x27;est plus titulaire de ce PCE, vous ne pouvez donc plus accéder à ses données. / Votre droit d’accès sur ce PCE a expiré. Pour continuer à accéder aux données, vous devez faire une nouvelle demande d&#x27;accès et, le cas échéant, renouveler le consentement du titulaire. / La preuve de consentement fournie lors du contrôle opéré par GRDF n’est pas valide. / GRDF a passé le droit d&#x27;accès à l&#x27;état obsolète. / Votre contrat GRDF ADICT est expiré. Veuillez prendre contact avec GRDF pour le renouveler. / Vos droits d’accès aux données des PCE ont été suspendus en raison d’une mauvaise utilisation de la plateforme. Veuillez prendre contact avec GRDF. / Le client titulaire a révoqué son consentement, vous ne pouvez plus accéder aux données de ce PCE. / GRDF a révoqué votre droit d’accès aux données de ce PCE à la demande du client titulaire. / Vous avez révoqué votre droit d’accès aux données de ce PCE. / Vous n&#x27;êtes pas autorisé à consulter les données de ce PCE. / Vous n&#x27;êtes pas ou plus autorisé à consulter les données de ce PCE. / Il n&#x27;y a pas de données correspondant à ce PCE sur la période demandée. / Le périmètre des données auxquelles vous avez accès pour ce PCE ne couvre pas les données de consommations publiées. / Le serveur a rencontré une erreur lors de l&#x27;exécution de la requête. Veuillez retenter votre appel sur la période mentionnée ci-dessus.
400 | [ApiResponseFor400](#get_pce_id_pce_donnees_consos_publiees.ApiResponseFor400) | BAD REQUEST : L&#x27;identifiant du PCE n&#x27;est pas correctement formaté (GI+6 chiffres ou 14 chiffres). / Le serveur a rencontré une erreur lors de l’exécution de la requête, veuillez réessayer ultérieurement. / Le format du paramètre &#x27;date_debut&#x27; et / ou &#x27;date_fin&#x27; n’est pas au format YYYY-MM-DD. / Le format du paramètre &#x27;periode&#x27; n’est pas à un format attendu valide (YYYY, YYYY-NN, YYYY-WNN, YYYY-NNN, PN-YYYY, PN-YYYY-NN, PN-YYYY-WNN, PN-YYYY-WMM-N). / Le paramètre &#x27;date_fin&#x27; est obligatoire et doit être renseigné au format YYYY-MM-DD. / Le paramètre &#x27;date_debut&#x27; est obligatoire et doit être renseigné au format YYYY-MM-DD. / Le paramètre &#x27;date_debut&#x27; ne doit pas être antérieur à la date du jour - 5 ans. / Seul le paramètre &#x27;periode&#x27; ou les paramètres &#x27;date_debut&#x27; / &#x27;date_fin&#x27; doivent être renseignés. / Le paramètre &#x27;periode&#x27; ou les paramètres &#x27;date_debut&#x27; / &#x27;date_fin&#x27; doivent être renseignés. / La date de début renseignée doit être antérieure à la date de fin. / Le paramètre &#x27;date_fin&#x27; doit être inférieur ou égal à la date du jour. / Donnée(s) obligatoire(s) manquante(s) / Format(s) de donnée(s) incorrect(s)
500 | [ApiResponseFor500](#get_pce_id_pce_donnees_consos_publiees.ApiResponseFor500) | INTERNAL SERVER ERROR : Le serveur a rencontré une erreur lors de l’exécution de la requête, veuillez réessayer ultérieurement.

#### get_pce_id_pce_donnees_consos_publiees.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationXNdjson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationXNdjson
Type | Description  | Notes
------------- | ------------- | -------------
[**Model1**](../../models/Model1.md) |  | 


#### get_pce_id_pce_donnees_consos_publiees.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationXNdjson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationXNdjson
Type | Description  | Notes
------------- | ------------- | -------------
[**ConsoRestit400**](../../models/ConsoRestit400.md) |  | 


#### get_pce_id_pce_donnees_consos_publiees.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationXNdjson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationXNdjson
Type | Description  | Notes
------------- | ------------- | -------------
[**ConsoRestit500**](../../models/ConsoRestit500.md) |  | 


### Authorization

[OAuth (External)AccessCode](../../../README.md#OAuth (External)AccessCode), [OAuth (External)Implicit](../../../README.md#OAuth (External)Implicit)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

