import pytest
from pages.auth_page import AuthPage
from utils.logger import Logger


def test_basic_auth_success(browser):
    auth_page = AuthPage(browser)

    Logger.info("Начало теста: Basic Auth")

    auth_page.open_with_auth("admin", "admin")

    expected_text = "Congratulations! You must have the proper credentials."
    actual_text = auth_page.get_success_message()

    Logger.info(f"Проверка текста"
                f"Ожидаемый: {expected_text}\n"
                f"Полученный: {actual_text}")

    assert expected_text in actual_text, f"Ожидался текст: {expected_text}\n" \
                                         f"Получен текст: {actual_text}"

    Logger.info("Basic auth test завершен успешно!")

