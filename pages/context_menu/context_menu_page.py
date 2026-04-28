from selenium.webdriver import ActionChains
from pages.base_page import BasePage
from utils.logger import Logger
from elements.web_element import WebElement


class ContextMenuPage(BasePage):
    UNIQUE_ELEMENT_LOC = "content"
    CONTEXT_AREA_LOCATOR = "content"
    HOT_SPOT = "hot-spot"

    def __init__(self, browser):
        super().__init__(browser)
        self.page_name = "Context menu page"
        self.unique_element = WebElement(browser, self.UNIQUE_ELEMENT_LOC, "Выделенная область")
        self.hot_spot = WebElement(browser, self.HOT_SPOT, "Hot spot")

    def right_click_on_hot_spot(self):
        element = self.hot_spot.wait_for_visible()
        actions = ActionChains(self.browser.driver)
        Logger.info(f"{self}: правый клик по выделенной области")
        actions.context_click(element).perform()
