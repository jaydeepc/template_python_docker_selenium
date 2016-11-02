import unittest

from selenium import webdriver
from functions import BasePage

from ..config.config import WebdriverConfig
from api.paa_api_clients.opportunity_client.opportunity_client import OpportunityAPIClient

class BaseTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        webdriver_config = WebdriverConfig()
        hub_url = webdriver_config.hub_url()
        cls.base_url = "http://52.2.223.255"

        browser = webdriver_config.browser()
        cls.opportunity_api_client = OpportunityAPIClient(cls.base_url)

        if browser == "firefox":
            capability = webdriver.DesiredCapabilities.FIREFOX
        elif browser == "chrome":
            capability = webdriver.DesiredCapabilities.CHROME
        else:
            raise Exception("Browser is not accepted")

        cls.driver = webdriver.Chrome()
        cls.base_page = BasePage(cls.driver, cls.base_url)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
