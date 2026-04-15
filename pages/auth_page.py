from locators.auth_locators import AuthLocators
from pages.base_page import BasePage
from utils.logger import Logger
from elements.label import Label


class AuthPage(BasePage):
    UNIQUE_ELEMENT_LOC = "//*[@id='content']//p"
    SUCCESS_MESSAGE = "//*[@id='content']//p"

    def __init__(self, browser):
        super().__init__(browser)
        self.page_name = "basic Auth page"
        self.success_message = Label(browser, self.SUCCESS_MESSAGE, "Сообщение об успшеной авторизации")

    def open_with_auth(self, url: str, username: str, password: str):
        auth_url = f"https://{username}:{password}@{url}"

        Logger.info(f"Выполнение Basic Auth для пользователя: {username}")
        Logger.debug(
            f"Полный URL для авторизации (пароль скрыт): http://{username}:****@{url}")

        self.browser.get(auth_url)
        self.success_message.wait_for_visible()

    def get_success_message(self) -> str:
        return self.success_message.get_text()
