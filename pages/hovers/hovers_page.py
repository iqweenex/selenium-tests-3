from selenium.webdriver import ActionChains
from elements.web_element import WebElement
from pages.base_page import BasePage
from utils.logger import Logger
from elements.multi_web_element import MultiWebElement


class HoversPage(BasePage):
    UNIQUE_ELEMENT_LOC = "//*[@id='content']//p"
    AVATARS_XPATH = "(//div[contains(@class, 'figure')])[{}]"
    _USER_NAME_XPATH = "(//div[contains(@class, 'figure')])[{}]//div[contains(@class, 'figcaption')]/h5"
    _PROFILE_LINK_XPATH = "(//div[contains(@class, 'figure')])[{}]//div[contains(@class, 'figcaption')]/a"

    def __init__(self, browser):
        super().__init__(browser)
        self.page_name = "Hovers page"
        self.avatars = MultiWebElement(browser, self.AVATARS_XPATH, "Аватары", timeout=3)
        self.unique_element = WebElement(browser, self.UNIQUE_ELEMENT_LOC, "Аватары")

    def get_avatars_count(self) -> int:
        count = len(self.avatars)
        Logger.info(f"Найдено {count} аватаров")
        return count

    def hover_over_avatar(self, avatar_index: int):
        avatar = self.avatars.get_by_index(avatar_index + 1)
        avatar.scroll_to_view()
        actions = ActionChains(self.browser.driver)
        Logger.info(f"Наводим курсор на аватар {avatar_index + 1}")
        actions.move_to_element(avatar.wait_for_visible()).perform()
        return avatar

    def get_user_name(self, avatar_index: int) -> str:
        self.hover_over_avatar(avatar_index)
        name_xpath = self._USER_NAME_XPATH.format(avatar_index + 1)
        name_element = WebElement(self.browser, name_xpath, f"Имя аватара {avatar_index + 1}")
        name = name_element.get_text()
        Logger.info(f"Имя аватара {avatar_index + 1}: {name}")
        return name

    def click_view_profile(self, avatar_index: int):
        self.hover_over_avatar(avatar_index)
        profile_xpath = self._PROFILE_LINK_XPATH.format(avatar_index + 1)
        profile_link = WebElement(self.browser, profile_xpath, f"Ссылка профиля {avatar_index + 1}")
        Logger.info(f"Нажимаем ссылку аватара {avatar_index + 1}")
        profile_link.click()