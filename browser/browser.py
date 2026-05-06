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
        self._driver.set_page_load_timeout(self.PAGE_LOAD_TIMEOUT)
        self.main_handle = None
        self._wait = WebDriverWait(self._driver, timeout=self.DEFAULT_TIMEOUT)

    @property
    def driver(self) -> WebDriver:
        return self._driver

    def get(self, url: str) -> None:
        Logger.info(f"{self}: get {url}")
        max_retries = 3
        for attempt in range(max_retries):
            try:
                self._driver.get(url)
                break
            except WebDriverException as err:
                logging.error(f"{self}: attempt {attempt + 1}/{max_retries} - {err}")
                if attempt == max_retries - 1:
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

    def open_with_auth(self, url: str, username: str, password: str) -> None:
        auth_url = f"https://{username}:{password}@{url}"
        Logger.info(f"Выполнение Basic Auth для пользователя: {username}")
        self.get(auth_url)

    def execute_script(self, script: str, *args) -> None:
        Logger.info(f"{self}: execute script = {script} with {args}")
        try:
            self._driver.execute_script(script, *args)
        except WebDriverException as err:
            Logger.error(f"{self}: {err}")
            raise

    def wait_alert_present(self):
        Logger.info(f"{self} wait alert present")
        return self._wait.until(EC.alert_is_present())

    def switch_to_alert(self):
        self.wait_alert_present()
        Logger.info(f"{self}: switch to alert")
        return self.driver.switch_to.alert

    def get_alert_text(self):
        alert = self.switch_to_alert()
        Logger.info(f"{self}: get alert text")
        text = alert.text
        return text

    def accept_alert(self):
        alert = self.switch_to_alert()
        Logger.info(f"{self}: accept alert")
        alert.accept()

    def send_keys_alert(self, text: str):
        alert = self.switch_to_alert()
        Logger.info(f"{self}: send {text} to alert")
        alert.send_keys(text)

    def switch_to_frame(self, frame: BaseElement):
        Logger.info(f"{self}: switch to frame")
        return self.driver.switch_to.frame(frame.wait_for_presence())

    def trigger_js_alert(self, message: str = "I am a JS Alert"):
        Logger.info("Вызов JS Alert через JavaScript")
        self.execute_script(f"alert('{message}');")

    def trigger_js_confirm(self, message: str = "I am a JS Confirm"):
        Logger.info("Вызов JS Confirm через JavaScript")
        self.execute_script(f"confirm('{message}');")

    def trigger_js_prompt(self, message: str = "I am a JS Prompt"):
        Logger.info("Вызов JS Prompt через JavaScript")
        self.execute_script(f"prompt('{message}');")

    def get_window_handles(self) -> list:
        Logger.info(f"{self}: get window handles")
        return self._driver.window_handles

    def switch_to_window(self, window_handle: str) -> None:
        Logger.info(f"{self}: switch to window {window_handle}")
        self._driver.switch_to.window(window_handle)

    def get_current_window_handle(self) -> str:
        Logger.info(f"{self}: get current window handle")
        return self._driver.current_window_handle

    def switch_to_new_window(self) -> None:
        handles = self.get_window_handles()
        self.switch_to_window(handles[-1])

    def refresh(self) -> None:
        Logger.info(f"{self}: refresh page")
        self._driver.refresh()

    def scroll_to_bottom(self):
        Logger.info(f"{self}: scroll to bottom")
        self.execute_script("window.scrollTo(0, document.body.scrollHeight);")
