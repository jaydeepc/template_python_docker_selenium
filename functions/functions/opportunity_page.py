import create_opportunity_widget

class OpportunityPage:

    def __init__(self):
        self.btn_create = "CREATE"
        self.ele_btn_create = self.driver.find_element_by_class_name(self.btn_create)

    def click_on_create(self):
        self.ele_btn_create.click()
        return create_opportunity_widget.CreateOpportunityPage()

    def find_opportunity_from_table(self, opportunity_name):
        return OpportunityPage()