import pytest
from utils.webdriversingleton import WebDriverSingleton


@pytest.fixture(scope="session")
def driver():
    WebDriverSingleton()
    yield WebDriverSingleton.get_driver()
    WebDriverSingleton.quit_driver()
