import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pytest

class OpportunityTests(unittest.TestCase):

    def setUp(self):
        capability = webdriver.DesiredCapabilities.FIREFOX
        self.driver = webdriver.Remote("http://localhost:4444/wd/hub", capability)

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://www.python.org")
        self.assertIn("Python", driver.title)
        elem = driver.find_element_by_name("q")
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source

    def test_search_in_python_org_2_test(self):
        driver = self.driver
        driver.get("http://www.python.org")
        self.assertIn("Python", driver.title)
        elem = driver.find_element_by_name("q")
        elem.send_keys("asdadsadsadas")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()