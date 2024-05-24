# grdf_client.model.demander_acces_out.DemanderAccesOut

informations spécifiques du droit d'accès crée, retournées par le service `/demander_acces` 

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | informations spécifiques du droit d&#x27;accès crée, retournées par le service &#x60;/demander_acces&#x60;  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id_pce** | str,  | str,  | identifiant du PCE | [optional] 
**role_tiers** | str,  | str,  | le rôle du tiers dans l&#x27;accès | [optional] must be one of ["AUTORISE_CONTRAT_FOURNITURE", "DETENTEUR_CONTRAT_FOURNITURE", ] 
**id_droit_acces** | str,  | str,  | UUID de l&#x27;accred | [optional] 
**etat_droit_acces** | str,  | str,  |  | [optional] 
**date_creation_droit_acces** | str, datetime,  | str,  | date de création du droit d&#x27;accès | [optional] value must conform to RFC-3339 date-time
**date_debut_droit_acces** | str, date,  | str,  | date du consentement déclarée à GRDF par le Tiers | [optional] value must conform to RFC-3339 full-date YYYY-MM-DD
**date_fin_droit_acces** | str, date,  | str,  | date de fin du consentement déclarée à GRDF par le Tiers | [optional] value must conform to RFC-3339 full-date YYYY-MM-DD
**nom_titulaire** | str,  | str,  | nom du titulaire si personne physique | [optional] 
**raison_sociale_du_titulaire** | str,  | str,  | raison sociale du titulaire si personne morale | [optional] 
**courriel_titulaire** | str,  | str,  |  | [optional] 
**numero_telephone_mobile_titulaire** | str,  | str,  |  | [optional] 
**code_postal** | str,  | str,  | code postal du PCE | [optional] 
**perim_donnees_conso_debut** | str, date,  | str,  |  | [optional] value must conform to RFC-3339 full-date YYYY-MM-DD
**perim_donnees_conso_fin** | str, date,  | str,  |  | [optional] value must conform to RFC-3339 full-date YYYY-MM-DD
**perim_donnees_contractuelles** | str,  | str,  |  | [optional] 
**perim_donnees_techniques** | str,  | str,  |  | [optional] 
**perim_donnees_informatives** | str,  | str,  |  | [optional] 
**perim_donnees_publiees** | str,  | str,  |  | [optional] 
**parcours** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

