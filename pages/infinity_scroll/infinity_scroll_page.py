from pages.base_page import BasePage
from elements.label import Label
from elements.multi_web_element import MultiWebElement
from elements.web_element import WebElement
from utils.logger import Logger


class InfinityScrolPage(BasePage):
    UNIQUE_ELEMENT_LOC = "//*[@id='content']//h3"
    PARAGRAPHS = "(//div[contains(@class, 'add')])[{}]"

    def __init__(self, browser):
        super().__init__(browser)
        self.page_name = "Infinity scroll page"
        self.unique_element = Label(browser, self.UNIQUE_ELEMENT_LOC, "Заголовок")
        self.paragraphs = MultiWebElement(browser, self.PARAGRAPHS, "Абзацы", timeout=3)

    def get_paragraphs_count(self) -> int:
        Logger.info(f"{self}: получение количества абзацев")
        count = len(self.paragraphs)
        Logger.info(f"Получено {count} абзацев")
        return count
