import pytest
from .base_test import BaseTest


class OpportunityTests(BaseTest):

    @pytest.mark.opportunity
    def test_user_can_create_opportunity(self):
        new_opportunity_name = "Opportunity From UI Tests"
        self.base_page\
            .navigate_to_home()\
            .click_on_create()\
            .populate_create_opportunity_widget("Ice Cream", "Manual", new_opportunity_name)\
            .click_on_create()

        self.assertTrue(self.base_page.navigate_to_home().is_opportunity_there_in_table(new_opportunity_name),
                        msg="The opportunity did not get created")

    def test_user_can_not_create_opportunity_with_blank_name(self):
        new_opportunity_name = ""
        self.base_page\
            .navigate_to_home()\
            .click_on_create()\
            .populate_create_opportunity_widget("Ice Cream", "Manual", new_opportunity_name)\
            .click_on_create()

        self.assertFalse(self.base_page.navigate_to_home().is_opportunity_there_in_table(new_opportunity_name),
                        msg="The opportunity got created with blank name")

    def test_user_can_not_create_opportunity_with_blank_cdt(self):
        new_opportunity_name = "Opportunity From UI Tests"
        self.base_page\
            .navigate_to_home()\
            .click_on_create()\
            .populate_create_opportunity_widget("", "Manual", new_opportunity_name)\
            .click_on_create()

        self.assertFalse(self.base_page.navigate_to_home().is_opportunity_there_in_table(new_opportunity_name),
                        msg="The opportunity got created with blank CDT.")

    def test_user_can_not_create_opportunity_with_blank_opportunity_type(self):
        new_opportunity_name = "Opportunity From UI Tests"
        self.base_page\
            .navigate_to_home()\
            .click_on_create()\
            .populate_create_opportunity_widget("Ice Cream", "", new_opportunity_name)\
            .click_on_create()

        self.assertFalse(self.base_page.navigate_to_home().is_opportunity_there_in_table(new_opportunity_name),
                        msg="The opportunity got created with blank Opportunity type")
