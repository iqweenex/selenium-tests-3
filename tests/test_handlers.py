import pytest
from pages.handlers.handlers_page import HandlersPage
from pages.handlers.new_window_page import NewWindowPage
from utils.logger import Logger
from utils.window_manager import WindowManager


class TestHandlers:
    """
    Добавил возможность открытия N страниц
    Количество страниц указывается в параметризации теста
    """
    URL_HANDLERS = "http://the-internet.herokuapp.com/windows"

    @pytest.mark.parametrize("windows_count", [1, 2, 3])
    def test_handlers_multiple_windows(self, browser, windows_count):
        handlers_page = HandlersPage(browser)
        window_manager = WindowManager(browser)

        Logger.info(f"Тест Handlers: открытие {windows_count} вкладок")

        browser.get(self.URL_HANDLERS)
        handlers_page.wait_for_open()
        window_manager.save_main_handle()
        expected_page_text = "New Window"
        expected_title = "New Window"

        for i in range(windows_count):
            Logger.info(f"Открытие вкладки {i + 1}")

            window_manager.open_new_window_and_switch(
                action=handlers_page.click_link
            )

            new_window_page = NewWindowPage(browser)
            actual_page_text = new_window_page.get_page_text()
            actual_title = browser.driver.title
            assert actual_page_text == expected_page_text, f"Ожидалось {expected_page_text}\n" \
                                                           f"Получено {actual_page_text}"

            assert actual_title == expected_title, f"Ожидалось {expected_title}\n" \
                                                   f"Получено {actual_title}"

            window_manager.switch_to_main()

        window_manager.close_all_opened_windows()

        Logger.info(f"Тест Handlers с {windows_count} вкладками завершен успешно")