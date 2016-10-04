import pytest

from .base_test import BaseTest


class OpportunityTests(BaseTest):

    @classmethod
    def setUpClass(cls):
        super(OpportunityTests, cls).setUpClass()
        cls.opportunity_name = "Opportunity From UI Tests"

    @classmethod
    def tearDownClass(cls):
        #This needs to be done from API, once we have API functions
        # cls.base_page\
        #     .navigate_to_home()\
        #     .select_opportunity_with_opportunity_name(cls.opportunity_name)\
        #     .click_on_delete()
        pass

    @pytest.mark.opportunity4
    def test_user_can_create_opportunity(self):
        self.base_page\
            .navigate_to_home()\
            .click_on_create()\
            .populate_create_opportunity_widget("Ice Cream", "Manual", self.opportunity_name)\
            .click_on_create()

        found, _ = self.base_page.navigate_to_home().is_opportunity_there_in_table(self.opportunity_name)
        self.assertTrue(found, msg="The opportunity did not get created")

    @pytest.mark.opportunity
    def test_user_can_not_create_opportunity_with_blank_name(self):
        new_opportunity_name = ""
        self.base_page\
            .navigate_to_home()\
            .click_on_create()\
            .populate_create_opportunity_widget("Ice Cream", "Manual", new_opportunity_name)\
            .click_on_create()

        found, _ = self.base_page.navigate_to_home().is_opportunity_there_in_table(new_opportunity_name)
        self.assertTrue(found, msg="The opportunity got created with blank name")

    @pytest.mark.opportunity
    def test_user_can_not_create_opportunity_with_blank_cdt(self):
        new_opportunity_name = "Opportunity From UI Tests"
        self.base_page\
            .navigate_to_home()\
            .click_on_create()\
            .populate_create_opportunity_widget("", "Manual", new_opportunity_name)\
            .click_on_create()

        found, _ = self.base_page.navigate_to_home().is_opportunity_there_in_table(new_opportunity_name)
        self.assertTrue(found, msg="The opportunity got created with blank CDT.")

    @pytest.mark.opportunity
    def test_user_can_not_create_opportunity_with_blank_opportunity_type(self):
        self.base_page\
            .navigate_to_home()\
            .click_on_create()\
            .populate_create_opportunity_widget("Ice Cream", "", self.opportunity_name)\
            .click_on_create()

        found, _ = self.base_page.navigate_to_home().is_opportunity_there_in_table(self.opportunity_name)
        self.assertTrue(found, msg="The opportunity got created with blank Opportunity type")

    @pytest.mark.opportunity
    def test_opportunity_does_not_get_created_when_cancel_is_clicked(self):
        new_opportunity_name = "Opportunity From UI Tests - Cancel"
        self.base_page\
            .navigate_to_home()\
            .click_on_create()\
            .populate_create_opportunity_widget("Ice Cream", "Manual", new_opportunity_name)\
            .click_on_cancel()

        found, _ = self.base_page.navigate_to_home().is_opportunity_there_in_table(new_opportunity_name)
        self.assertTrue(found, msg="The opportunity got created even on clicking cancel")
