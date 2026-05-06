from pages.base_page import BasePage
from elements.label import Label


class AuthPage(BasePage):
    UNIQUE_ELEMENT_LOC = "//*[@id='content']//p"
    SUCCESS_MESSAGE = "//*[@id='content']//p"

    def __init__(self, browser):
        super().__init__(browser)
        self.page_name = "basic Auth page"
        self.success_message = Label(browser, self.SUCCESS_MESSAGE, "Сообщение об успшеной авторизации")
        self.unique_element = Label(browser, self.SUCCESS_MESSAGE, "Сообщение об успшеной авторизации")

    def get_success_message(self) -> str:
        return self.success_message.get_text()
