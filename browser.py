import logging

from selenium.common import WebDriverException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from elements.base_element import BaseElement
from utils.logger import Logger


class Browser:
    DEFAULT_TIMEOUT = 10
    PAGE_LOAD_TIMEOUT = 120

    def __init__(self, driver: WebDriver):
        self._driver = driver
        self._driver.set_page_load_time(self.PAGE_LOAD_TIMEOUT)
        self.main_handle = None
        self._wait = WebDriverWait(self._driver, timeout=self.DEFAULT_TIMEOUT)

    @property
    def driver(self) -> WebDriver:
        return self._driver

    def get(self, url: str) -> None:
        Logger.info(f"{self}: get {url}")
        try:
            self._driver.get(url)
        except WebDriverException as err:
            logging.error(f"{self}: {err}")
            raise
        self.main_handle = self._driver.current_window_handle

    def close(self) -> None:
        Logger.info(f"{self} close window handle = {self._driver.current_window_handle}")
        self._driver.close()

    def quit(self) -> None:
        logging.info(f"{self} quit")
        try:
            self._driver.quit()
        except WebDriverException as err:
            logging.error(f"{self}: {err}")
            raise

    def wait_alert_present(self):
        Logger.info(f"{self} wait alert present")
        return self._wait.until(EC.alert_is_present())

    def switch_to_alert(self):
        Logger.info(f"{self}: switch to alert")
        self.wait_alert_present()
        return self.driver.switch_to.alert

    def get_alert_text(self):
        Logger.info(f"{self}: get alert text")
        return self.switch_to_alert().text

    def accept_alert(self):
        Logger.info(f"{self}: accept alert")
        self.switch_to_alert().accept()

    def send_keys_alert(self, text:str):
        Logger.info(f"{self}: send {text} to alert")
        self.switch_to_alert().send_keys(text)

    def switch_to_frame(self, frame: BaseElement):
        Logger.info(f"{self}: switch to frame")
        return self.driver.switch_to.frame(frame.wait_for_presence())
