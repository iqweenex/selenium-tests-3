from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
from locators.horizontal_slider_locators import HorizontalSliderLocators
from utils.logger import Logger
from elements.web_element import WebElement
import random


class HorizontalSliderPage(BasePage):
    UNIQUE_ELEMENT_LOC = HorizontalSliderLocators.CONTENT_AREA

    def __init__(self, browser):
        super().__init__(browser)
        self.unique_element = WebElement(browser, self.UNIQUE_ELEMENT_LOC, "Область контента")
        self.page_name = "Horizontal slider page"
        self.slider = WebElement(browser, HorizontalSliderLocators.SLIDER, "Слайдер")
        self.slider_value = WebElement(browser, HorizontalSliderLocators.SLIDER_VALUE, "Видимое значение")

    def open(self):
        self.browser.get("https://the-internet.herokuapp.com/horizontal_slider")
        self.wait_for_open()
        Logger.info(f"{self}: {self.page_name} открыта")
        return self

    def get_slider_value(self) -> float:
        value = float(self.slider.get_attribute("value"))
        Logger.info(f"Текущее значение слайдера: {value}")
        return value

    def get_displayed_value(self) -> float:
        self.slider_value.wait_for_presence()
        value = float(self.slider_value.get_text())
        Logger.info(f"Отображаемое значение: {value}")
        return value

    def get_slider_step(self) -> float:
        step = float(self.slider.get_attribute("step"))
        Logger.debug(f"Шаг слайдера: {step}")
        return step

    def get_max_value(self) -> float:
        return float(self.slider.get_attribute("max"))

    def get_min_value(self) -> float:
        return float(self.slider.get_attribute("min"))

    def get_random_value(self) -> float:
        step = self.get_slider_step()
        max_value = self.get_max_value()
        min_value = self.get_min_value()

        possible_values = []
        current = min_value + step
        while current < max_value:
            possible_values.append(round(current, 1))
            current += step

        return random.choice(possible_values)

    def set_slider_value(self):
        target_value = self.get_random_value()
        self.slider.click()

        current_value = self.get_slider_value()
        step = self.get_slider_step()
        steps = int((target_value - current_value) / step)

        actions = ActionChains(self.browser.driver)

        if steps > 0:
            for _ in range(steps):
                actions.send_keys(Keys.ARROW_RIGHT)
        elif steps<0:
            for _ in range(-steps):
                actions.send_keys(Keys.ARROW_LEFT)

        actions.perform()

        Logger.info(f"Слайдер установлен на значение {target_value}")
        return self
