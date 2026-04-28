from pages.base_page import BasePage
from elements.web_element import WebElement
from elements.multi_web_element import MultiWebElement
from utils.logger import Logger

class DynamicContentPage(BasePage):
    UNIQUE_ELEMENT_LOC = "//h3[contains(text(), 'Dynamic')]"
    IMAGES_XPATH = "(//div[@class='row']//img)[{}]"

    def __init__(self, browser):
        super().__init__(browser)
        self.page_name = 'Dynamic content page'
        self.unique_element = WebElement(browser, self.UNIQUE_ELEMENT_LOC, "Заголовок страницы")
        self.images = MultiWebElement(browser, self.IMAGES_XPATH, "Изображения", timeout=2)

    def get_images_src_list(self) -> list:
        Logger.info(f"{self}: получение списка src аттрибутов img")
        src_list = []
        for img in self.images:
            src_list.append(img.get_attribute('src'))
        return src_list

    def has_duplicate_images(self) -> bool:
        src_list = self.get_images_src_list()
        Logger.info("Проверка на дубликаты")
        has_duplicat = len(set(src_list)) != len(src_list)
        return has_duplicat

    def refresh_page(self):
        Logger.info(f"{self}: обновление страницы")
        self.browser.refresh()
