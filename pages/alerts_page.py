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
        self.result_text_element = Label(browser, AlertsLocators.RESULT_TEXT, "Текст результата")
        self.btn_js_alert = Button(browser, AlertsLocators.BUTTON_JS_ALERT, "Кнопка JS Alert")
        self.btn_js_confirm = Button(browser, AlertsLocators.BUTTON_JS_CONFIRM, "Кнопка JS Confirm")
        self.btn_js_prompt = Button(browser, AlertsLocators.BUTTON_JS_PROMPT, "Кнопка JS Prompt")

    def open(self, url: str):
        Logger.info(f"Открываем страницу {self.page_name}")
        self.browser.get(url)
        self.wait_for_open()

    def click_js_alert_button(self):
        Logger.info(f"Нажимаем кнопку JS Alert")
        self.btn_js_alert.click()

    def click_js_confirm_button(self):
        Logger.info(f"Нажимаем кнопку JS Confirm")
        self.btn_js_confirm.click()

    def click_js_prompt_button(self):
        Logger.info(f"Нажимаем кнопку JS Prompt")
        self.btn_js_prompt.click()

    def trigger_js_alert_via_js(self):
        Logger.info("Вызов JS Alert через JavaScript")
        self.browser.execute_script("alert('I am a JS Alert');")

    def trigger_js_confirm_via_js(self):
        Logger.info("Вызов JS Confirm через JavaScript")
        self.browser.execute_script("confirm('I am a JS Confirm');")

    def trigger_js_prompt_via_js(self):
        Logger.info("Вызов JS Prompt через JavaScript")
        self.browser.execute_script("prompt('I am a JS Prompt');")

    def get_result_text(self) -> str:
        return self.result_text_element.get_text()
