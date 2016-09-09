from selenium.webdriver.common.keys import Keys
from periscope.projects.paa_lite.tests.base_test import BaseTest


class OpportunityTests(BaseTest):

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://www.python.org")
        self.assertIn("Python", driver.title)
        elem = driver.find_element_by_name("q")
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "JD." not in driver.page_source

    def test_search_in_python_org_2_test(self):
        driver = self.driver
        driver.get("http://www.python.org")
        self.assertIn("Python", driver.title)
        elem = driver.find_element_by_name("q")
        elem.send_keys("asdadsadsadas")
        elem.send_keys(Keys.RETURN)
        assert "JD" not in driver.page_source
