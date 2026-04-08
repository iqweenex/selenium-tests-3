from pages.horizontal_slider_page import HorizontalSliderPage
from utils.logger import Logger


class TestHorizontalSlider:
    def test_horizontal_slider_random_value(self, browser):
        slider_page = HorizontalSliderPage(browser)
        Logger.info("Тест Horizontal Slider")

        slider_page.open()
        slider_page.set_slider_value()

        slider_value = slider_page.get_slider_value()
        displayed_value = slider_page.get_displayed_value()

        Logger.info(f"Установленное значение: {slider_value}")
        Logger.info(f"Отображаемое значение: {displayed_value}")

        assert slider_value == displayed_value, \
            f"Ожидалось значение: {slider_value}\n" \
            f"Отображается: {displayed_value}"

        Logger.info("Тест Horizontal Slider завершен успешно")
