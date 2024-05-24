# grdf_client.model.demander_acces_in.DemanderAccesIn

informations transmises au service `/pce/{id_pce}/droit_acces`

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | informations transmises au service &#x60;/pce/{id_pce}/droit_acces&#x60; | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**code_postal** | str,  | str,  | code postal du PCE | 
**role_tiers** | str,  | str,  |  | must be one of ["AUTORISE_CONTRAT_FOURNITURE", "DETENTEUR_CONTRAT_FOURNITURE, AUTORISE_CONTRAT_INJECTION", "DETENTEUR_CONTRAT_INJECTION", ] 
**raison_sociale** | str,  | str,  | la raison sociale du titulaire si personne morale | [optional] 
**nom_titulaire** | str,  | str,  | le nom du titulaire si personne physique | [optional] 
**courriel_titulaire** | str,  | str,  | courriel utilisé par GRDF pour signifier au titulaire un nouveau droit d&#x27;accès par le tiers aux données de son PCE | [optional] 
**numero_telephone_mobile_titulaire** | str,  | str,  | Numéro de téléphone mobile du titulaire | [optional] 
**date_debut_droit_acces** | str, date,  | str,  | date du consentement déclarée à GRDF par le Tiers | [optional] value must conform to RFC-3339 full-date YYYY-MM-DD
**date_fin_droit_acces** | str, date,  | str,  | date de fin du consentement déclarée à GRDF par le Tiers | [optional] value must conform to RFC-3339 full-date YYYY-MM-DD
**perim_donnees_conso_debut** | str, date,  | str,  |  | [optional] value must conform to RFC-3339 full-date YYYY-MM-DD
**perim_donnees_conso_fin** | str, date,  | str,  |  | [optional] value must conform to RFC-3339 full-date YYYY-MM-DD
**perim_donnees_inj_debut** | str, date,  | str,  |  | [optional] value must conform to RFC-3339 full-date YYYY-MM-DD
**perim_donnees_inj_fin** | str, date,  | str,  |  | [optional] value must conform to RFC-3339 full-date YYYY-MM-DD
**perim_donnees_contractuelles** | str,  | str,  |  | [optional] 
**perim_donnees_techniques** | str,  | str,  |  | [optional] 
**perim_donnees_informatives** | str,  | str,  |  | [optional] 
**perim_donnees_publiees** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

