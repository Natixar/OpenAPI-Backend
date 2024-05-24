# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import grdf_client
from grdf_client.paths.droit_acces_id_droit_acces import patch  # noqa: E501
from grdf_client import configuration, schemas, api_client

from .. import ApiTestMixin


class TestDroitAccesIdDroitAcces(ApiTestMixin, unittest.TestCase):
    """
    DroitAccesIdDroitAcces unit test stubs
        Révoquer un droit d'accès en tant que tiers AUTORISE  # noqa: E501
    """
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = patch.ApiForpatch(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()
