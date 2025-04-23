import pytest
from utils.webdriver import WebDriver


@pytest.fixture(scope="session")
def driver():
    WebDriver()
    yield WebDriver.get_driver()
    WebDriver.quit_driver()
