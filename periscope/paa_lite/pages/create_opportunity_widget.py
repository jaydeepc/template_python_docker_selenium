from selenium.webdriver.support.ui import Select

import opportunity_page


class CreateOpportunityPage:

    def __init__(self):
        self.select_cdt = ""
        self.select_opportunity_type = ""
        self.txt_opportunity_name = ""
        self.btn_create = ""
        self.btn_cancel = ""

        self.ele_select_cdt = Select(self.driver.find_element_by_class_name(self.select_cdt))
        self.ele_select_opportunity_type = Select(self.driver.find_element_by_class_name(self.select_opportunity_type))
        self.ele_txt_opportunity_name = self.driver.find_element_by_class_name(self.txt_opportunity_name)
        self.ele_btn_create = self.driver.find_element_by_class_name(self.btn_create)
        self.ele_btn_cancel = self.driver.find_element_by_class_name(self.btn_cancel)

    def populate_create_opportunity_widget(self, cdt, opportunity_type, opportunity_name):
        self.ele_select_cdt.select_by_visible_text(cdt)
        self.ele_select_opportunity_type.select_by_visible_text(opportunity_type)
        self.ele_txt_opportunity_name.send_keys(opportunity_name)

        return CreateOpportunityPage()

    def click_on_create(self):
        self.ele_btn_create.click()
        return CreateOpportunityPage()

    def click_on_cancel(self):
        self.ele_btn_cancel.click()
        return opportunity_page.OpportunityPage()