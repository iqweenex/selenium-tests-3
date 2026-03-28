import pytest
from pages.alerts_page import AlertsPage
from utils.logger import Logger
from faker import Faker


class TestAlerts:

    def test_js_alert(self, driver):
        expected_alert_text = "I am a JS Alert"
        expected_result_text = "You successfully clicked an alert"
        alerts_page = AlertsPage(driver)
        Logger.info("Тест js alerts")

        alerts_page.open()
        Logger.info("Открыли страницу алерт")

        alerts_page.click_js_alert_button()

        alert_text = alerts_page.get_alert_text()
        assert alert_text == expected_alert_text, f"Ожидался текст: {expected_alert_text}\n" \
                                                  f"Получен текст: {alert_text}"

        alerts_page.accept_alert()

        result_text = alerts_page.get_result_text()
        assert result_text == expected_result_text, f"Ожидаемы текст результата: {expected_result_text}\n" \
                                                    f"Полученный текст результата: {result_text}"

        Logger.info("Тест js Alert завершен успешно")

    def test_js_confirm_ok(self, driver):
        expected_alert_text = "I am a JS Confirm"
        expected_result_text = "You clicked: Ok"

        alerts_page = AlertsPage(driver)
        Logger.info("Тест js confirm")

        alerts_page.open()
        Logger.info("Открыли страницу алерт")

        alerts_page.click_js_confirm_button()

        alert_text = alerts_page.get_alert_text()
        assert alert_text == expected_alert_text, f"Ожидался текст: {expected_alert_text}\n" \
                                                  f"Получен текст: {alert_text}"

        alerts_page.accept_alert()

        result_text = alerts_page.get_result_text()
        assert result_text == expected_result_text, f"Ожидаемы текст результата: {expected_result_text}\n" \
                                                    f"Полученный текст результата: {result_text}"

        Logger.info("Тест js Confirm завершен успешно")

    def test_js_prompt(self, driver):
        faker = Faker()
        random_text = faker.text(30)
        expected_alert_text = "I am a JS prompt"
        expected_result_text = f"You entered: {random_text}"

        alerts_page = AlertsPage(driver)
        Logger.info("Тест js prompt")

        alerts_page.open()
        Logger.info("Открыли страницу алерт")

        alerts_page.click_js_prompt_button()

        alert_text = alerts_page.get_alert_text()
        assert alert_text == expected_alert_text, f"Ожидался текст: {expected_alert_text}\n" \
                                                  f"Получен текст: {alert_text}"

        alerts_page.send_text_for_prompt(random_text)
        alerts_page.accept_alert()

        result_text = alerts_page.get_result_text()
        assert result_text == expected_result_text, f"Ожидаемы текст результата: {expected_result_text}\n" \
                                                    f"Полученный текст результата: {result_text}"

        Logger.info("Тест jsPrompt завершен успешно")

    def test_js_alert_via_js(self, driver):
        """Тест #3: JS Alert через JavaScript"""
        expected_alert_text = "I am a JS Alert"
        expected_result_text = "You successfully clicked an alert"

        alerts_page = AlertsPage(driver)

        alerts_page.open()
        alerts_page.trigger_js_alert_via_js()

        alert_text = alerts_page.get_alert_text()
        assert alert_text == expected_alert_text, f"Ожидался текст: {expected_alert_text}\n" \
                                                  f"Получен текст: {alert_text}"

        alerts_page.accept_alert()

        Logger.info("Тест JS Alert (через JavaScript) завершен")

    def test_js_confirm_via_js(self, driver):
        expected_alert_text = "I am a JS Confirm"
        expected_result_text = "You clicked: Ok"

        alerts_page = AlertsPage(driver)
        Logger.info("Тест JS Confirm (через JavaScript)")

        alerts_page.open()
        alerts_page.trigger_js_confirm_via_js()

        alert_text = alerts_page.get_alert_text()
        assert alert_text == expected_alert_text, f"Ожидался текст: {expected_alert_text}\n" \
                                                  f"Получен текст: {alert_text}"

        alerts_page.accept_alert()

        Logger.info("Тест JS Confirm (через JavaScript) завершен")

    def test_js_prompt_via_js(self, driver):
        expected_alert_text = "I am a JS Prompt"

        fake = Faker()
        random_text = fake.text(30)
        expected_result_text = f"You entered: {random_text}"

        alerts_page = AlertsPage(driver)

        alerts_page.open()
        alerts_page.trigger_js_prompt_via_js()

        alert_text = alerts_page.get_alert_text()
        assert alert_text == expected_alert_text, f"Ожидался текст: {expected_alert_text}\n" \
                                                  f"Получен текст: {alert_text}"

        alerts_page.send_text_for_prompt(random_text)
        alerts_page.accept_alert()

        Logger.info("Тест JS Prompt (через JavaScript) завершен")
