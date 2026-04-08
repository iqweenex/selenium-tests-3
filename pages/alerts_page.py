from pages.base_page import BasePage
from locators.alerts_locators import AlertsLocators
from utils.logger import Logger
from elements.label import Label
from elements.button import Button


class AlertsPage(BasePage):
    UNIQUE_ELEMENT_LOC = AlertsLocators.RESULT_TEXT

    def __init__(self, browser):
        super().__init__(browser)
        self.unique_element = Label(browser, self.UNIQUE_ELEMENT_LOC, "Текст результата")
        self.page_name = "Alerts page"
        self.btn_js_alert = Button(browser, AlertsLocators.BUTTON_JS_ALERT, "Кнопка JS Alert")
        self.btn_js_confirm = Button(browser, AlertsLocators.BUTTON_JS_CONFIRM, "Кнопка JS Confirm")
        self.btn_js_prompt = Button(browser, AlertsLocators.BUTTON_JS_PROMPT, "Кнопка JS Prompt")

    def open(self):
        self.browser.get("https://the-internet.herokuapp.com/javascript_alerts")
        self.wait_for_open()
        Logger.info(f"{self.page_name} страница открыта")
        return self

    def click_js_alert_button(self):
        self.btn_js_alert.click()
        Logger.info(f"{self}: кнопка JS Alert нажата")
        return self

    def click_js_confirm_button(self):
        self.btn_js_confirm.click()
        Logger.info(f"{self}: кнопка JS Confirm нажата")
        return self

    def click_js_prompt_button(self):
        self.btn_js_prompt.click()
        Logger.info(f"{self}: кнопка JS Prompt нажата")
        return self

    def trigger_js_alert_via_js(self):
        Logger.info("Вызов JS Alert через JavaScript")
        self.browser.execute_script("alert('I am a JS Alert');")
        return self

    def trigger_js_confirm_via_js(self):
        Logger.info("Вызов JS Confirm через JavaScript")
        self.browser.execute_script("confirm('I am a JS Confirm');")
        return self

    def trigger_js_prompt_via_js(self):
        Logger.info("Вызов JS Prompt через JavaScript")
        self.browser.execute_script("prompt('I am a JS Prompt');")
        return self

    def get_alert_text(self) -> str:
        return self.browser.get_alert_text()

    def accept_alert(self):
        self.browser.accept_alert()
        Logger.info("Алерт подтвержден")
        return self

    def dismiss_alert(self):
        alert = self.browser.switch_to_alert()
        alert.dismiss()
        Logger.info("Алерт отклонен")
        return self

    def send_text_for_prompt(self, text: str):
        self.browser.send_keys_alert(text)
        Logger.info(f"В алерт введен текст: {text}")
        return self

    def get_result_text(self) -> str:
        return self.unique_element.get_text()

