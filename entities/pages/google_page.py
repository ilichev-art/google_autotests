from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class GooglePage:
    def __init__(self, driver):
        self.driver = driver
        self.search_box = (By.NAME, "q")

    def open_site(self):
        self.driver.get("https://www.google.com")
        return self

    def search(self, query):
        search_input = self.driver.find_element(*self.search_box)
        search_input.send_keys(query + Keys.RETURN)
        return self

    def title(self):
        return self.driver.title
