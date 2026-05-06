from utils.logger import Logger
from browser.browser import Browser


class BasePage:
    UNIQUE_ELEMENT_LOC = None

    def __init__(self, browser: Browser):
        self.browser = browser
        self.page_name = None
        self.unique_element = None

    def wait_for_open(self) -> None:
        Logger.info(f"{self}: wait for open")
        self.unique_element.wait_for_presence()
