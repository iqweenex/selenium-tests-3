from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import Logger
from elements.base_element import BaseElement


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "http://the-internet.herokuapp.com"

    def open_url(self, url):
        full_url = f"{self.base_url}{url}"
        Logger.info(f"Открытие страницы: {full_url}")
        self.driver.get(full_url)

    def find_element(self, locator: tuple, name: str = "Элемент", timeout: int = 10) -> BaseElement:
        Logger.debug(f"Поиск элемента '{name}' по локатору: {locator}")
        WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator),
            message=f"Элемент '{name}' не найден за {timeout} секунд"
        )
        return BaseElement(self.driver, locator, name)
