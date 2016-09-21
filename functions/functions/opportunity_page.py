from .create_opportunity_widget import CreateOpportunityPage
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as EC
import selenium.webdriver.support.ui as ui


class OpportunityPage:

    def __init__(self, driver):
        self.driver = driver
        self.btn_create = "createButton"
        self.opportunity_name_col_in_table = '[colid="name"]'
        try:
            ui.WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "{0}".format(self.opportunity_name_col_in_table))))
        except TimeoutException:
            raise TimeoutException("TimeOut")

        self.all_elements_in_name_column = self.driver.find_elements_by_css_selector(self.opportunity_name_col_in_table)

    def click_on_create(self):
        self.ele_btn_create = self.driver.find_element_by_id(self.btn_create)
        self.ele_btn_create.click()
        return CreateOpportunityPage(self.driver)

    def is_opportunity_there_in_table(self, opportunity_name):
        found = False
        for element in self.all_elements_in_name_column:
            if element.text == opportunity_name:
                found = True
        return found