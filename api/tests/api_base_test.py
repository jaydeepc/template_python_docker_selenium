import unittest

from api.paa_api_clients.opportunity_client.opportunity_client import OpportunityAPIClient
from api.paa_api_clients.assortment_client.assortment_client import AssortmentAPIClient


class APIBaseTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.base_url_opportunity_service = "http://52.2.223.255/OpportunityService"
        cls.base_url_assortment_service = "http://52.2.223.255/AssortmentService"
        cls.opportunity_api_client = OpportunityAPIClient(cls.base_url_opportunity_service)
        cls.assortment_api_client = AssortmentAPIClient(cls.base_url_assortment_service)
