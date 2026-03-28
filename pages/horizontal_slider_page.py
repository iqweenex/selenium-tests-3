from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
from locators.horizontal_slider_locators import HorizontalSliderLocators
from utils.logger import Logger
import random


class HorizontalSliderPage(BasePage):
    def open(self):
        self.open_url("/horizontal_slider")
        Logger.info("Открываем страницу horizontal slider")

    def get_slider_value(self) -> float:
        slider = self.find_element(HorizontalSliderLocators.SLIDER, "Слайдер")
        value = float(slider.web_element.get_attribute("value"))
        Logger.info(f"Текущее значение слайдера: {value}")
        return value

    def get_displayed_value(self) -> float:
        value_element = self.find_element(HorizontalSliderLocators.SLIDER_VALUE, "Видимое значение")
        value = float(value_element.get_text())
        Logger.info(f"Отображаемое значение: {value}")
        return value

    def get_random_value(self):
        slider = self.find_element(HorizontalSliderLocators.SLIDER, "Слайдер")
        step = self.get_slider_step()
        max_value = float(slider.web_element.get_attribute("max"))
        min_value = float(slider.web_element.get_attribute("min"))

        possible_values = []
        current = min_value + step
        while current < max_value:
            possible_values.append(round(current, 1))
            current += step

        return random.choice(possible_values)

    def get_slider_step(self) -> float:
        slider = self.find_element(HorizontalSliderLocators.SLIDER, "Слайдер")
        step = float(slider.web_element.get_attribute("step"))
        Logger.debug(f"Шаг слайдера: {step}")
        return step

    def set_slider_value(self):
        target_value = self.get_random_value()
        slider = self.find_element(HorizontalSliderLocators.SLIDER, "Слайдер")
        slider.click()

        current_value = self.get_slider_value()
        step = self.get_slider_step()
        steps = int((target_value - current_value) / step)

        actions = ActionChains(self.driver)

        if steps > 0:
            for _ in range(steps):
                actions.send_keys(Keys.ARROW_RIGHT)
        if steps < 0:
            for _ in range(abs(steps)):
                actions.send_keys(Keys.ARROW_LEFT)

        actions.perform()

        Logger.info(f"Слайдер установлен на значение {target_value}")

