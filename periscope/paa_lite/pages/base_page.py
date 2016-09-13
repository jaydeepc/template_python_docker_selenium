import unittest

from periscope.paa_lite import OpportunityPage


class BasePage(unittest.TestCase):

    def __init__(self, driver, base_url):
        self.base_url = base_url
        self.driver = driver

    def navigate_to_home(self):
        self.driver.get(self.base_url)
        return OpportunityPage()