from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import Logger


class BaseElement:
    def __init__(self, driver, web_element, name="Элемент"):
        self.driver = driver
        self.web_element = web_element
        self.name = name

    def click(self):
        Logger.info(f"Клик по элементу: '{self.name}'")
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.web_element)
        ).click()

    def get_text(self):
        Logger.info(f"Получение текста из элемента: '{self.name}'")
        text = self.web_element.text
        Logger.info(f"Получен текст: '{text}'")
        return text

    def get_attribute(self, attribute_name: str) -> str:
        value = self.web_element.get_attribute(attribute_name)
        Logger.debug(f"Получен атрибут '{attribute_name}': '{value}'")
        return value
