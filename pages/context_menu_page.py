from selenium.webdriver import ActionChains
from pages.base_page import BasePage
from locators.context_menu_locators import ContextMenuLocators
from utils.logger import Logger
from elements.web_element import WebElement


class ContextMenuPage(BasePage):
    UNIQUE_ELEMENT_LOC = ContextMenuLocators.CONTEXT_AREA

    def __init__(self, browser):
        super().__init__(browser)
        self.page_name = "Context menu page"
        self.unique_element = WebElement(browser, self.UNIQUE_ELEMENT_LOC, "Выделенная область")
        self.hot_spot = WebElement(browser, ContextMenuLocators.HOT_SPOT, "Hot spot")

    def open(self):
        self.browser.get("https://the-internet.herokuapp.com/context_menu")
        self.wait_for_open()
        Logger.info(f"{self}: {self.page_name} открыта")
        return self

    def right_click_on_hot_spot(self):
        element = self.hot_spot.wait_for_visible()
        actions = ActionChains(self.browser.driver)
        actions.context_click(element).perform()
        Logger.info(f"{self}: правый клик по выделенной области")
        return self

    def get_alert_text(self) -> str:
        return self.browser.get_alert_text()

    def accept_alert(self):
        self.browser.accept_alert()
        return self
