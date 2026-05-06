from pages.base_page import BasePage
from elements.label import Label


class UserProfilePage(BasePage):
    UNIQUE_ELEMENT_LOC = "//h1"

    def __init__(self, browser):
        super().__init__(browser)
        self.page_name = "User Profile Page"
        self.unique_element = Label(browser, self.UNIQUE_ELEMENT_LOC, "Заголовок профиля")
