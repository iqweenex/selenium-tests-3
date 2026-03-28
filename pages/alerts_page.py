from pages.base_page import BasePage
from locators.alerts_locators import AlertsLocators
from utils.logger import Logger


class AlertsPage(BasePage):
    def open(self):
        self.open_url("/javascript_alerts")

    def click_js_alert_button(self):
        button = self.find_element(AlertsLocators.BUTTON_JS_ALERT, "кнопка jsAlert")
        button.click()
        Logger.info("Нажата кнопка jasAlert")

    def click_js_confirm_button(self):
        button = self.find_element(AlertsLocators.BUTTON_JS_CONFIRM, "кнопка jsConfirm")
        button.click()
        Logger.info("Нажата кнопка jsConfirm")

    def click_js_prompt_button(self):
        button = self.find_element(AlertsLocators.BUTTON_JS_PROMPT, "кнопка jsPrompt")
        button.click()
        Logger.info("Нажата кнопка jsPrompt")

    def trigger_js_alert_via_js(self):
        Logger.info("Вызов JS Alert через JavaScript")
        self.driver.execute_script("alert('I am a JS Alert');")

    def trigger_js_confirm_via_js(self):
        Logger.info("Вызов JS Confirm через JavaScript")
        self.driver.execute_script("confirm('I am a JS Confirm');")

    def trigger_js_prompt_via_js(self):
        Logger.info("Вызов JS Prompt через JavaScript")
        self.driver.execute_script("prompt('I am a JS Prompt');")

    def get_alert_text(self) -> str:
        alert = self.driver.switch_to.alert
        text = alert.text
        Logger.info(f"Текст алерта: {text}")
        return text

    def accept_alert(self):
        alert = self.driver.switch_to.alert
        alert.accept()
        Logger.info("Алерт подтвержден")

    def dismiss_alert(self):
        alert = self.driver.switch_to.alert
        alert.dismiss()
        Logger.info("Алерт отклонен")

    def send_text_for_prompt(self, text: str):
        alert = self.driver.switch_to.alert
        alert.send_keys(text)
        Logger.info(f"В алерт введен текст: {text}")

    def get_result_text(self) -> str:
        res = self.find_element(AlertsLocators.RESULT_TEXT, "Текст результата")
        return res.get_text()
