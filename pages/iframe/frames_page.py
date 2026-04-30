from pages.base_page import BasePage
from elements.label import Label
from elements.web_element import WebElement
from utils.logger import Logger


class FramesPage(BasePage):
    UNIQUE_ELEMENT_LOC = "//div[@id='framesWrapper']//h1[text()='Frames']"

    FRAME1_LOC = "frame1"
    FRAME2_LOC = "frame2"
    FRAME_TEXT_LOC = "sampleHeading"

    def __init__(self, browser):
        super().__init__(browser)
        self.page_name = "Frames Page"
        self.unique_element = Label(browser, self.UNIQUE_ELEMENT_LOC, "Заголовок Frames")

        self.frame1 = WebElement(browser, self.FRAME1_LOC, "Frame1")
        self.frame2 = WebElement(browser, self.FRAME2_LOC, "Frame2")
        self.frame_text = Label(browser, self.FRAME_TEXT_LOC, "Текст внутри фрейма")

    def get_frame1_text(self) -> str:
        Logger.info(f"{self}: получение текста из frame1")

        self.browser.driver.switch_to.default_content()
        self.browser.switch_to_frame(self.frame1)

        text = self.frame_text.get_text()
        self.browser.driver.switch_to.default_content()
        return text

    def get_frame2_text(self) -> str:
        Logger.info(f"{self}: получение текста из frame2")

        self.browser.driver.switch_to.default_content()
        self.browser.switch_to_frame(self.frame2)

        text = self.frame_text.get_text()
        self.browser.driver.switch_to.default_content()
        return text
