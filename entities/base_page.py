from __future__ import annotations
import logging
from typing import Tuple
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import TimeoutException

from utils.webdriversingleton import WebDriverSingleton

log = logging.getLogger(__name__)


class BasePage:
    """Базовый класс для всех страниц"""

    def __init__(self):
        self.driver: WebDriver = WebDriverSingleton.get_driver()

    def assert_loaded(self, container_locator: Tuple[str, str], timeout: int = 10):
        """Проверка, что страница загружена по видимости контейнера."""
        log.debug(f"Waiting for element {container_locator} to be visible...")
        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(container_locator))
            log.info(f"Page loaded successfully, container {container_locator} is visible.")
        except TimeoutException:
            log.error(f"Page failed to load within {timeout} seconds. Element not found: {container_locator}")
            raise AssertionError(f"Page did not load. Missing element: {container_locator}")
        return self

    def open(self, url: str) -> BasePage:
        """Открытие страницы"""
        log.info(f"Open url: {url}")
        self.driver.get(url)
        return self

    def find(self, locator: Tuple[str, str]) -> WebElement:
        """Поиск одного элемента"""
        log.info(f"Finding element by locator: {locator}")
        return self.driver.find_element(*locator)

    def find_all(self, locator: Tuple[str, str]) -> list[WebElement]:
        """Поиск всех элементов"""
        log.info(f"Finding all elements by locator: {locator}")
        return self.driver.find_elements(*locator)

    def wait_for_visible(self, locator: Tuple[str, str], timeout: int = 10) -> WebElement:
        """Ожидание видимости элемента"""
        log.info(f"Waiting for visible element: {locator}")
        try:
            return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            log.error(f"Element not visible: {locator}")
            raise AssertionError(f"Элемент {locator} не стал видимым за {timeout} секунд.")

    def wait_for_clickable(self, locator: Tuple[str, str], timeout: int = 10) -> WebElement:
        """Ожидание кликабельности элемента"""
        log.info(f"Waiting clickable element: {locator}")
        try:
            return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
        except TimeoutException:
            log.error(f"Element not clickable: {locator}")
            raise AssertionError(f"Элемент {locator} не стал кликабельным за {timeout} секунд.")

    def wait_for_title(self, text: str, timeout: int = 10) -> BasePage:
        """Ожидание видимости заголовка страницы"""
        log.info(f"Waiting for page title to contain: '{text}'")
        try:
            WebDriverWait(self.driver, timeout).until(EC.title_contains(text))
        except TimeoutException:
            raise AssertionError(f"Title does not contain expected text: '{text}'")
        return self

    def type_text(self, locator: Tuple[str, str], text: str) -> BasePage:
        """Ввод текста в поле для ввода"""
        log.info(f"Typing into element {locator}: '{text}'")
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)
        return self

    def click(self, locator: Tuple[str, str]) -> BasePage:
        """Клик по элементу"""
        log.info(f"Clicking on element: {locator}")
        element = self.wait_for_clickable(locator)
        element.click()
        return self
