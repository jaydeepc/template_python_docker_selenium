import pytest
import random

from .api_base_test import APIBaseTest


class HomePageAPITests(APIBaseTest):

    @classmethod
    def setUpClass(cls):
        super(HomePageAPITests, cls).setUpClass()

    # @classmethod
    # def tearDownClass(cls):
    #     cls.opportunity_api_client.delete_opportunity([cls.opportunity_id_1])

    @pytest.mark.home_page_api
    def test_opportunity_filter(self):
        filter_cdt_ids = ["1"]
        response = self.opportunity_api_client.get_filtered_opportunities(type="CDT", filter=filter_cdt_ids)
        self.assertEquals(200, response.status_code, msg="The response code returned does not match expected value."
                                                         "Expected: {0}"
                                                         "Actual: {1}".format(200, response.status_code))
        filtered_list = response.entity
        filter_flag = True
        for opportunity in filtered_list.opportunities:
            print(opportunity.cdt_id)
            if opportunity.cdt_id not in filter_cdt_ids:
                filter_flag = False

        self.assertTrue(filter_flag, msg="The filter did not happen according to filter type selected.")


    @pytest.mark.home_page_api
    def test_user_can_retrieve_all_opportunities(self):
        response = self.opportunity_api_client.get_all_opportunities()
        all_opportunities = response.json()
        number_of_opportunities = len(all_opportunities.get("opportunities"))
        self.assertEquals(200, response.status_code, msg="The response code returned does not match expected value."
                                                         "Expected: {0}"
                                                         "Actual: {1}".format(200, response.status_code))

        new_opportunity = self.opportunity_api_client.create_opportunity("Ice Cream", "MANUAL",
                                                       "api_created_opportunity_{0}".format(random.randint(1, 100))).json()
        opportunity_id_1 = new_opportunity.get("Opportunity").get("id")

        new_list_all_opportunities = self.opportunity_api_client.get_all_opportunities().json()
        number_of_opportunities_after_add = len(new_list_all_opportunities.get("opportunities"))

        self.assertEquals(number_of_opportunities_after_add, number_of_opportunities + 1, msg="All opportunities are not returned")
        self.opportunity_api_client.delete_opportunity([opportunity_id_1])