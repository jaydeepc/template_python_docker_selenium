import unittest
from selenium import webdriver
from periscope.common_config.config import WebdriverConfig


class BaseTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        webdriver_config = WebdriverConfig()
        hub_url = webdriver_config.hub_url()
        capability = webdriver.DesiredCapabilities.FIREFOX
        cls.driver = webdriver.Remote(hub_url, capability)
        print cls.driver

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
