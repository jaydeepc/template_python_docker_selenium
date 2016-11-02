import pytest
import random

from .api_base_test import APIBaseTest


class ProductivityPageAPITests(APIBaseTest):

    @classmethod
    def setUpClass(cls):
        super(ProductivityPageAPITests, cls).setUpClass()
        cls.cdt_type = "1"
        cls.opportunity_type = "MANUAL"
        cls.opportunity_name = "api_created_opportunity_{0}".format(random.randint(1, 100))
        cls.delisted_prod_id = 1
        cls.delisted_prod_name = "ABSOLUTE FRUITSHELLS MANGO "
        cls.product_to_compare = "PL Regular"
        cls.expected_tranfer_analysis_revenue = 7.5
        cls.expected_tranfer_analysis_volume = 24.6
        cls.expected_tranfer_analysis_profit = 42.6


        cls.opportunity = cls.opportunity_api_client.create_opportunity(cls.cdt_type, cls.opportunity_type, cls.opportunity_name).object
        cls.opportunity_id = cls.opportunity.opportunity.id


    @classmethod
    def tearDownClass(cls):
        cls.opportunity_api_client.delete_opportunity([cls.opportunity_id])

    @pytest.mark.productivity_page_api1
    def test_user_transfer_analysis_of_profit_is_correct(self):
        run_simulation = self.assortment_api_client.run_simulation(self.cdt_type, [self.delisted_prod_id])
        simulation_id = run_simulation.object.simulation_id

        products_by_simulation = self.assortment_api_client.get_products_by_simulation_id(simulation_id).object

        total_change = 0
        delisted_prod_change = 0

        for product in products_by_simulation:
            if product.brand == self.product_to_compare:
                prof_change = product.simulated_measures.profit - product.current_measures.profit
                total_change = total_change + prof_change
            elif product.product_display_name == self.delisted_prod_name:
                delisted_prod_change = product.simulated_measures.profit - product.current_measures.profit

        self.assertEquals(abs(round(total_change*100/delisted_prod_change, 1)), self.expected_tranfer_analysis_profit,
                          msg="The transfer analysis for Profit does not match")

    @pytest.mark.productivity_page_api
    def test_user_transfer_analysis_of_volume_is_correct(self):
        run_simulation = self.assortment_api_client.run_simulation(self.cdt_type, [self.delisted_prod_id])
        simulation_id = run_simulation.object.simulation_id

        products_by_simulation = self.assortment_api_client.get_products_by_simulation_id(simulation_id).object

        total_change = 0
        delisted_prod_change = 0

        for product in products_by_simulation:
            if product.brand == self.product_to_compare:
                vol_change = product.simulated_measures.volume - product.current_measures.volume
                total_change = total_change + vol_change
            elif product.product_display_name == self.delisted_prod_name:
                delisted_prod_change = product.simulated_measures.volume - product.current_measures.volume

        self.assertEquals(abs(round(total_change*100/delisted_prod_change, 1)), self.expected_tranfer_analysis_volume,
                          msg="The transfer analysis for Volume does not match")

    @pytest.mark.productivity_page_api
    def test_user_transfer_analysis_of_revenue_is_correct(self):
        run_simulation = self.assortment_api_client.run_simulation(self.cdt_type, [self.delisted_prod_id])
        simulation_id = run_simulation.object.simulation_id

        products_by_simulation = self.assortment_api_client.get_products_by_simulation_id(simulation_id).object

        total_change = 0
        delisted_prod_change = 0

        for product in products_by_simulation:
            if product.brand == self.product_to_compare:
                rev_change = product.simulated_measures.revenue - product.current_measures.revenue
                total_change = total_change + rev_change
            elif product.product_display_name == self.delisted_prod_name:
                delisted_prod_change = product.simulated_measures.revenue - product.current_measures.revenue

        self.assertEquals(abs(round(total_change*100/delisted_prod_change, 1)), self.expected_tranfer_analysis_revenue,
                          msg="The transfer analysis for Revenue does not match")

    @pytest.mark.productivity_page_api
    def test_user_can_retrieve_the_opportunity_details(self):
        opportunity_details = self.opportunity_api_client.get_opportunity_details(self.opportunity_id)
        self.assertEquals(200, opportunity_details.status_code, msg="The response code returned does not match expected value."
                                                         "Expected: {0}"
                                                         "Actual: {1}".format(200, opportunity_details.status_code))
        opportunity_details_object = opportunity_details.object

        print(vars(opportunity_details_object))
        self.assertEquals(opportunity_details_object.name, self.opportunity_name, msg="The opportunity name does not match")
        self.assertEquals(opportunity_details_object.type, self.opportunity_type, msg="The opportunity type does not match")
        self.assertEquals(opportunity_details_object.cdt_id, self.cdt_type, msg="The cdt id does not match")

    @pytest.mark.productivity_page_api
    def test_user_can_not_retrieve_the_opportunity_details_for_non_existing_opportunity(self):
        opportunity_details = self.opportunity_api_client.get_opportunity_details(9999)
        self.assertEquals(404, opportunity_details.status_code, msg="The response code returned does not match expected value."
                                                         "Expected: {0}"
                                                         "Actual: {1}".format(404, opportunity_details.status_code))

    @pytest.mark.productivity_page_api1
    def test_user_can_not_retrieve_the_opportunity_details_for_invalid_opportunity(self):
        opportunity_details = self.opportunity_api_client.get_opportunity_details("abcd")
        self.assertEquals(400, opportunity_details.status_code, msg="The response code returned does not match expected value."
                                                         "Expected: {0}"
                                                         "Actual: {1}".format(400, opportunity_details.status_code))

    @pytest.mark.productivity_page_api
    def test_user_can_not_retieve_products_for_invalid_simulation_id(self):
        products_details = self.assortment_api_client.get_products_by_simulation_id("abcd")
        self.assertEquals(400, products_details.status_code, msg="The response code returned does not match expected value."
                                                         "Expected: {0}"
                                                         "Actual: {1}".format(400, products_details.status_code))

    @pytest.mark.productivity_page_api
    def test_user_can_not_retieve_products_for_non_existent_simulation_id(self):
        products_details = self.assortment_api_client.get_products_by_simulation_id("99999")
        self.assertEquals(404, products_details.status_code, msg="The response code returned does not match expected value."
                                                         "Expected: {0}"
                                                         "Actual: {1}".format(404, products_details.status_code))

    @pytest.mark.productivity_page_api
    def test_user_can_not_run_simulation_for_invalid_product_ids(self):
        products_details = self.assortment_api_client.run_simulation(self.cdt_type, ["abcd", "efgh"])
        self.assertEquals(400, products_details.status_code, msg="The response code returned does not match expected value."
                                                         "Expected: {0}"
                                                         "Actual: {1}".format(400, products_details.status_code))

    @pytest.mark.productivity_page_api
    def test_user_can_not_run_simulation_for_non_existent_product_ids(self):
        products_details = self.assortment_api_client.run_simulation(self.cdt_type, [99999, 9999999])
        self.assertEquals(404, products_details.status_code, msg="The response code returned does not match expected value."
                                                         "Expected: {0}"
                                                         "Actual: {1}".format(404, products_details.status_code))

    @pytest.mark.productivity_page_api
    def test_user_can_not_run_simulation_for_invalid_cdt_id(self):
        products_details = self.assortment_api_client.run_simulation("abcd", [1])
        self.assertEquals(400, products_details.status_code, msg="The response code returned does not match expected value."
                                                         "Expected: {0}"
                                                         "Actual: {1}".format(400, products_details.status_code))

    @pytest.mark.productivity_page_api
    def test_user_can_not_get_cdt_tree_for_invalid_tree_id(self):
        details = self.assortment_api_client.get_cdt_tree("abcd")
        self.assertEquals(400, details.status_code, msg="The response code returned does not match expected value."
                                                         "Expected: {0}"
                                                         "Actual: {1}".format(400, details.status_code))

    @pytest.mark.productivity_page_api
    def test_user_can_not_get_cdt_tree_for_non_existent_tree_id(self):
        details = self.assortment_api_client.get_cdt_tree(999999)
        self.assertEquals(404, details.status_code, msg="The response code returned does not match expected value."
                                                         "Expected: {0}"
                                                         "Actual: {1}".format(404, details.status_code))
