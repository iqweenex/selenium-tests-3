from locators.auth_locators import AuthLocators
from pages.base_page import BasePage
from utils.logger import Logger


class AuthPage(BasePage):
    def login_with_basic_auth(self, username: str, password: str) -> None:
        auth_url = f"http://{username}:{password}@the-internet.herokuapp.com/basic_auth"

        Logger.info(f"Выполнение Basic Auth для пользователя: {username}")
        Logger.debug(
            f"Полный URL для авторизации (пароль скрыт): http://{username}:****@the-internet.herokuapp.com/basic_auth")

        self.driver.get(auth_url)

    def get_success_message(self) -> str:
        element = self.find_element(AuthLocators.SUCCESS_MESSAGE, "Сообщение об успешной авторизации")
        return element.get_text()
