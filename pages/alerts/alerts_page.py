from pages.base_page import BasePage
from elements.label import Label
from elements.button import Button


class AlertsPage(BasePage):
    UNIQUE_ELEMENT_LOC = "result"
    BUTTON_JS_ALERT = "//button[contains(@onclick, 'jsAlert()')]"
    BUTTON_JS_CONFIRM = "//button[contains(@onclick, 'jsConfirm')]"
    BUTTON_JS_PROMPT = "//button[contains(@onclick, 'jsPrompt')]"

    RESULT_TEXT = "result"

    def __init__(self, browser):
        super().__init__(browser)
        self.unique_element = Label(browser, self.UNIQUE_ELEMENT_LOC, "Текст результата")
        self.page_name = "Alerts page"
        self.result_text_element = Label(browser, self.RESULT_TEXT, "Текст результата")
        self.btn_js_alert = Button(browser, self.BUTTON_JS_ALERT, "Кнопка JS Alert")
        self.btn_js_confirm = Button(browser, self.BUTTON_JS_CONFIRM, "Кнопка JS Confirm")
        self.btn_js_prompt = Button(browser, self.BUTTON_JS_PROMPT, "Кнопка JS Prompt")

    def click_js_alert_button(self):
        self.btn_js_alert.click()

    def click_js_confirm_button(self):
        self.btn_js_confirm.click()

    def click_js_prompt_button(self):
        self.btn_js_prompt.click()

    def get_result_text(self) -> str:
        return self.result_text_element.get_text()
