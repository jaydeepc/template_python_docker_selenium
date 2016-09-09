import unittest
from selenium import webdriver
from periscope.common_config.config import WebdriverConfig


class BaseTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        webdriver_config = WebdriverConfig()
        hub_url = webdriver_config.hub_url()
        browser = webdriver_config.browser()

        if browser == "firefox":
            capability = webdriver.DesiredCapabilities.FIREFOX
        elif browser == "chrome":
            capability = webdriver.DesiredCapabilities.CHROME
        else:
            raise Exception("Browser is not accepted")

        cls.driver = webdriver.Remote(hub_url, capability)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
