import unittest

from selenium import webdriver
from functions import BasePage

from ..config.config import WebdriverConfig


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

        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(5)
        cls.base_url = "http://52.2.223.255/opportunities"
        cls.base_page = BasePage(cls.driver, cls.base_url)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
