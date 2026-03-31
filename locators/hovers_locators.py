from selenium.webdriver.common.by import By


class HoversLocators:
    AVATARS = (By.XPATH, "//*[@class='figure']")
    USER_NAME = (By.XPATH, "//*[@class='figcaption']/h5")
    PROFILE_LINK = (By.XPATH, "//*[@class='figcaption']/a")
    
