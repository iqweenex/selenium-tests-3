from pages.base_page import BasePage
from utils.logger import Logger
from selenium.webdriver import ActionChains
from elements.web_element import WebElement
from elements.label import Label


class HandlersPage(BasePage):
    UNIQUE_ELEMENT_LOC = "//*[@id='content']//a[contains(@href, 'new')]"
    CLICK_HERE_BUTTON_LOCATOR = "//*[@id='content']//a[contains(@href, 'new')]"

    def __init__(self, browser):
        super().__init__(browser)
        self.page_name = "Handlers page"
        self.unique_element = WebElement(browser, self.UNIQUE_ELEMENT_LOC, "Ссылка нажми сюда")
        self.click_here_btn = WebElement(browser, self.CLICK_HERE_BUTTON_LOCATOR, "Click here button")

    def click_link(self):
        Logger.info(f"{self}: click on button")
        self.click_here_btn.click()
