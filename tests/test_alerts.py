import pytest
from pages.alerts_page import AlertsPage
from utils.logger import Logger
from faker import Faker


class TestAlerts:

    def test_js_alert(self, browser):
        expected_alert_text = "I am a JS Alert"
        expected_result_text = "You successfully clicked an alert"

        alerts_page = AlertsPage(browser)
        Logger.info("Тест JS Alert")

        alerts_page.open()
        alerts_page.click_js_alert_button()

        alert_text = alerts_page.get_alert_text()
        assert alert_text == expected_alert_text

        alerts_page.accept_alert()

        result_text = alerts_page.get_result_text()
        assert result_text == expected_result_text

        Logger.info("Тест JS Alert завершен успешно")

    def test_js_confirm_ok(self, browser):
        expected_alert_text = "I am a JS Confirm"
        expected_result_text = "You clicked: Ok"

        alerts_page = AlertsPage(browser)
        Logger.info("Тест JS Confirm")

        alerts_page.open()
        alerts_page.click_js_confirm_button()

        alert_text = alerts_page.get_alert_text()
        assert alert_text == expected_alert_text

        alerts_page.accept_alert()

        result_text = alerts_page.get_result_text()
        assert result_text == expected_result_text

        Logger.info("Тест JS Confirm завершен успешно")

    def test_js_prompt(self, browser):
        faker = Faker()
        random_text = faker.text(30)
        expected_alert_text = "I am a JS prompt"
        expected_result_text = f"You entered: {random_text}"

        alerts_page = AlertsPage(browser)
        Logger.info("Тест JS Prompt")

        alerts_page.open()
        alerts_page.click_js_prompt_button()

        alert_text = alerts_page.get_alert_text()
        assert alert_text == expected_alert_text

        alerts_page.send_text_for_prompt(random_text)
        alerts_page.accept_alert()

        result_text = alerts_page.get_result_text()
        assert result_text == expected_result_text

        Logger.info("Тест JS Prompt завершен успешно")

    def test_js_alert_via_js(self, browser):
        expected_alert_text = "I am a JS Alert"

        alerts_page = AlertsPage(browser)
        Logger.info("Тест JS Alert через JavaScript")

        alerts_page.open()
        alerts_page.trigger_js_alert_via_js()

        alert_text = alerts_page.get_alert_text()
        assert alert_text == expected_alert_text

        alerts_page.accept_alert()

        Logger.info("Тест JS Alert (через JavaScript) завершен успешно")

    def test_js_confirm_via_js(self, browser):
        expected_alert_text = "I am a JS Confirm"

        alerts_page = AlertsPage(browser)
        Logger.info("Тест JS Confirm через JavaScript")

        alerts_page.open()
        alerts_page.trigger_js_confirm_via_js()

        alert_text = alerts_page.get_alert_text()
        assert alert_text == expected_alert_text

        alerts_page.accept_alert()

        Logger.info("Тест JS Confirm (через JavaScript) завершен успешно")

    def test_js_prompt_via_js(self, browser):
        fake = Faker()
        random_text = fake.text(30)
        expected_alert_text = "I am a JS Prompt"

        alerts_page = AlertsPage(browser)
        Logger.info("Тест JS Prompt через JavaScript")

        alerts_page.open()
        alerts_page.trigger_js_prompt_via_js()

        alert_text = alerts_page.get_alert_text()
        assert alert_text == expected_alert_text

        alerts_page.send_text_for_prompt(random_text)
        alerts_page.accept_alert()

        Logger.info("Тест JS Prompt (через JavaScript) завершен успешно")
