from pages.context_menu_page import ContextMenuPage
from utils.logger import Logger

class TestContextMenu:
    def test_context_menu_alert(self, browser):
        expected_alert_text = "You selected a context menu"

        context_page = ContextMenuPage(browser)
        Logger.info(f"Тест Context Menu")

        context_page.open()
        context_page.right_click_on_hot_spot()

        alert_text = context_page.get_alert_text()
        assert alert_text == expected_alert_text, f"Ожидался текст: {expected_alert_text}\n" \
                                                  f"Получен текст: {alert_text}"

        context_page.accept_alert()
        Logger.info("Тест context menu завершен успешно")