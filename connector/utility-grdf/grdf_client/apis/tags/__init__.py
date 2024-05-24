# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from grdf_client.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    DROITS_DACCS_CONSOMMATIONS_INJECTIONS_DONNES_CONTRACTUELLES_ET_TECHNIQUES = "Droits d&#x27;accès, Consommations, Injections, Données contractuelles et techniques"
    DONNES_CONTRACTUELLES = "Données contractuelles"
    DONNES_DINJECTION = "Données d&#x27;injection"
    DONNES_DE_CONSOMMATION = "Données de consommation"
    DONNES_TECHNIQUES = "Données techniques"
    DROITS_DACCS = "Droits d&#x27;accès"
