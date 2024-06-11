<a name="__pageTop"></a>
# grdf_client.apis.tags.droits_daccs_api.DroitsDaccsApi

All URIs are relative to *http://api.grdf.fr/adict/v2*

| Method                                          | HTTP request                                  | Description                                               |
|-------------------------------------------------|-----------------------------------------------|-----------------------------------------------------------|
| [**consulter_acces**](#consulter_acces)         | **get** /droits_acces                         | Consulter mes droits d&#x27;accès                         |
| [**droit_acces**](#droit_acces)                 | **put** /pce/{id_pce}/droit_acces             | Déclarer l&#x27;accès aux données d&#x27;un PCE           |
| [**fin_acces**](#fin_acces)                     | **patch** /droit_acces/{id_droit_acces}       | Révoquer un droit d&#x27;accès en tant que tiers AUTORISE |
| [**p_ost__droits_acces**](#p_ost__droits_acces) | **post** /droits_acces                        | Consulter des droits d&#x27;accès spécifiques             |
| [**preuve**](#preuve)                           | **put** /droit_acces/{id_droit_acces}/preuves | Transmettre une preuve                                    |

# **consulter_acces**
<a name="consulter_acces"></a>
> ConsulterAcces200Response consulter_acces()

Consulter mes droits d'accès

Ce service vous permet de consulter l'ensemble de vos droits d'accès aux données des PCE.

### Example

* OAuth Authentication (OAuth (External)AccessCode):
* OAuth Authentication (OAuth (External)Implicit):
```python
import grdf_client
from grdf_client.apis.tags import droits_daccs_api
from grdf_client.model.consulter_acces401_response import ConsulterAcces401Response
from grdf_client.model.consulter_acces500_response import ConsulterAcces500Response
from grdf_client.model.consulter_acces409_response import ConsulterAcces409Response
from grdf_client.model.consulter_acces400_response import ConsulterAcces400Response
from grdf_client.model.consulter_acces200_response import ConsulterAcces200Response
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
    api_instance = droits_daccs_api.DroitsDaccsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Consulter mes droits d'accès
        api_response = api_instance.consulter_acces()
        pprint(api_response)
    except grdf_client.ApiException as e:
        print("Exception when calling DroitsDaccsApi->consulter_acces: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#consulter_acces.ApiResponseFor200) | SUCCESS : L&#x27;opération s&#x27;est déroulée avec succès. / Aucun droit d’accès trouvé.
400 | [ApiResponseFor400](#consulter_acces.ApiResponseFor400) | BAD REQUEST : Une erreur technique est survenue.
401 | [ApiResponseFor401](#consulter_acces.ApiResponseFor401) | UNAUTHORIZED : Une erreur technique est survenue.
500 | [ApiResponseFor500](#consulter_acces.ApiResponseFor500) | INTERNAL SERVER ERROR : Une erreur technique est survenue.
409 | [ApiResponseFor409](#consulter_acces.ApiResponseFor409) | CONFLICT : Une erreur technique est survenue.

#### consulter_acces.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationXNdjson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationXNdjson
Type | Description  | Notes
------------- | ------------- | -------------
[**ConsulterAcces200Response**](../../models/ConsulterAcces200Response.md) |  | 


#### consulter_acces.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationXNdjson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationXNdjson
Type | Description  | Notes
------------- | ------------- | -------------
[**ConsulterAcces400Response**](../../models/ConsulterAcces400Response.md) |  | 


#### consulter_acces.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationXNdjson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationXNdjson
Type | Description  | Notes
------------- | ------------- | -------------
[**ConsulterAcces401Response**](../../models/ConsulterAcces401Response.md) |  | 


#### consulter_acces.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationXNdjson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationXNdjson
Type | Description  | Notes
------------- | ------------- | -------------
[**ConsulterAcces500Response**](../../models/ConsulterAcces500Response.md) |  | 


#### consulter_acces.ApiResponseFor409
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor409ResponseBodyApplicationXNdjson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor409ResponseBodyApplicationXNdjson
Type | Description  | Notes
------------- | ------------- | -------------
[**ConsulterAcces409Response**](../../models/ConsulterAcces409Response.md) |  | 


### Authorization

[OAuth (External)AccessCode](../../../README.md#OAuth (External)AccessCode), [OAuth (External)Implicit](../../../README.md#OAuth (External)Implicit)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **droit_acces**
<a name="droit_acces"></a>
> DroitAcces201Response droit_acces(id_pcebody)

Déclarer l'accès aux données d'un PCE

Ce service vous permet de déclarer un droit d'accès préalablement à la consultation des données d'un PCE.

### Example

* OAuth Authentication (OAuth (External)AccessCode):
* OAuth Authentication (OAuth (External)Implicit):
```python
import grdf_client
from grdf_client.apis.tags import droits_daccs_api
from grdf_client.model.retour500_demander_acces import Retour500DemanderAcces
from grdf_client.model.retour400_demander_acces import Retour400DemanderAcces
from grdf_client.model.retour409_demander_acces import Retour409DemanderAcces
from grdf_client.model.retour404_demander_acces import Retour404DemanderAcces
from grdf_client.model.demander_acces_in import DemanderAccesIn
from grdf_client.model.droit_acces201_response import DroitAcces201Response
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
    api_instance = droits_daccs_api.DroitsDaccsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id_pce': "id_pce_example",
    }
    body = DemanderAccesIn(
        role_tiers="AUTORISE_CONTRAT_FOURNITURE",
        raison_sociale="BabaTech",
        nom_titulaire="null",
        code_postal="77900",
        courriel_titulaire="robert.dupont@dupont.fr",
        numero_telephone_mobile_titulaire="0699999999",
        date_debut_droit_acces="Fri Jul 05 02:00:00 CEST 2019",
        date_fin_droit_acces="Wed Jan 31 01:00:00 CET 2024",
        perim_donnees_conso_debut="Mon Jan 01 01:00:00 CET 2018",
        perim_donnees_conso_fin="Sun Dec 31 01:00:00 CET 2023",
        perim_donnees_inj_debut="Mon Jan 01 01:00:00 CET 2018",
        perim_donnees_inj_fin="Sun Dec 31 01:00:00 CET 2023",
        perim_donnees_contractuelles="Faux",
        perim_donnees_techniques="Faux",
        perim_donnees_informatives="Faux",
        perim_donnees_publiees="Vrai",
    )
    try:
        # Déclarer l'accès aux données d'un PCE
        api_response = api_instance.droit_acces(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except grdf_client.ApiException as e:
        print("Exception when calling DroitsDaccsApi->droit_acces: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**DemanderAccesIn**](../../models/DemanderAccesIn.md) |  | 


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
201 | [ApiResponseFor201](#droit_acces.ApiResponseFor201) | CREATED : L&#x27;opération s&#x27;est déroulée avec succès. / La demande d&#x27;accès est en attente de la validation du titulaire du PCE.
400 | [ApiResponseFor400](#droit_acces.ApiResponseFor400) | BAD REQUEST : Votre rôle dans la demande d&#x27;accès n&#x27;est pas renseigné. / Le nom ou la raison sociale du titulaire doit être renseigné. / Seul le nom ou la raison sociale du titulaire doit être renseigné. / Le format de la date de fin d&#x27;accès est incorrect. / Le périmètre d&#x27;accès doit être renseigné. / Le format du courriel du titulaire est incorrect. / Le code postal n&#x27;est pas renseigné. / Le courriel du titulaire n&#x27;est pas renseigné. / Le périmètre d&#x27;accès aux données contractuelles doit être renseigné à Vrai ou Faux. / La date de début du périmètre relatif aux données de consommation est obligatoire et doit être renseignée au format YYYY-MM-DD. / Le périmètre d&#x27;accès aux données techniques doit être renseigné à Vrai ou Faux. / Le périmètre d&#x27;accès aux données contractuelles doit être renseigné à Vrai ou Faux. / Le périmètre d&#x27;accès aux données publiées doit être renseigné à Vrai ou Faux. / Le périmètre d&#x27;accès aux données informatives doit être renseigné à Vrai ou Faux. / La date de fin du périmètre relatif aux données de consommation est obligatoire et doit être renseignée au format YYYY-MM-DD. / Le numéro de téléphone mobile du titulaire renseigné n&#x27;est pas correctement formaté. / La date de début du périmètre relatif aux données de consommation doit être renseignée au format YYYY-MM-DD ou null ou vide. / La date de fin du périmètre relatif aux données de consommation doit être renseignée au format YYYY-MM-DD ou null ou vide. / La date de début du droit d’accès est obligatoire et doit être renseignée au format YYYY-MM-DD. / La date de fin du droit d’accès est obligatoire et doit être renseignée au format YYYY-MM-DD. / Le format du code postal est incorrect. / Le format du PCE est incorrect.
500 | [ApiResponseFor500](#droit_acces.ApiResponseFor500) | INTERNAL SERVER ERROR : Une erreur technique est survenue.
404 | [ApiResponseFor404](#droit_acces.ApiResponseFor404) | NOT FOUND : Le PCE est inconnu.
409 | [ApiResponseFor409](#droit_acces.ApiResponseFor409) | CONFLICT : Un droit d&#x27;accès existe déjà. / Le contrat de fourniture de gaz est échu. / Le code postal ne correspond pas à l&#x27;adresse du PCE. / Le droit d&#x27;accès est révoqué. / La demande d&#x27;accès est incohérente. / La demande d&#x27;accès est en attente de la validation du titulaire du PCE. / La date de fin du droit d’accès doit être supérieure ou égale à la date du jour. / La date de début du droit d’accès doit être inférieure ou égale à la date du jour. / La date de début du périmètre relatif aux données de consommation doit être inférieure ou égale à la date du jour. / La date de fin du périmètre relatif aux données de consommation doit être supérieure ou égale à la date de début du périmètre relatif aux données de consommation. /  La date de fin du périmètre relatif aux données de consommation doit être inférieure ou égale à la date de fin du droit d’accès.

#### droit_acces.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**DroitAcces201Response**](../../models/DroitAcces201Response.md) |  | 


#### droit_acces.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Retour400DemanderAcces**](../../models/Retour400DemanderAcces.md) |  | 


#### droit_acces.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Retour500DemanderAcces**](../../models/Retour500DemanderAcces.md) |  | 


#### droit_acces.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Retour404DemanderAcces**](../../models/Retour404DemanderAcces.md) |  | 


#### droit_acces.ApiResponseFor409
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor409ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor409ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Retour409DemanderAcces**](../../models/Retour409DemanderAcces.md) |  | 


### Authorization

[OAuth (External)AccessCode](../../../README.md#OAuth (External)AccessCode), [OAuth (External)Implicit](../../../README.md#OAuth (External)Implicit)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **fin_acces**
<a name="fin_acces"></a>
> FinAcces200Response fin_acces(id_droit_acces)

Révoquer un droit d'accès en tant que tiers AUTORISE

Ce service vous permet de révoquer votre droit d'accès aux données d'un PCE.

### Example

* OAuth Authentication (OAuth (External)AccessCode):
* OAuth Authentication (OAuth (External)Implicit):
```python
import grdf_client
from grdf_client.apis.tags import droits_daccs_api
from grdf_client.model.fin_acces409_response import FinAcces409Response
from grdf_client.model.fin_acces200_response import FinAcces200Response
from grdf_client.model.fin_acces500_response import FinAcces500Response
from grdf_client.model.fin_acces404_response import FinAcces404Response
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
    api_instance = droits_daccs_api.DroitsDaccsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id_droit_acces': "id_droit_acces_example",
    }
    try:
        # Révoquer un droit d'accès en tant que tiers AUTORISE
        api_response = api_instance.fin_acces(
            path_params=path_params,
        )
        pprint(api_response)
    except grdf_client.ApiException as e:
        print("Exception when calling DroitsDaccsApi->fin_acces: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
id_droit_acces | IdDroitAccesSchema | | 

# IdDroitAccesSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#fin_acces.ApiResponseFor200) | SUCCESS : L&#x27;opération s&#x27;est déroulée avec succès.
500 | [ApiResponseFor500](#fin_acces.ApiResponseFor500) | INTERNAL SERVER ERROR : Une erreur technique est survenue.
404 | [ApiResponseFor404](#fin_acces.ApiResponseFor404) | NOT FOUND : Aucun droit d’accès trouvé.
409 | [ApiResponseFor409](#fin_acces.ApiResponseFor409) | CONFLICT : Le demande est incohérente. / Le droit d&#x27;accès à révoquer n&#x27;existe pas. / Une erreur technique est survenue.

#### fin_acces.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**FinAcces200Response**](../../models/FinAcces200Response.md) |  | 


#### fin_acces.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**FinAcces500Response**](../../models/FinAcces500Response.md) |  | 


#### fin_acces.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**FinAcces404Response**](../../models/FinAcces404Response.md) |  | 


#### fin_acces.ApiResponseFor409
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor409ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor409ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**FinAcces409Response**](../../models/FinAcces409Response.md) |  | 


### Authorization

[OAuth (External)AccessCode](../../../README.md#OAuth (External)AccessCode), [OAuth (External)Implicit](../../../README.md#OAuth (External)Implicit)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **p_ost__droits_acces**
<a name="p_ost__droits_acces"></a>
> ConsulterAcces200Response p_ost__droits_acces(body)

Consulter des droits d'accès spécifiques

Ce service vous permet de consulter l'ensemble de vos droits d'accès aux données des PCE en fonction des filtres saisis en entrée.

### Example

* OAuth Authentication (OAuth (External)AccessCode):
* OAuth Authentication (OAuth (External)Implicit):
```python
import grdf_client
from grdf_client.apis.tags import droits_daccs_api
from grdf_client.model.liste_acces_in import ListeAccesIn
from grdf_client.model.consulter_acces401_response import ConsulterAcces401Response
from grdf_client.model.consulter_acces500_response import ConsulterAcces500Response
from grdf_client.model.consulter_acces409_response import ConsulterAcces409Response
from grdf_client.model.consulter_acces400_response import ConsulterAcces400Response
from grdf_client.model.consulter_acces200_response import ConsulterAcces200Response
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
    api_instance = droits_daccs_api.DroitsDaccsApi(api_client)

    # example passing only required values which don't have defaults set
    body = ListeAccesIn(
        role_tiers="role_tiers_example",
        id_pce="id_pce_example",
        statut_controle_preuve="statut_controle_preuve_example",
        etat_droit_acces="etat_droit_acces_example",
    )
    try:
        # Consulter des droits d'accès spécifiques
        api_response = api_instance.p_ost__droits_acces(
            body=body,
        )
        pprint(api_response)
    except grdf_client.ApiException as e:
        print("Exception when calling DroitsDaccsApi->p_ost__droits_acces: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/x-ndjson', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ListeAccesIn**](../../models/ListeAccesIn.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#p_ost__droits_acces.ApiResponseFor200) | SUCCESS : L&#x27;opération s&#x27;est déroulée avec succès. / Aucun droit d’accès trouvé.
400 | [ApiResponseFor400](#p_ost__droits_acces.ApiResponseFor400) | BAD REQUEST : Une erreur technique est survenue.
401 | [ApiResponseFor401](#p_ost__droits_acces.ApiResponseFor401) | UNAUTHORIZED : Une erreur technique est survenue.
500 | [ApiResponseFor500](#p_ost__droits_acces.ApiResponseFor500) | INTERNAL SERVER ERROR : Une erreur technique est survenue.
409 | [ApiResponseFor409](#p_ost__droits_acces.ApiResponseFor409) | CONFLICT : Une erreur technique est survenue.

#### p_ost__droits_acces.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationXNdjson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationXNdjson
Type | Description  | Notes
------------- | ------------- | -------------
[**ConsulterAcces200Response**](../../models/ConsulterAcces200Response.md) |  | 


#### p_ost__droits_acces.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationXNdjson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationXNdjson
Type | Description  | Notes
------------- | ------------- | -------------
[**ConsulterAcces400Response**](../../models/ConsulterAcces400Response.md) |  | 


#### p_ost__droits_acces.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationXNdjson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationXNdjson
Type | Description  | Notes
------------- | ------------- | -------------
[**ConsulterAcces401Response**](../../models/ConsulterAcces401Response.md) |  | 


#### p_ost__droits_acces.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationXNdjson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationXNdjson
Type | Description  | Notes
------------- | ------------- | -------------
[**ConsulterAcces500Response**](../../models/ConsulterAcces500Response.md) |  | 


#### p_ost__droits_acces.ApiResponseFor409
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor409ResponseBodyApplicationXNdjson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor409ResponseBodyApplicationXNdjson
Type | Description  | Notes
------------- | ------------- | -------------
[**ConsulterAcces409Response**](../../models/ConsulterAcces409Response.md) |  | 


### Authorization

[OAuth (External)AccessCode](../../../README.md#OAuth (External)AccessCode), [OAuth (External)Implicit](../../../README.md#OAuth (External)Implicit)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **preuve**
<a name="preuve"></a>
> Preuve200Response preuve(id_droit_acces)

Transmettre une preuve

Ce service vous permet de transmettre une ou plusieurs preuves de consentement pour un droit d'accès spécifique.

### Example

* OAuth Authentication (OAuth (External)AccessCode):
* OAuth Authentication (OAuth (External)Implicit):
```python
import grdf_client
from grdf_client.apis.tags import droits_daccs_api
from grdf_client.model.preuve_request import PreuveRequest
from grdf_client.model.retour400_transmettre_preuve import Retour400TransmettrePreuve
from grdf_client.model.retour409_transmettre_preuve import Retour409TransmettrePreuve
from grdf_client.model.retour500_transmettre_preuve import Retour500TransmettrePreuve
from grdf_client.model.preuve200_response import Preuve200Response
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
    api_instance = droits_daccs_api.DroitsDaccsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id_droit_acces': "id_droit_acces_example",
    }
    try:
        # Transmettre une preuve
        api_response = api_instance.preuve(
            path_params=path_params,
        )
        pprint(api_response)
    except grdf_client.ApiException as e:
        print("Exception when calling DroitsDaccsApi->preuve: %s\n" % e)

    # example passing only optional values
    path_params = {
        'id_droit_acces': "id_droit_acces_example",
    }
    body = None
    try:
        # Transmettre une preuve
        api_response = api_instance.preuve(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except grdf_client.ApiException as e:
        print("Exception when calling DroitsDaccsApi->preuve: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyMultipartFormData, Unset] | optional, default is unset |
path_params | RequestPathParams | |
content_type | str | optional, default is 'multipart/form-data' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyMultipartFormData
Type | Description  | Notes
------------- | ------------- | -------------
[**PreuveRequest**](../../models/PreuveRequest.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
id_droit_acces | IdDroitAccesSchema | | 

# IdDroitAccesSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#preuve.ApiResponseFor200) | SUCCESS : L&#x27;opération s&#x27;est déroulée avec succès.
400 | [ApiResponseFor400](#preuve.ApiResponseFor400) | BAD REQUEST : La forme de la requête est incorrecte.
500 | [ApiResponseFor500](#preuve.ApiResponseFor500) | INTERNAL SERVER ERROR : Une erreur technique est survenue.
409 | [ApiResponseFor409](#preuve.ApiResponseFor409) | CONFLICT : Le nombre maximal autorisé de 3 preuves est dépassé. / Une ou plusieurs preuves ne possèdent pas un format autorisé. / GRDF ne demande pas de preuve sur ce droit d&#x27;accès. / Le contrat de fourniture de gaz est échu. / La taille maximale autorisée de 4Mo d’une ou plusieurs preuves est dépassée. / Le traitement n&#x27;a pu aboutir car une ou plusieurs preuves sont corrompues et présentent un risque de sécurité.

#### preuve.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Preuve200Response**](../../models/Preuve200Response.md) |  | 


#### preuve.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Retour400TransmettrePreuve**](../../models/Retour400TransmettrePreuve.md) |  | 


#### preuve.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Retour500TransmettrePreuve**](../../models/Retour500TransmettrePreuve.md) |  | 


#### preuve.ApiResponseFor409
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor409ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor409ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Retour409TransmettrePreuve**](../../models/Retour409TransmettrePreuve.md) |  | 


### Authorization

[OAuth (External)AccessCode](../../../README.md#OAuth (External)AccessCode), [OAuth (External)Implicit](../../../README.md#OAuth (External)Implicit)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

