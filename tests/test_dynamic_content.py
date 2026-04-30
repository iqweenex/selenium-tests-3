from pages.dynamic_content.dynamic_content_page import DynamicContentPage
from utils.logger import Logger


class TestDynamicContent:
    URL = "http://the-internet.herokuapp.com/dynamic_content"
    MAX_REFRESH_ATTEMPTS = 20

    def test_dynamic_content(self, browser):
        Logger.info("Тест: Dynamic Content")

        dynamic_page = DynamicContentPage(browser)

        attempt = 0
        while attempt < self.MAX_REFRESH_ATTEMPTS:
            if attempt == 0:
                browser.get(self.URL)
            else:
                browser.refresh()

            dynamic_page.wait_for_open()

            if dynamic_page.has_duplicate_images():
                Logger.info(f"Найдены дубликаты изображений на попытке {attempt + 1}")
                break

            attempt += 1
        else:
            raise AssertionError(f"После {self.MAX_REFRESH_ATTEMPTS} "
                                 f"обновлений не найдено двух одинаковых изображений")

        Logger.info("Тест Dynamic Content успешно пройден")