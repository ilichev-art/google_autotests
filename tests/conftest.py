import pytest
from utils.webdriver import WebDriver


@pytest.fixture(scope="session", autouse=True)
def setup_teardown():
    WebDriver()
    yield WebDriver.get_driver()
    WebDriver.quit_driver()
