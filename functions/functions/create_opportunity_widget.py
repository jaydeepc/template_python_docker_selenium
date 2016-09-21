import time
from selenium.webdriver import ActionChains

from . import opportunity_page
from . import productivity_chart_page


class CreateOpportunityPage:

    def __init__(self, driver):
        self.driver = driver
        self.action = ActionChains(self.driver)

        self.select_cdt = "selectCdtDropdown"
        self.select_opportunity_type = "selectOpportunityDropdown"
        self.txt_opportunity_name = "opportunityNameInput"
        self.btn_create = "createOpportunityButton"
        self.btn_cancel = "cancelOpportunityButton"

        self.ele_select_cdt = self.driver.find_element_by_id(self.select_cdt)
        self.ele_select_opportunity_type = self.driver.find_element_by_id(self.select_opportunity_type)
        self.ele_txt_opportunity_name = self.driver.find_element_by_id(self.txt_opportunity_name)
        self.ele_btn_create = self.driver.find_element_by_id(self.btn_create)
        self.ele_btn_cancel = self.driver.find_element_by_id(self.btn_cancel)


    def populate_create_opportunity_widget(self, cdt, opportunity_type, opportunity_name):

        self.action.click(self.ele_select_cdt)
        self.action.perform()
        available_options_in_cdt_dropdown = self.driver.find_elements_by_css_selector("#{0} ul li".format(self.select_cdt))
        self.click_on_dropdown_option(available_options_in_cdt_dropdown, cdt)
        time.sleep(2)

        self.action.click(self.ele_select_opportunity_type)
        self.action.perform()
        available_options_in_type_dropdown = self.driver.find_elements_by_css_selector("#{0} ul li".format(self.select_opportunity_type))
        self.click_on_dropdown_option(available_options_in_type_dropdown, opportunity_type)

        self.ele_txt_opportunity_name.clear()
        self.ele_txt_opportunity_name.send_keys(opportunity_name)

        return CreateOpportunityPage(self.driver)

    def click_on_dropdown_option(self, available_options_in_dropdown, option_to_be_clicked):
        for option in available_options_in_dropdown:
            if option.text == option_to_be_clicked:
                option.click()

    def click_on_create(self):
        self.ele_btn_create.click()
        return productivity_chart_page.ProductivityPage(self.driver)

    def click_on_cancel(self):
        self.ele_btn_cancel.click()
        return opportunity_page.OpportunityPage(self.driver)