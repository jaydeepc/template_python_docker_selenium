import unittest

import functions.opportunity_page as opportunity_page


class BasePage(unittest.TestCase):

    def __init__(self, driver, base_url):
        self.base_url = base_url
        self.driver = driver

    def navigate_to_home(self):
        self.driver.get(self.base_url)
        return opportunity_page.OpportunityPage(self.driver)
