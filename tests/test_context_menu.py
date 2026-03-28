from pages.context_menu_page import ContextMenuPage
from utils.logger import Logger


class TestContextMenu:
    def test_context_menu_alert(self, driver):
        expected_alert_text = "You selected a context menu"

        context_page = ContextMenuPage(driver)
        Logger.info("Тест Context Menu")

        context_page.open()
        context_page.right_click_on_hot_spot()

        alert_text = context_page.get_alert_text()
        Logger.info(f"Текст алерта: {alert_text}")
        assert alert_text == expected_alert_text, \
            f"Ожидался текст: {expected_alert_text}\n" \
            f"Полученный текст: '{alert_text}'"

        context_page.accept_alert()
        Logger.info("Алерт закрыт")
        Logger.info("Тест Context Menu пройден успешно")