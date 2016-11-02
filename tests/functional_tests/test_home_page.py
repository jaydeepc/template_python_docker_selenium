import pytest
import random

from .base_test import BaseTest

class HomePageTests(BaseTest):

    @classmethod
    def setUp(cls):
        super(HomePageTests, cls).setUpClass()
        cls.created_opportunity = cls.opportunity_api_client.create_opportunity("Ice Cream",
                                                                                "MANUAL",
                                                                                "api_created_opportunity_{0}".format(random.randint(1, 100))).json()
        cls.opportunity_id_1 = cls.created_opportunity.get("Opportunity").get("id")
        cls.opportunity_name = cls.created_opportunity.get("Opportunity").get("name")

    @classmethod
    def tearDownClass(cls):
        super(HomePageTests, cls).tearDownClass()
        cls.opportunity_api_client.delete_opportunity([cls.opportunity_id_1])
