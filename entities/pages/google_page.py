from __future__ import annotations
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from entities.base_page import BasePage
import logging
from config import BASE_URL

log = logging.getLogger(__name__)


class GooglePage(BasePage):
    _container = (By.NAME, "q")

    def assert_loaded(self, **kwargs) -> GooglePage:
        log.info('Assert Google Page loaded')
        return super().assert_loaded(self._container)

    def open_site(self):
        return self.open(BASE_URL)

    def search(self, query: str):
        self.type_text(self._container, query)
        self.find(self._container).send_keys(Keys.RETURN)
        return self.wait_for_title(query)

    def title(self) -> str:
        return self.driver.title
