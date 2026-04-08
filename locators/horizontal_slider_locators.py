from selenium.webdriver.common.by import By


class HorizontalSliderLocators:
    CONTENT_AREA = (By.ID, "content")
    SLIDER = (By.XPATH, "//input[@type='range']")
    SLIDER_VALUE = (By.XPATH, "//div[@id='content']//span[@id='range']")
