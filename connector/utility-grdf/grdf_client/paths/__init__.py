# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from grdf_client.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    PCE_ID_PCE_DONNEES_CONSOS_INFORMATIVES = "/pce/{id_pce}/donnees_consos_informatives"
    PCE_ID_PCE_DONNEES_CONTRACTUELLES = "/pce/{id_pce}/donnees_contractuelles"
    DROIT_ACCES_ID_DROIT_ACCES = "/droit_acces/{id_droit_acces}"
    PCE_ID_PCE_DONNEES_CONSOS_PUBLIEES = "/pce/{id_pce}/donnees_consos_publiees"
    PCE_ID_PCE_DONNEES_INJECTIONS_PUBLIEES = "/pce/{id_pce}/donnees_injections_publiees"
    DROIT_ACCES_ID_DROIT_ACCES_PREUVES = "/droit_acces/{id_droit_acces}/preuves"
    PCE_ID_PCE_DONNEES_TECHNIQUES = "/pce/{id_pce}/donnees_techniques"
    PCE_ID_PCE_DROIT_ACCES = "/pce/{id_pce}/droit_acces"
    DROITS_ACCES = "/droits_acces"
