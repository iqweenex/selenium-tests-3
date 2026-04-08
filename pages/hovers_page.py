from selenium.webdriver import ActionChains
from elements.web_element import WebElement
from pages.base_page import BasePage
from locators.hovers_locators import HoversLocators
from utils.logger import Logger
from elements.multi_web_element import MultiWebElement


class HoversPage(BasePage):
    UNIQUE_ELEMENT_LOC = HoversLocators.AVATARS

    def __init__(self, browser):
        super().__init__(browser)
        self.page_name = "Hovers page"
        self.avatars = MultiWebElement(browser, HoversLocators.AVATARS_XPATH, "Аватары")
        self.unique_element = WebElement(browser, self.UNIQUE_ELEMENT_LOC, "Аватары")

    def open(self):
        self.browser.get("https://the-internet.herokuapp.com/hovers")
        self.wait_for_open()
        Logger.info(f"{self.page_name} открыта")
        return self

    def get_avatars_count(self) -> int:
        count = self.avatars.count()
        Logger.info(f"Найдено {count} аватаров")
        return count

    def hover_over_avatar(self, avatar_index: int):
        avatar = self.avatars.get_by_index(avatar_index + 1)
        avatar.wait_for_presence()

        self.browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", avatar.wait_for_presence())

        actions = ActionChains(self.browser.driver)
        actions.move_to_element(avatar.wait_for_presence()).perform()

        Logger.info(f"Курсор наведен на аватар {avatar_index + 1}")
        return avatar

    def get_user_name(self, avatar_index: int) -> str:
        self.hover_over_avatar(avatar_index)
        name_xpath = f"(//div[@class='figure'])[{avatar_index + 1}]//div[@class='figcaption']/h5"
        name_element = WebElement(self.browser, name_xpath, f"Имя аватара {avatar_index + 1}")
        name = name_element.get_text()
        Logger.info(f"Имя аватара {avatar_index + 1}: {name}")
        return name

    def click_view_profile(self, avatar_index: int):
        self.hover_over_avatar(avatar_index)
        profile_xpath = f"(//div[@class='figure'])[{avatar_index + 1}]//div[@class='figcaption']/a"
        profile_link = WebElement(self.browser, profile_xpath, f"Ссылка профиля {avatar_index + 1}")
        profile_link.click()
        Logger.info(f"Нажата ссылка аватара {avatar_index + 1}")
        return self

    def go_back(self):
        self.browser.driver.back()
        self.wait_for_open()
        self.avatars = MultiWebElement(self.browser, HoversLocators.AVATARS_XPATH, "Аватары")
        Logger.info("Вернулись на страницу Hovers")
        return self
