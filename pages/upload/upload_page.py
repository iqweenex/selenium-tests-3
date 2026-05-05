from elements.input import Input
from pages.base_page import BasePage
from elements.web_element import WebElement
from utils.logger import Logger
from utils.pyautogui_utils import PyAutoGUIUtilities
import os


class UploadPage(BasePage):
    UNIQUE_ELEMENT_LOC = "file-upload"
    FILE_INPUT = "file-upload"
    UPLOAD_BUTTON = "file-submit"
    DRAG_DROP_AREA = "drag-drop-upload"
    SUCCESS_MARK = "//*[@id='drag-drop-upload']//div[contains(@class,'dz-success-mark')]//span"
    SELECTED_FILE = "//*[@id='drag-drop-upload']//div[contains(@class, 'dz-filename')]//span"

    def __init__(self, browser):
        super().__init__(browser)
        self.page_name = "Upload page"
        self.unique_element = WebElement(browser, self.UNIQUE_ELEMENT_LOC, "Кнопка выбора файла")
        self.file_input = Input(browser, self.FILE_INPUT, "Выбор файла")
        self.upload_button = WebElement(browser, self.UPLOAD_BUTTON, "Кнопка загрузить")
        self.drag_drop_area = WebElement(browser, self.DRAG_DROP_AREA, "Область для загрузки")
        self.success_mark = WebElement(browser, self.SUCCESS_MARK, "Галочка")
        self.file_name = WebElement(browser, self.SELECTED_FILE, "Выбранный файл")

    def upload_file(self, file_path: str):
        self.file_input.send_keys(file_path, clear=False)
        self.upload_button.click()

    def file_dialog_upload(self, file_path: str):
        Logger.info("Клик по области загрузки")
        self.drag_drop_area.click()
        Logger.info("Работа PyAutoGUI")
        PyAutoGUIUtilities.upload_file(file_path)
        self.success_mark.wait_for_visible()

    def get_success_mark_text(self):
        return self.success_mark.get_text()

    def get_filename_text(self):
        return self.file_name.get_text()
