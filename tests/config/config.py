from tests.config.base_config import BaseConfig


class WebdriverConfig(BaseConfig):

    def __init__(self):
        self.SECTION="WEBDRIVER"
        config_path = "tests/config/common.properties"
        self.config = self.read_config(config_path)

    def hub_url(self):
        return self.config.get(self.SECTION, 'hub_url')

    def browser(self):
        return self.config.get(self.SECTION, 'browser')