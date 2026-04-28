from pages.base_page import BasePage
from elements.web_element import WebElement
from utils.logger import Logger


class AlertsFrameWindowsPage(BasePage):
    UNIQUE_ELEMENT_LOC = "//div[contains(text(), 'Please select an item')]"

    MENU_HEADER = "//span//div[contains(text(), 'Alerts, Frame & Windows')]"
    MENU_CONTAINER = "//span[.//div[contains(text(), 'Alerts, Frame & Windows')]]" \
                     "/following-sibling::div[contains(@class, 'element-list')]"
    NESTED_FRAMES_MENU = "//span[text()='Nested Frames']"
    FRAMES_MENU = "//span[text()='Frames']"

    def __init__(self, browser):
        super().__init__(browser)
        self.page_name = "Alerts Frame Windows Page"
        self.unique_element = WebElement(browser, self.UNIQUE_ELEMENT_LOC, "Плейсхолдер Please select an item")
        self.menu_header = WebElement(browser, self.MENU_HEADER, "Заголовок меню")
        self.menu_container = WebElement(browser, self.MENU_CONTAINER, "Контейнер меню")
        self.nested_frames_menu = WebElement(browser, self.NESTED_FRAMES_MENU, "Пункт Nested Frames")
        self.frames_menu = WebElement(browser, self.FRAMES_MENU, "Пункт Frames")

    def ensure_menu_open(self):
        Logger.info(f"Открываем боковое меню Alerts, Frame & Windows, если не открыто")
        class_attribute = self.menu_container.get_attribute("class")
        if "collapse" in class_attribute and "show" not in class_attribute:
            Logger.info(f"{self}: меню закрыто, открываем")
            self.menu_header.click()
        else:
            Logger.info(f"{self}: меню уже открыто")
