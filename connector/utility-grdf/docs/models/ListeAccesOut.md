# grdf_client.model.liste_acces_out.ListeAccesOut

liste des droits d'accès retournée par le service `/consulter_acces`

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | liste des droits d&#x27;accès retournée par le service &#x60;/consulter_acces&#x60; | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id_droit_acces** | str,  | str,  | UUID de l&#x27;accreditation | [optional] 
**id_pce** | str,  | str,  | identifiant du PCE | [optional] 
**role_tiers** | str,  | str,  | le rôle du tiers dans l&#x27;accès | [optional] must be one of ["AUTORISE_CONTRAT_FOURNITURE", "DETENTEUR_CONTRAT_FOURNITURE, AUTORISE_CONTRAT_INJECTION", "DETENTEUR_CONTRAT_INJECTION", ] 
**raison_sociale_du_tiers** | str,  | str,  |  | [optional] 
**nom_titulaire** | str,  | str,  |  | [optional] 
**raison_sociale_du_titulaire** | str,  | str,  |  | [optional] 
**courriel_titulaire** | str,  | str,  |  | [optional] 
**numero_telephone_mobile_titulaire** | str,  | str,  |  | [optional] 
**code_postal** | str,  | str,  | code postal du PCE | [optional] 
**date_debut_droit_acces** | str, date,  | str,  |  | [optional] value must conform to RFC-3339 full-date YYYY-MM-DD
**date_fin_droit_acces** | str, date,  | str,  |  | [optional] value must conform to RFC-3339 full-date YYYY-MM-DD
**perim_donnees_conso_debut** | str, date,  | str,  | Date de début d’autorisation du périmètre des données de consommation (AAAA-MM-JJ) | [optional] value must conform to RFC-3339 full-date YYYY-MM-DD
**perim_donnees_conso_fin** | str, date,  | str,  | Date de fin d’autorisation du périmètre des données de consommation (AAAA-MM-JJ) | [optional] value must conform to RFC-3339 full-date YYYY-MM-DD
**perim_donnees_inj_debut** | str, date,  | str,  | Date de début d’autorisation du périmètre des données d&#x27;injection (AAAA-MM-JJ) | [optional] value must conform to RFC-3339 full-date YYYY-MM-DD
**perim_donnees_inj_fin** | str, date,  | str,  | Date de fin d’autorisation du périmètre des données d&#x27;injection (AAAA-MM-JJ) | [optional] value must conform to RFC-3339 full-date YYYY-MM-DD
**perim_donnees_contractuelles** | str,  | str,  |  | [optional] 
**perim_donnees_techniques** | str,  | str,  |  | [optional] 
**perim_donnees_informatives** | str,  | str,  |  | [optional] 
**perim_donnees_publiees** | str,  | str,  |  | [optional] 
**date_creation** | str, datetime,  | str,  | date de création du droit d&#x27;accès | [optional] value must conform to RFC-3339 date-time
**etat_droit_acces** | str,  | str,  |  | [optional] 
**date_revocation** | str, datetime,  | str,  | date de révocation du droit d&#x27;accès | [optional] value must conform to RFC-3339 date-time
**source_revocation** | str,  | str,  | la source du passage à l&#x27;état révoqué | [optional] 
**date_passage_a_obsolete** | str, datetime,  | str,  | date de passage à l état obsolète du droit d&#x27;accès | [optional] value must conform to RFC-3339 date-time
**source_passage_a_obsolete** | str,  | str,  | origine du passage à l état obsolète | [optional] 
**date_passage_a_refuse** | str, datetime,  | str,  | la date de passage à l&#x27;état refusé | [optional] value must conform to RFC-3339 date-time
**source_passage_a_refuse** | str,  | str,  | la source de passage à l&#x27;état refusé | [optional] 
**parcours** | str,  | str,  |  | [optional] 
**statut_controle_preuve** | str,  | str,  |  | [optional] 
**date_limite_transmission_preuve** | str, date,  | str,  |  | [optional] value must conform to RFC-3339 full-date YYYY-MM-DD
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

