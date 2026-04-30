from pages.base_page import BasePage
from elements.web_element import WebElement
from elements.label import Label
from utils.logger import Logger


class UploadedPage(BasePage):
    UNIQUE_ELEMENT_LOC = "uploaded-files"
    FILE_UPLOADED_LABEL = "//*[@id='content']//h3"
    UPLOADED_FILE_NAME = "uploaded-files"

    def __init__(self, browser):
        super().__init__(browser)
        self.page_name = "Uploaded file page"
        self.unique_element = Label(browser, self.UNIQUE_ELEMENT_LOC, "Надпись File Uploaded")
        self.uploaded_file = WebElement(browser, self.UPLOADED_FILE_NAME, "Название файла")
        self.uploaded_label = Label(browser, self.FILE_UPLOADED_LABEL, "Надпись File Uploaded")

    def get_uploaded_file_name(self) -> str:
        Logger.info(f"{self}: получение название файла")
        return self.uploaded_file.get_text()

    def get_uploaded_message(self) -> str:
        Logger.info(f"{self}: получение заголовка File Uploaded")
        return self.uploaded_label.get_text()
