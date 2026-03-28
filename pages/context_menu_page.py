from selenium.webdriver import ActionChains
from pages.base_page import BasePage
from locators.context_menu_locators import ContextMenuLocators
from utils.logger import Logger


class ContextMenuPage(BasePage):
    def open(self):
        self.open_url("/context_menu")
        Logger.info("Страница context_menu открыта")

    def right_click_on_hot_spot(self):
        element = self.find_element(ContextMenuLocators.CONTEXT_AREA, "Выделенная область")
        actions = ActionChains(self.driver)
        actions.context_click(element.web_element).perform()
        Logger.info("Выполнен клик правой кнопкой мыши на выделенной области")

    def get_alert_text(self) -> str:
        alert = self.driver.switch_to.alert
        text = alert.text
        Logger.debug(f"Текст алерта: '{text}'")
        return text

    def accept_alert(self):
        alert = self.driver.switch_to.alert
        alert.accept()
        Logger.info("Алерт подтвержден (OK)")