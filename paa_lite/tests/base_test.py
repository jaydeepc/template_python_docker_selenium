import unittest

from paa_lite.paa_lite_pages.base_page import BasePage
from selenium import webdriver

from paa_lite.config.config import WebdriverConfig


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
        cls.base_page = BasePage(cls.driver, "http://52.2.223.255")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
