import time
from selenium.webdriver import ActionChains
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as EC
import selenium.webdriver.support.ui as ui
from . import opportunity_page

class ProductivityPage:

    def __init__(self, driver):
        self.driver = driver
        self.action = ActionChains(self.driver)
        try:
            ui.WebDriverWait(self.driver, 60).until(
                EC.visibility_of_any_elements_located((By.CSS_SELECTOR, "[colid='productName'] span")))
        except TimeoutException:
            raise TimeoutException("TimeOut")

        self.chart_area_id = "productivity-chart-area"
        self.power_ranking_area_id = "powerRankingContiner"
        self.change_summary_area_id = "changeSummaryChart"
        self.transfer_analysis_area_id = "volumeChart"

        self.chart_area_element = self.driver.find_element_by_id(self.chart_area_id)
        self.power_ranking_area = self.driver.find_element_by_id(self.power_ranking_area_id)
        self.all_product_names_in_power_ranking = self.driver.find_elements_by_css_selector('[colid="productName"] span')
        self.all_actions_in_power_ranking = self.driver.find_elements_by_css_selector('[colid="action"] button')
        self.brands_tab = self.driver.find_element_by_css_selector('[name="brands"]')
        self.all_brand_options = self.driver.find_elements_by_css_selector('#BrandFilter input')
        self.vendors_tab = self.driver.find_element_by_css_selector('[id="1"]')
        self.cdt_tab = self.driver.find_element_by_css_selector('[id="0"]')
        self.chart_bubbles = self.driver.find_elements_by_class_name('nv-point')
        self.brand_names_in_power_ranking_grid = self.driver.find_elements_by_css_selector('[colid="brandName"] span')
        self.analyze_button = self.driver.find_element_by_id('analyzeButton')
        self.save_button = self.driver.find_element_by_id('saveOpportunityButton')

    def is_power_ranking_populated_with_products(self):
        return ProductivityPage(self.driver)

    def click_on_brands(self):
        self.brands_tab.click()
        return ProductivityPage(self.driver)

    def click_on_vendors(self):
        self.vendors_tab.click()
        return ProductivityPage(self.driver)

    def click_on_cdt(self):
        self.cdt_tab.click()
        return ProductivityPage(self.driver)

    def click_on_analyze(self):
        self.analyze_button.click()
        return ProductivityPage(self.driver)

    def click_on_specific_brand(self, brand_name):
        return ProductivityPage(self.driver)

    def is_product_present_in_power_ranking(self, product_name):
        found = False
        row_num = 0
        all_product_names_in_power_ranking = self.driver.find_elements_by_css_selector('[colid="productName"] span')
        for element in range(0, len(self.all_product_names_in_power_ranking)):
            if all_product_names_in_power_ranking[element].text == product_name:
                found = True
                first_parent = all_product_names_in_power_ranking[element].find_element_by_xpath('..')
                row = first_parent.find_element_by_xpath('..')
                row_num = int(row.get_attribute("row"))
                break
        return found, row_num

    def click_on_delist(self, list_of_entities_to_be_delisted):
        for entity in list_of_entities_to_be_delisted:
            found, row = self.is_product_present_in_power_ranking(entity)
            if found is True:
                all_actions_in_power_ranking = self.driver.find_elements_by_css_selector('[colid="action"] button')
                all_actions_in_power_ranking[row].click()
        return ProductivityPage(self.driver)

    def find_action_column_text_for_a_product(self, product_name):
        for entity in range(0, len(self.all_product_names_in_power_ranking)):
            if self.all_product_names_in_power_ranking[entity].text == product_name:
                row_num = int(self.all_product_names_in_power_ranking[entity].find_element_by_xpath('..').find_element_by_xpath('..').get_attribute("row"))
                return self.all_actions_in_power_ranking[row_num].text
            else:
                Exception("Product name does not exist in Power Ranking grid")

    def remove_brand_from_filter(self, list_of_brand_names):
        for brand_name in list_of_brand_names:
            for option in self.all_brand_options:
                if option.get_attribute("label") == brand_name:
                    option.find_element_by_xpath('..').find_element_by_css_selector('div').click()
        return ProductivityPage(self.driver)

    def is_brand_present_in_power_ranking_grid(self, brand_name_to_be_checked):
        found = False
        for brand_name in self.brand_names_in_power_ranking_grid:
            if brand_name.text == brand_name_to_be_checked:
                found = True
        return found

    def click_on_save(self):
        self.save_button.click()
        return opportunity_page.OpportunityPage(self.driver)

    def is_transfer_analysis_populated(self):
        graph = self.driver.find_element_by_id("transferContainer").is_displayed()
        return graph

    def is_change_summary_populated(self):
        graph = self.driver.find_element_by_id("changeSummaryChart").is_displayed()
        return graph

    def wait_for_analysis_to_end(self):
        try:
            ui.WebDriverWait(self.driver, 60).until(
                EC.visibility_of_any_elements_located((By.ID, "transferContainer")))
        except TimeoutException:
            raise TimeoutException("TimeOut")

        return ProductivityPage(self.driver)
