from pages.base_page import BasePage
from elements.button import Button
from utils.logger import Logger


class DemoqaMainPage(BasePage):
    UNIQUE_ELEMENT_LOC = "//div[contains(@class, 'category-cards')]"
    ALERTS_FRAME_WINDOWS_CARD = "//div[contains(@class, 'home-body')]//a[contains(@href, 'alerts')]"

    def __init__(self, browser):
        super().__init__(browser)
        self.page_name = "Demoqa Main Page"
        self.unique_element = Button(browser, self.UNIQUE_ELEMENT_LOC, "Карточки категорий")
        self.alerts_card = Button(browser, self.ALERTS_FRAME_WINDOWS_CARD, "Карточка Alerts, Frame & Windows")

    def click_alerts_frame_windows_card(self):
        Logger.info(f"{self}: клик по карточке Alerts, Frame & Windows")
        self.alerts_card.click()
