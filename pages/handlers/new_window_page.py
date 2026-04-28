from pages.base_page import BasePage
from elements.label import Label


class NewWindowPage(BasePage):
    UNIQUE_ELEMENT_LOC = "//div//h3"

    def __init__(self, browser):
        super().__init__(browser)
        self.page_name = "New Window Page"
        self.unique_element = Label(browser, self.UNIQUE_ELEMENT_LOC, "Заголовок новой вкладки")
        self.title_new_window = Label(browser, self.UNIQUE_ELEMENT_LOC, "Заголовок новой вкладки")

    def get_page_text(self) -> str:
        return self.title_new_window.get_text()
