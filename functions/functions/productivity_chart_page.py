from selenium.webdriver import ActionChains


class ProductivityPage:

    def __init__(self, driver):
        self.driver = driver
        self.action = ActionChains(self.driver)

