from selenium.webdriver.common.by import By


class HoversLocators:
    UNIQUE_LOCATOR = "//*[@id='content']//p"
    AVATARS_XPATH = "(//div[contains(@class, 'figure')])[{}]"
    AVATARS = "//div[contains(@class, 'figure')]"
    USER_NAME = ".//div[contains(@class, 'figcaption')]/h5"
    PROFILE_LINK = ".//div[contains(@class, 'figcaption')]/a"
    
