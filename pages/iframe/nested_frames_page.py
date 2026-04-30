from pages.base_page import BasePage
from elements.label import Label
from elements.web_element import WebElement
from utils.logger import Logger


class NestedFramesPage(BasePage):
    UNIQUE_ELEMENT_LOC = "//*[@id='framesWrapper']//h1[contains(text(), 'Nested')]"

    PARENT_FRAME_LOC = "frame1"
    PARENT_FRAME_TEXT_LOC = "//body"
    CHILD_FRAME_LOC = "//iframe"
    CHILD_FRAME_TEXT_LOC = "//p"

    def __init__(self, browser):
        super().__init__(browser)
        self.page_name = "Nested Frames Page"
        self.unique_element = Label(browser, self.UNIQUE_ELEMENT_LOC, "Заголовок Nested Frames")
        self.parent_frame = WebElement(browser, self.PARENT_FRAME_LOC, "Parent frame")
        self.parent_frame_text = Label(browser, self.PARENT_FRAME_TEXT_LOC, "Текст parent frame")
        self.child_frame = WebElement(browser, self.CHILD_FRAME_LOC, "Child frame")
        self.child_frame_text = Label(browser, self.CHILD_FRAME_TEXT_LOC, "Текст child frame")

    def get_parent_frame_text(self) -> str:
        Logger.info(f"{self}: получение текста из parent frame")

        self.browser.driver.switch_to.default_content()
        self.browser.switch_to_frame(self.parent_frame)

        text = self.parent_frame_text.get_text()

        Logger.info(f"{self}: текст parent frame = '{text}'")
        self.browser.driver.switch_to.default_content()

        return text

    def get_child_frame_text(self) -> str:
        Logger.info(f"{self}: получение текста из child frame")

        self.browser.driver.switch_to.default_content()
        self.browser.switch_to_frame(self.parent_frame)
        self.browser.switch_to_frame(self.child_frame)

        text = self.child_frame_text.get_text()

        Logger.info(f"{self}: текст child frame = '{text}'")
        self.browser.driver.switch_to.default_content()

        return text