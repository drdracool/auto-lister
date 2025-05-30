from selenium import webdriver


class Selenium_client:
    def __init__(self):
        self.driver = self.create_brower()

    def create_brower(self) -> webdriver:
        driver = webdriver.Chrome()
        return driver
