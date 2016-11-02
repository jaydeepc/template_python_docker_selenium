import pytest
import random

from .api_base_test import APIBaseTest


class HomePageAPITests(APIBaseTest):

    @classmethod
    def setUpClass(cls):
        super(HomePageAPITests, cls).setUpClass()

    @pytest.mark.home_page_api
    def test_opportunity_filter(self):
        filter_cdt_ids = ["1"]
        response = self.opportunity_api_client.get_filtered_opportunities(type="CDT", filter=filter_cdt_ids)
        self.assertEquals(200, response.status_code, msg="The response code returned does not match expected value."
                                                         "Expected: {0}"
                                                         "Actual: {1}".format(200, response.status_code))
        filtered_list = response.object
        filter_flag = True
        for opportunity in filtered_list.opportunities:
            print(opportunity.cdt_id)
            if opportunity.cdt_id not in filter_cdt_ids:
                filter_flag = False

        self.assertTrue(filter_flag, msg="The filter did not happen according to filter type selected.")

    @pytest.mark.home_page_api
    def test_user_can_retrieve_all_opportunities(self):
        response = self.opportunity_api_client.get_all_opportunities()
        all_opportunities = response.object
        number_of_opportunities = len(all_opportunities.opportunities)
        self.assertEquals(200, response.status_code, msg="The response code returned does not match expected value."
                                                         "Expected: {0}"
                                                         "Actual: {1}".format(200, response.status_code))

        new_opportunity = self.opportunity_api_client.create_opportunity("1", "MANUAL",
                                                       "api_created_opportunity_{0}".format(random.randint(1, 100))).object

        opportunity_id_1 = new_opportunity.opportunity.id

        new_list_all_opportunities = self.opportunity_api_client.get_all_opportunities()
        number_of_opportunities_after_add = len(new_list_all_opportunities.object.opportunities)

        self.assertEquals(number_of_opportunities_after_add, number_of_opportunities + 1, msg="All opportunities are not returned")
        self.opportunity_api_client.delete_opportunity([opportunity_id_1])

    @pytest.mark.home_page_api
    def test_user_can_not_filter_with_invalid_cdt_id(self):
        filter_cdt_ids = ["abcd"]
        response = self.opportunity_api_client.get_filtered_opportunities(type="CDT", filter=filter_cdt_ids)
        self.assertEquals(400, response.status_code, msg="The response code returned does not match expected value."
                                                         "Expected: {0}"
                                                         "Actual: {1}".format(400, response.status_code))

    @pytest.mark.home_page_api
    def test_user_can_not_filter_with_invalid_cdt_type(self):
        filter_cdt_ids = ["1"]
        response = self.opportunity_api_client.get_filtered_opportunities(type="abcd", filter=filter_cdt_ids)
        self.assertEquals(400, response.status_code, msg="The response code returned does not match expected value."
                                                         "Expected: {0}"
                                                         "Actual: {1}".format(400, response.status_code))

    @pytest.mark.home_page_api
    def test_user_can_create_a_new_opportunity(self):
        cdt_type = "1"
        opportunity_type = "MANUAL"
        opportunity_name = "api_created_opportunity_{0}".format(random.randint(1, 100))
        response = self.opportunity_api_client.create_opportunity(cdt_type, opportunity_type, opportunity_name)
        self.assertEquals(200, response.status_code, msg="The response code returned does not match expected value."
                                                         "Expected: {0}"
                                                         "Actual: {1}".format(200, response.status_code))

        new_opportunity = response.object
        opportunity_id = new_opportunity.opportunity.id

        list_all_opportunities = self.opportunity_api_client.get_all_opportunities().object
        found = False
        for opportunity in list_all_opportunities.opportunities:
            if opportunity.id == opportunity_id:
                found = True
                self.assertEquals(opportunity.name, opportunity_name, msg="The opportunity name does not match.\n"
                                                                          "Expected Name: {0} \n"
                                                                          "Actual Name: {1}".format(opportunity_name, opportunity.name))

                self.assertEquals(opportunity.cdt_id, cdt_type, msg="The CDT type id does not match.\n"
                                                                          "Expected CDT ID: {0} \n"
                                                                          "Actual CDT ID: {1}".format(cdt_type, opportunity.cdt_id))

                self.assertEquals(opportunity.type, opportunity_type, msg="The CDT type id does not match.\n"
                                                                          "Expected CDT ID: {0} \n"
                                                                          "Actual CDT ID: {1}".format(opportunity_type, opportunity.type))

        self.assertTrue(found, msg="The opportunity did not get created")
        self.opportunity_api_client.delete_opportunity([opportunity_id])

    @pytest.mark.home_page_api
    def test_user_can_not_create_a_new_opportunity_with_invalid_cdt_type(self):
        cdt_type = "abcd"
        opportunity_type = "MANUAL"
        opportunity_name = "api_created_opportunity_{0}".format(random.randint(1, 100))
        response = self.opportunity_api_client.create_opportunity(cdt_type, opportunity_type, opportunity_name)
        self.assertEquals(400, response.status_code, msg="The response code returned does not match expected value."
                                                         "Expected: {0}"
                                                         "Actual: {1}".format(400, response.status_code))

    @pytest.mark.home_page_api
    def test_user_can_not_create_a_new_opportunity_with_invalid_opportunity_type(self):
        cdt_type = "1"
        opportunity_type = "abcd"
        opportunity_name = "api_created_opportunity_{0}".format(random.randint(1, 100))
        response = self.opportunity_api_client.create_opportunity(cdt_type, opportunity_type, opportunity_name)
        self.assertEquals(400, response.status_code, msg="The response code returned does not match expected value."
                                                         "Expected: {0}"
                                                         "Actual: {1}".format(400, response.status_code))

    @pytest.mark.home_page_api
    def test_user_can_not_create_a_new_opportunity_with_blank_name(self):
        cdt_type = "1"
        opportunity_type = "MANUAL"
        opportunity_name = ""
        response = self.opportunity_api_client.create_opportunity(cdt_type, opportunity_type, opportunity_name)
        self.assertEquals(400, response.status_code, msg="The response code returned does not match expected value."
                                                         "Expected: {0}"
                                                         "Actual: {1}".format(400, response.status_code))

    @pytest.mark.home_page_api
    def test_user_can_delete_an_opportunity(self):
        new_opp = self.opportunity_api_client.get_existing_opportunity_or_create()
        delete_opp = self.opportunity_api_client.delete_opportunity([int(new_opp.id)])
        self.assertEquals(200, delete_opp.status_code, msg="The response code returned does not match expected value."
                                                         "Expected: {0}"
                                                         "Actual: {1}".format(200, delete_opp.status_code))
        get_all_opportunities = self.opportunity_api_client.get_all_opportunities().object
        found = False
        for opp in get_all_opportunities.opportunities:
            if int(opp.id) == int(new_opp.id):
                found = True
        self.assertFalse(found, msg="The opportunity still available and did not get deleted,\n"
                                    "even after successful request.")

    @pytest.mark.home_page_api
    def test_user_can_not_delete_an_opportunity_with_invalid_id(self):
        delete_opp = self.opportunity_api_client.delete_opportunity(["abcd"])
        self.assertEquals(400, delete_opp.status_code, msg="The response code returned does not match expected value."
                                                         "Expected: {0}"
                                                         "Actual: {1}".format(400, delete_opp.status_code))

    @pytest.mark.home_page_api
    def test_user_can_not_delete_an_opportunity_with_nonexistent_id(self):
        delete_opp = self.opportunity_api_client.delete_opportunity([9999])
        self.assertEquals(404, delete_opp.status_code, msg="The response code returned does not match expected value."
                                                         "Expected: {0}"
                                                         "Actual: {1}".format(404, delete_opp.status_code))

    