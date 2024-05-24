import typing_extensions

from grdf_client.paths import PathValues
from grdf_client.apis.paths.pce_id_pce_donnees_consos_informatives import PceIdPceDonneesConsosInformatives
from grdf_client.apis.paths.pce_id_pce_donnees_contractuelles import PceIdPceDonneesContractuelles
from grdf_client.apis.paths.droit_acces_id_droit_acces import DroitAccesIdDroitAcces
from grdf_client.apis.paths.pce_id_pce_donnees_consos_publiees import PceIdPceDonneesConsosPubliees
from grdf_client.apis.paths.pce_id_pce_donnees_injections_publiees import PceIdPceDonneesInjectionsPubliees
from grdf_client.apis.paths.droit_acces_id_droit_acces_preuves import DroitAccesIdDroitAccesPreuves
from grdf_client.apis.paths.pce_id_pce_donnees_techniques import PceIdPceDonneesTechniques
from grdf_client.apis.paths.pce_id_pce_droit_acces import PceIdPceDroitAcces
from grdf_client.apis.paths.droits_acces import DroitsAcces

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.PCE_ID_PCE_DONNEES_CONSOS_INFORMATIVES: PceIdPceDonneesConsosInformatives,
        PathValues.PCE_ID_PCE_DONNEES_CONTRACTUELLES: PceIdPceDonneesContractuelles,
        PathValues.DROIT_ACCES_ID_DROIT_ACCES: DroitAccesIdDroitAcces,
        PathValues.PCE_ID_PCE_DONNEES_CONSOS_PUBLIEES: PceIdPceDonneesConsosPubliees,
        PathValues.PCE_ID_PCE_DONNEES_INJECTIONS_PUBLIEES: PceIdPceDonneesInjectionsPubliees,
        PathValues.DROIT_ACCES_ID_DROIT_ACCES_PREUVES: DroitAccesIdDroitAccesPreuves,
        PathValues.PCE_ID_PCE_DONNEES_TECHNIQUES: PceIdPceDonneesTechniques,
        PathValues.PCE_ID_PCE_DROIT_ACCES: PceIdPceDroitAcces,
        PathValues.DROITS_ACCES: DroitsAcces,
    }
)

path_to_api = PathToApi(
    {
        PathValues.PCE_ID_PCE_DONNEES_CONSOS_INFORMATIVES: PceIdPceDonneesConsosInformatives,
        PathValues.PCE_ID_PCE_DONNEES_CONTRACTUELLES: PceIdPceDonneesContractuelles,
        PathValues.DROIT_ACCES_ID_DROIT_ACCES: DroitAccesIdDroitAcces,
        PathValues.PCE_ID_PCE_DONNEES_CONSOS_PUBLIEES: PceIdPceDonneesConsosPubliees,
        PathValues.PCE_ID_PCE_DONNEES_INJECTIONS_PUBLIEES: PceIdPceDonneesInjectionsPubliees,
        PathValues.DROIT_ACCES_ID_DROIT_ACCES_PREUVES: DroitAccesIdDroitAccesPreuves,
        PathValues.PCE_ID_PCE_DONNEES_TECHNIQUES: PceIdPceDonneesTechniques,
        PathValues.PCE_ID_PCE_DROIT_ACCES: PceIdPceDroitAcces,
        PathValues.DROITS_ACCES: DroitsAcces,
    }
)
