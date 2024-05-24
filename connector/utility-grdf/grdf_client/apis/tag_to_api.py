import typing_extensions

from grdf_client.apis.tags import TagValues
from grdf_client.apis.tags.droits_daccs_consommations_injections_donnes_contractuelles_et_techniques_api import DroitsDaccsConsommationsInjectionsDonnesContractuellesEtTechniquesApi
from grdf_client.apis.tags.donnes_contractuelles_api import DonnesContractuellesApi
from grdf_client.apis.tags.donnes_dinjection_api import DonnesDinjectionApi
from grdf_client.apis.tags.donnes_de_consommation_api import DonnesDeConsommationApi
from grdf_client.apis.tags.donnes_techniques_api import DonnesTechniquesApi
from grdf_client.apis.tags.droits_daccs_api import DroitsDaccsApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.DROITS_DACCS_CONSOMMATIONS_INJECTIONS_DONNES_CONTRACTUELLES_ET_TECHNIQUES: DroitsDaccsConsommationsInjectionsDonnesContractuellesEtTechniquesApi,
        TagValues.DONNES_CONTRACTUELLES: DonnesContractuellesApi,
        TagValues.DONNES_DINJECTION: DonnesDinjectionApi,
        TagValues.DONNES_DE_CONSOMMATION: DonnesDeConsommationApi,
        TagValues.DONNES_TECHNIQUES: DonnesTechniquesApi,
        TagValues.DROITS_DACCS: DroitsDaccsApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.DROITS_DACCS_CONSOMMATIONS_INJECTIONS_DONNES_CONTRACTUELLES_ET_TECHNIQUES: DroitsDaccsConsommationsInjectionsDonnesContractuellesEtTechniquesApi,
        TagValues.DONNES_CONTRACTUELLES: DonnesContractuellesApi,
        TagValues.DONNES_DINJECTION: DonnesDinjectionApi,
        TagValues.DONNES_DE_CONSOMMATION: DonnesDeConsommationApi,
        TagValues.DONNES_TECHNIQUES: DonnesTechniquesApi,
        TagValues.DROITS_DACCS: DroitsDaccsApi,
    }
)
