from selenium.webdriver.common.by import By


class AlertsLocators:
    BUTTON_JS_ALERT = (By.XPATH, "//button[contains(@onclick, 'jsAlert()')]")
    BUTTON_JS_CONFIRM = (By.XPATH, "//button[contains(@onclick, 'jsConfirm')]")
    BUTTON_JS_PROMPT = (By.XPATH, "//button[contains(@onclick, 'jsPrompt')]")

    RESULT_TEXT = (By.ID, "result")
