<a name="__pageTop"></a>
# grdf_client.apis.tags.donnes_techniques_api.DonnesTechniquesApi

All URIs are relative to *http://api.grdf.fr/adict/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_pce_id_pce_donnees_techniques**](#get_pce_id_pce_donnees_techniques) | **get** /pce/{id_pce}/donnees_techniques | Consulter les données techniques du PCE demandé

# **get_pce_id_pce_donnees_techniques**
<a name="get_pce_id_pce_donnees_techniques"></a>
> GetPceIdPceDonneesTechniques200Response get_pce_id_pce_donnees_techniques(id_pce)

Consulter les données techniques du PCE demandé

Ce service vous permet de consulter les données techniques d’un PCE.

### Example

* OAuth Authentication (OAuth (External)AccessCode):
* OAuth Authentication (OAuth (External)Implicit):
```python
import grdf_client
from grdf_client.apis.tags import donnes_techniques_api
from grdf_client.model.get_pce_id_pce_donnees_techniques400_response import GetPceIdPceDonneesTechniques400Response
from grdf_client.model.get_pce_id_pce_donnees_techniques500_response import GetPceIdPceDonneesTechniques500Response
from grdf_client.model.get_pce_id_pce_donnees_techniques200_response import GetPceIdPceDonneesTechniques200Response
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
    api_instance = donnes_techniques_api.DonnesTechniquesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id_pce': "48072888001528",
    }
    try:
        # Consulter les données techniques du PCE demandé
        api_response = api_instance.get_pce_id_pce_donnees_techniques(
            path_params=path_params,
        )
        pprint(api_response)
    except grdf_client.ApiException as e:
        print("Exception when calling DonnesTechniquesApi->get_pce_id_pce_donnees_techniques: %s\n" % e)
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
200 | [ApiResponseFor200](#get_pce_id_pce_donnees_techniques.ApiResponseFor200) | SUCCESS : Aucun droit d&#x27;accès pour tous les PCE en entrée. / Le client semble avoir déménagé et n&#x27;est plus titulaire de ce PCE, vous ne pouvez donc plus accéder à ses données. / Votre droit d’accès sur ce PCE a expiré. Pour continuer à accéder aux données, vous devez faire une nouvelle demande d&#x27;accès et, le cas échéant, renouveler le consentement du titulaire. / La preuve de consentement fournie lors du contrôle opéré par GRDF n’est pas valide. / Votre contrat GRDF ADICT est expiré. Veuillez prendre contact avec GRDF pour le renouveler. / GRDF a passé le droit d&#x27;accès à l&#x27;état obsolète. / Vos droits d’accès aux données des PCE ont été suspendus en raison d’une mauvaise utilisation de la plateforme. Veuillez prendre contact avec GRDF. / Le client titulaire a révoqué son consentement, vous ne pouvez plus accéder aux données de ce PCE. / GRDF a révoqué votre droit d’accès aux données de ce PCE à la demande du client titulaire. / Vous avez révoqué votre droit d’accès sur ce PCE. / Vous n&#x27;êtes pas autorisé à consulter les données de ce PCE. / Vous n&#x27;êtes pas ou plus autorisé à consulter les données de ce PCE. / Il n&#x27;y a pas de données correspondant à ce PCE sur la période demandée. / Le périmètre des données auxquelles vous avez accès pour ce PCE ne couvre pas les données techniques.
400 | [ApiResponseFor400](#get_pce_id_pce_donnees_techniques.ApiResponseFor400) | BAD REQUEST : L&#x27;identifiant du PCE n&#x27;est pas correctement formaté (GI+6 chiffres ou 14 chiffres).
500 | [ApiResponseFor500](#get_pce_id_pce_donnees_techniques.ApiResponseFor500) | INTERNAL SERVER ERROR : Le serveur a rencontré une erreur lors de l’exécution de la requête, veuillez réessayer ultérieurement.

#### get_pce_id_pce_donnees_techniques.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**GetPceIdPceDonneesTechniques200Response**](../../models/GetPceIdPceDonneesTechniques200Response.md) |  | 


#### get_pce_id_pce_donnees_techniques.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**GetPceIdPceDonneesTechniques400Response**](../../models/GetPceIdPceDonneesTechniques400Response.md) |  | 


#### get_pce_id_pce_donnees_techniques.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**GetPceIdPceDonneesTechniques500Response**](../../models/GetPceIdPceDonneesTechniques500Response.md) |  | 


### Authorization

[OAuth (External)AccessCode](../../../README.md#OAuth (External)AccessCode), [OAuth (External)Implicit](../../../README.md#OAuth (External)Implicit)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)
