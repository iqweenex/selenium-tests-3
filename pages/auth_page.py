from locators.auth_locators import AuthLocators
from pages.base_page import BasePage
from utils.logger import Logger
from elements.label import Label


class AuthPage(BasePage):
    UNIQUE_ELEMENT_LOC = AuthLocators.SUCCESS_MESSAGE

    def __init__(self, browser):
        super().__init__(browser)
        self.page_name = "basic Auth page"
        self.success_message = Label(browser, self.UNIQUE_ELEMENT_LOC, "Сообщение об успшеной авторизации")

    def open_with_auth(self, username: str, password: str):
        auth_url = f"http://{username}:{password}@the-internet.herokuapp.com/basic_auth"

        Logger.info(f"Выполнение Basic Auth для пользователя: {username}")
        Logger.debug(
            f"Полный URL для авторизации (пароль скрыт): http://{username}:****@the-internet.herokuapp.com/basic_auth")

        self.browser.get(auth_url)
        self.success_message.wait_for_visible()

        Logger.info(f"{self}: {self.page_name}: открыта с авторизацией")
        return self

    def get_success_message(self) -> str:
        return self.success_message.get_text()
