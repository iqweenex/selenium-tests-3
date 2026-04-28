from pages.base_page import BasePage
from elements.web_element import WebElement
from utils.logger import Logger


class DemoqaMainPage(BasePage):
    UNIQUE_ELEMENT_LOC = "//div[contains(@class, 'category-cards')]"
    ALERTS_FRAME_WINDOWS_CARD = "//div[contains(@class, 'home-body')]//a[contains(@href, 'alerts')]"

    def __init__(self, browser):
        super().__init__(browser)
        self.page_name = "Demoqa Main Page"
        self.unique_element = WebElement(browser, self.UNIQUE_ELEMENT_LOC, "Карточки категорий")
        self.alerts_card = WebElement(browser, self.ALERTS_FRAME_WINDOWS_CARD, "Карточка Alerts, Frame & Windows")
