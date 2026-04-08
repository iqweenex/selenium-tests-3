from selenium.webdriver.common.by import By


class HoversLocators:
    AVATARS_XPATH = "(//div[@class='figure'])[{}]"
    AVATARS = (By.XPATH, "//div[@class='figure']")
    USER_NAME = (By.XPATH, ".//div[@class='figcaption']/h5")
    PROFILE_LINK = (By.XPATH, ".//div[@class='figcaption']/a")
    
