import pytest
from utils.webdriver import WebDriver


@pytest.fixture(scope="session", autouse=True)
def setup_teardown():
    driver = WebDriver.get_driver()
    yield driver
    WebDriver.quit_driver()
