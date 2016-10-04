import unittest
import os

from api.paa_api_clients.opportunity_client.client import OpportunityAPIClient


class APIBaseTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        os.environ["CAFE_ENGINE_CONFIG_FILE_PATH"] = "."
        cls.base_url = "http://52.2.223.255/OpportunityService"
        cls.opportunity_api_client = OpportunityAPIClient(cls.base_url)
