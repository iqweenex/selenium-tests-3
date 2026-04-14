from selenium.webdriver.common.by import By


class AlertsLocators:
    BUTTON_JS_ALERT = "//button[contains(@onclick, 'jsAlert()')]"
    BUTTON_JS_CONFIRM = "//button[contains(@onclick, 'jsConfirm')]"
    BUTTON_JS_PROMPT = "//button[contains(@onclick, 'jsPrompt')]"

    RESULT_TEXT = "result"
