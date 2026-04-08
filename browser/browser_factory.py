from enum import StrEnum

from selenium import webdriver

from utils.logger import Logger
from selenium.webdriver.remote.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


class AvailableDriverName(StrEnum):
    CHROME = "chrome"


class BrowserFactory:
    @staticmethod
    def get_driver(
            driver_name: AvailableDriverName = AvailableDriverName.CHROME,
            options: list[str] = None,
    ) -> WebDriver:
        if options is None:
            options = []

        Logger.info(f"Start web driver {driver_name}")
        if driver_name == AvailableDriverName.CHROME:
            chrome_options = webdriver.ChromeOptions()

            for option in options:
                chrome_options.add_argument(option)

            service = Service(ChromeDriverManager().install())
            driver = webdriver.Chrome(service=service, options=chrome_options)
        else:
            raise NotImplementedError(f"{driver_name} is not implemented")
        return driver
