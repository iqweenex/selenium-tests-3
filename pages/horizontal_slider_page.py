from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
from utils.logger import Logger
from elements.web_element import WebElement


class HorizontalSliderPage(BasePage):
    UNIQUE_ELEMENT_LOC = "content"
    CONTENT_AREA = "content"
    SLIDER = "//input[@type='range']"
    SLIDER_VALUE = "//*[@id='content']//*[@id='range']"

    def __init__(self, browser):
        super().__init__(browser)
        self.unique_element = WebElement(browser, self.UNIQUE_ELEMENT_LOC, "Область контента")
        self.page_name = "Horizontal slider page"
        self.slider = WebElement(browser, self.SLIDER, "Слайдер")
        self.slider_value = WebElement(browser, self.SLIDER_VALUE, "Видимое значение")

    def get_slider_value(self) -> float:
        value = float(self.slider.get_attribute("value"))
        Logger.info(f"Текущее значение слайдера: {value}")
        return value

    def get_displayed_value(self) -> float:
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

    def set_slider_value(self, target_value: float):
        self.slider.click()

        current_value = self.get_slider_value()
        step = self.get_slider_step()
        steps = int((target_value - current_value) / step)

        actions = ActionChains(self.browser.driver)

        if steps > 0:
            actions.send_keys(Keys.ARROW_RIGHT * steps)
        elif steps < 0:
            actions.send_keys(Keys.ARROW_LEFT * abs(steps))

        Logger.info(f"Слайдер устанавливаем на значение {target_value}")
        actions.perform()
