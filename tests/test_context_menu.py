from pages.context_menu.context_menu_page import ContextMenuPage
from utils.logger import Logger


class TestContextMenu:
    URL_CONTEXT_MENU = "http://the-internet.herokuapp.com/context_menu"

    def test_context_menu_alert(self, browser):
        expected_alert_text = "You selected a context menu"

        context_page = ContextMenuPage(browser)
        Logger.info(f"Тест Context Menu")

        Logger.info(f"Открываем {context_page.page_name}")
        browser.get(self.URL_CONTEXT_MENU)
        context_page.wait_for_open()
        context_page.right_click_on_hot_spot()

        alert_text = browser.get_alert_text()
        assert alert_text == expected_alert_text, f"Ожидался текст: {expected_alert_text}\n" \
                                                  f"Получен текст: {alert_text}"

        browser.accept_alert()
        Logger.info("Тест context menu завершен успешно")
