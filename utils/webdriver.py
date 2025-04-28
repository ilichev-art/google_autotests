from __future__ import annotations

import logging

from selenium import webdriver
from selenium.common import WebDriverException
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

log = logging.getLogger(__name__)


class WebDriver:
    _instance: WebDriver | None = None
    _driver: webdriver.Chrome | None = None

    def __new__(cls) -> WebDriver:
        if cls._instance is None:
            try:
                log.debug('Creating new WebDriver instance...')
                cls._instance = super().__new__(cls)
                cls._driver = cls._initialize_driver()
            except Exception as e:
                log.exception('WebDriver initialization error')
                raise RuntimeError(f'Error creating driver: {e}') from e
        return cls._instance

    @staticmethod
    def _initialize_driver() -> webdriver.Chrome:
        try:
            log.debug('Setting ChromeOptions...')
            options = webdriver.ChromeOptions()
            options.add_argument("--start-maximized")
            options.add_argument("--disable-blink-features=AutomationControlled")
            options.add_experimental_option("excludeSwitches", ["enable-automation"])
            options.add_experimental_option("useAutomationExtension", False)

            log.debug('Installing ChromeDriverManager...')
            service = Service(ChromeDriverManager().install())
            driver = webdriver.Chrome(service=service, options=options)

            log.debug('Disabling webdriver flag in browser...')
            driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

            return driver
        except WebDriverException as e:
            log.error(f'Failed to initialize WebDriver\n{e}')
            raise RuntimeError(f'Failed to initialize WebDriver. {e}') from e

    @classmethod
    def get_driver(cls) -> webdriver.Chrome:
        if cls._driver is None:
            log.error("Driver not initialized. Please ensure proper initialization")
            raise RuntimeError('Driver not initialized')
        return cls._driver

    @classmethod
    def quit_driver(cls):
        if cls._driver:
            try:
                log.debug('Quitting the browser...')
                cls._driver.quit()
                cls._instance = None
                cls._driver = None
                log.info('Browser closed')
            except Exception as e:
                log.error(f'An unexpected error occurred during WebDriver teardown\n{e}')
                raise Exception(f'An unexpected error occurred during WebDriver teardown. {e}') from e
