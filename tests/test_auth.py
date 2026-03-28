import pytest
from pages.auth_page import AuthPage
from utils.logger import Logger


def test_basic_auth_success(driver):
    auth_page = AuthPage(driver)

    Logger.info("Начало теста: Basic Auth")
    auth_page.login_with_basic_auth("admin", "admin")

    expected_text = "Congratulations! You must have the proper credentials."
    actual_text = auth_page.get_success_message()

    Logger.info(f"Проверка текста. Ожидаем: '{expected_text}'")
    assert expected_text in actual_text
    Logger.info("Тест Basic Auth успешно пройден!")
