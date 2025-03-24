from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class WebDriver:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(WebDriver, cls).__new__(cls)
            cls._instance.driver = cls._initialize_driver()
        return cls._instance

    @staticmethod
    def _initialize_driver():
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option("useAutomationExtension", False)

        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)

        driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

        return driver

    @classmethod
    def get_driver(cls):
        return cls().driver

    @classmethod
    def quit_driver(cls):
        if cls._instance:
            cls._instance.driver.quit()
            cls._instance = None
