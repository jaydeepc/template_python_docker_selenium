from base_config import BaseConfig
import os

class WebdriverConfig(BaseConfig):

    def __init__(self):
        self.SECTION="WEBDRIVER"
        project_parent_dir = "paa_lite"
        current_dir = os.getcwd()
        config_path = "{0}/{1}/config/common.properties".format(current_dir, project_parent_dir)
        self.config = self.read_config(config_path)

    def hub_url(self):
        return self.config.get(self.SECTION, 'hub_url')

    def browser(self):
        return self.config.get(self.SECTION, 'browser')