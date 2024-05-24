# grdf_client.model.consommation.Consommation

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**date_debut_consommation** | str, date,  | str,  |  | [optional] value must conform to RFC-3339 full-date YYYY-MM-DD
**date_fin_consommation** | str, date,  | str,  |  | [optional] value must conform to RFC-3339 full-date YYYY-MM-DD
**flag_retour_zero** | bool,  | BoolClass,  |  | [optional] 
**volume_brut** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**coeff_calcul** | [**CoeffCalcul**](CoeffCalcul.md) | [**CoeffCalcul**](CoeffCalcul.md) |  | [optional] 
**volume_converti** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**energie** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**type_qualif_conso** | str,  | str,  |  | [optional] 
**sens_flux_gaz** | str,  | str,  |  | [optional] 
**statut_conso** | str,  | str,  |  | [optional] 
**journee_gaziere** | str, date,  | str,  |  | [optional] value must conform to RFC-3339 full-date YYYY-MM-DD
**type_conso** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

