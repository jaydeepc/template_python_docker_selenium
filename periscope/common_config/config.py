from base_config import BaseConfig
import os

class WebdriverConfig(BaseConfig):

    def __init__(self):
        self.SECTION="WEBDRIVER"
        self.config = self.read_config('/Users/jaydeepc/Documents/work/paa_lite/functional_tests_python/periscope/common_config/common.properties')

    def hub_url(self):
        return self.config.get(self.SECTION, 'hub_url')

    def browser(self):
        return self.config.get(self.SECTION, 'browser')