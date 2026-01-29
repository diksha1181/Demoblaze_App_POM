import os
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class Import_libraries:

    By = By
    WebDriverWait = WebDriverWait

    _driver = None
    keep_browser_open = False   # IMPORTANT for CI

    @classmethod
    def get_driver(cls):
        if cls._driver is None:

            remote_url = os.environ.get("SELENIUM_REMOTE_URL")
            headless = os.environ.get("SELENIUM_HEADLESS", "0") == "1"

            options = Options()

            # --- CI / Docker safe options ---
            if headless:
                options.add_argument("--headless=new")
                print("Running in headless mode")

            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--window-size=1920,1080")

            if remote_url:
                print(f"Using remote Selenium server at {remote_url}")
                cls._driver = webdriver.Remote(
                    command_executor=remote_url,
                    options=options
                )
            else:
                print("Using local Chrome driver")
                service = Service(ChromeDriverManager().install())
                cls._driver = webdriver.Chrome(
                    service=service,
                    options=options
                )

        return cls._driver

    @classmethod
    def quit_driver(cls):
        if cls._driver is not None:
            cls._driver.quit()
            cls._driver = None
