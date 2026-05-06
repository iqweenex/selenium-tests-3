from pages.horizontal_slider.horizontal_slider_page import HorizontalSliderPage
from utils.logger import Logger
import random


class TestHorizontalSlider:
    URL_HORIZONTAL_SLIDER_PAGE = "https://the-internet.herokuapp.com/horizontal_slider"
    def test_horizontal_slider_random_value(self, browser):
        slider_page = HorizontalSliderPage(browser)
        Logger.info("Тест Horizontal Slider")

        Logger.info(f"Открываем страницу {slider_page.page_name}")
        browser.get(self.URL_HORIZONTAL_SLIDER_PAGE)
        slider_page.wait_for_open()
        step = slider_page.get_slider_step()
        max_value = slider_page.get_max_value()
        min_value = slider_page.get_min_value()

        possible_values = [round(min_value + step * i, 1) for i in range(1, int((max_value - min_value) / step))]

        target_value = random.choice(possible_values)
        slider_page.set_slider_value(target_value)

        slider_value = slider_page.get_slider_value()
        displayed_value = slider_page.get_displayed_value()

        Logger.info(f"Установленное значение: {slider_value}")
        Logger.info(f"Отображаемое значение: {displayed_value}")

        assert slider_value == displayed_value, \
            f"Ожидалось значение: {slider_value}\n" \
            f"Отображается: {displayed_value}"

        Logger.info("Тест Horizontal Slider завершен успешно")
