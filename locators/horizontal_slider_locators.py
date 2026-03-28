from selenium.webdriver.common.by import By


class HorizontalSliderLocators:
    SLIDER = (By.XPATH, "//input[@type='range']")
    SLIDER_VALUE = (By.ID, "range")
