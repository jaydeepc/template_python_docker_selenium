from tests.base_test import BaseTest


class OpportunityTests(BaseTest):

    def test_user_can_create_opportunity(self):
        new_opportunity_name = "Opportunity From UI Tests"
        new_opportunity = self.base_page\
                                .navigate_to_home()\
                                .click_on_create()\
                                .populate_create_opportunity_widget("Ice Cream", "Manual", new_opportunity_name)\
                                .click_on_create()

        self.assertTrue(self.base_page.navigate_to_home().find_opportunity_from_table(new_opportunity_name),
                        msg="The opportunity did not get created")
