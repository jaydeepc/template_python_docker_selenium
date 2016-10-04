import time

from .create_opportunity_widget import CreateOpportunityPage
from .productivity_chart_page import ProductivityPage
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as EC
import selenium.webdriver.support.ui as ui
from selenium.webdriver import ActionChains
from .common import Common

class OpportunityPage:

    def __init__(self, driver):
        self.driver = driver
        self.action = ActionChains(self.driver)

        self.btn_create = "createButton"
        self.opportunity_name_col_in_table = '[colid="name"]'
        self.opportunity_select_box = '[colid="select"] .ag-selection-checkbox'
        self.delete_button_id = "deleteButton"
        self.open_button_id = "openButton"
        self.opportunity_filter_dropdown_id = "opportunityFilterDropdown"

        try:
            ui.WebDriverWait(driver, 30).until(
                    EC.visibility_of_element_located((By.CSS_SELECTOR, "{0}".format(self.opportunity_name_col_in_table))))
        except TimeoutException:
            raise TimeoutException("TimeOut")

        self.all_elements_in_name_column = self.driver.find_elements_by_css_selector(self.opportunity_name_col_in_table)
        self.all_opportunity_select_boxes = self.driver.find_elements_by_css_selector(self.opportunity_select_box)
        self.delete_button = self.driver.find_element_by_id(self.delete_button_id)
        self.open_button = self.driver.find_element_by_id(self.open_button_id)
        self.opportunity_filter_dropdown_ele = self.driver.find_element_by_id(self.opportunity_filter_dropdown_id)

    def click_on_create(self):
        self.ele_btn_create = self.driver.find_element_by_id(self.btn_create)
        self.ele_btn_create.click()
        return CreateOpportunityPage(self.driver)

    def select_opportunity_with_opportunity_name(self, opportunity_name):
        found, row_number = self.is_opportunity_there_in_table(opportunity_name)
        if found is True:
            self.all_opportunity_select_boxes[row_number - 1].click()
            return OpportunityPage(self.driver)
        else:
            raise Exception("The opportunity to select does not exist!")

    def click_on_delete(self):
        self.delete_button.click()
        return OpportunityPage(self.driver)

    def click_on_open(self):
        self.open_button.click()
        return ProductivityPage(self.driver)

    def is_opportunity_there_in_table(self, opportunity_name):
        found = False
        row_number = 0
        for element in range(0, len(self.all_elements_in_name_column)):
            if self.all_elements_in_name_column[element].text == opportunity_name:
                found = True
                row_number = element
        return found, row_number

    def select_opportunity_filter_type(self, opportunity_name):
        self.action.click(self.opportunity_filter_dropdown_ele)
        self.action.perform()
        available_options_in_opportunity_dropdown = self.driver.find_elements_by_css_selector("#{0} ul li".format(self.opportunity_filter_dropdown_id))
        Common().click_on_dropdown_option(available_options_in_opportunity_dropdown, opportunity_name)
        return OpportunityPage(self.driver)

    def find_opportunity_in_table(self, opportunity_name):
        found = False
        all_elements_in_name_column = self.driver.find_elements_by_css_selector(self.opportunity_name_col_in_table)
        for element in range(0, len(all_elements_in_name_column)):
            print (all_elements_in_name_column[element].text + "-" + opportunity_name)
            if all_elements_in_name_column[element].text == opportunity_name:
                found = True
        return found

    def wait_for_table_to_refresh(self):
        #Need to implement logical wait here
        time.sleep(5)
        return OpportunityPage(self.driver)