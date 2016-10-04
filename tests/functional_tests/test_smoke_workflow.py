import pytest

from .base_test import BaseTest

class SmokeTest(BaseTest):

    @classmethod
    def tearDownClass(cls):
        #This needs to be done from API, once we have API functions
        cls.base_page\
            .navigate_to_home()\
            .select_opportunity_with_opportunity_name("Opportunity By UI Smoke Test")\
            .click_on_delete()

    @pytest.mark.smoke
    def test_smoke_workflow(self):
        with_created_opportunity = self.base_page\
            .navigate_to_home()\
            .click_on_create()\
            .populate_create_opportunity_widget("Ice Cream", "Manual", "Opportunity By UI Smoke Test")\
            .click_on_create()\
            .click_on_brands()\
            .remove_brand_from_filter(["GALLIKER S"])

        self.assertFalse(with_created_opportunity.is_brand_present_in_power_ranking_grid("GALLIKER S"),
                         msg="Brand still exists in Power Ranking")

        with_saved_opportunity = \
            with_created_opportunity\
            .click_on_delist(["ABSOLUTE FRUITSHELLS MANGO", "ABSOLUTE SORBET LEMON"])\
            .click_on_analyze()\
            .wait_for_analysis_to_end()\
            .click_on_save()\
            .select_opportunity_filter_type("Ice Cream")\
            .wait_for_table_to_refresh()\

        self.assertTrue(with_saved_opportunity.is_opportunity_there_in_table("Opportunity By UI Smoke Test"),
                        msg="Opportunity did not get created.")

        with_opened_opportunity = \
            with_saved_opportunity\
            .select_opportunity_filter_type("Ice Cream")\
            .select_opportunity_with_opportunity_name("Opportunity By UI Smoke Test")\
            .click_on_open()

        self.current_state = with_opened_opportunity

        self.assertEquals(with_opened_opportunity.find_action_column_text_for_a_product("ABSOLUTE FRUITSHELLS MANGO"), "DELISTED",
                          msg="The opportunity was not properly saved")
        self.assertEquals(with_opened_opportunity.find_action_column_text_for_a_product("ABSOLUTE SORBET LEMON"), "DELISTED",
                          msg="The opportunity was not properly saved")

