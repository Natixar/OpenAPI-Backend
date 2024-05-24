# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import grdf_client
from grdf_client.paths.pce_id_pce_donnees_consos_informatives import get  # noqa: E501
from grdf_client import configuration, schemas, api_client

from .. import ApiTestMixin


class TestPceIdPceDonneesConsosInformatives(ApiTestMixin, unittest.TestCase):
    """
    PceIdPceDonneesConsosInformatives unit test stubs
        Consulter les consommations informatives du PCE demandé  # noqa: E501
    """
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = get.ApiForget(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()
