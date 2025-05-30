from client.selenium_client import Selenium_client


class Harvest:
    def __init__(self, web_client: Selenium_client):
        self.web_client = web_client
