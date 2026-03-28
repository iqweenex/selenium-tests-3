from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import Logger


class BaseElement:
    def __init__(self, driver, locator, name="Элемент"):
        self.driver = driver
        self.locator = locator
        self.name = name
        self._element = None

    def find(self, time=10):
        if self._element is None:
            Logger.debug(f"Поиск элемента '{self.name}' по локатору: {self.locator}")
            self._element = WebDriverWait(self.driver, time).until(
                EC.presence_of_element_located(self.locator),
                message=f"Не удалось найти элемент '{self.name}' по локатору: {self.locator}"
            )
        return self._element

    @property
    def web_element(self):
        return self.find()


    def click(self):
        Logger.info(f"Клик по элементу: '{self.name}'")
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.locator)
        )
        element.click()

    def get_text(self):
        Logger.info(f"Получение текста из элемента: '{self.name}'")
        element_text = self.find().text
        Logger.info(f"Получен текст: '{element_text}'")
        return element_text
