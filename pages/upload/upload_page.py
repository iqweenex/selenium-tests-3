from elements.input import Input
from pages.base_page import BasePage
from elements.web_element import WebElement
from utils.logger import Logger
from utils.pyautogui_utils import PyAutoGUIUtilities
from selenium.webdriver.common.by import By
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
        Logger.info(f"Загружаем файл {file_path}")
        self.file_input.send_keys(file_path, clear=False)
        self.upload_button.click()

    def file_dialog_upload(self, file_path: str):
        Logger.info("Клик по области загрузки")
        self.drag_drop_area.click()
        Logger.info("Работа PyAutoGUI")
        PyAutoGUIUtilities.upload_file(file_path)
        self.success_mark.wait_for_visible()


    def drag_and_drop_file_js(self, file_path: str):
        '''
        метод ИИшный, я не совсем понял что и как тут, скорее всего не работает
        :param file_path:
        :return:
        '''
        Logger.info(f"Drag and drop файла {file_path} через JS")

        # Читаем файл как base64 (для изображений)
        import base64
        with open(file_path, "rb") as f:
            file_data = base64.b64encode(f.read()).decode('utf-8')

        filename = os.path.basename(file_path)
        file_ext = filename.split('.')[-1].lower()

        mime_types = {
            'jpg': 'image/jpeg',
            'jpeg': 'image/jpeg',
            'png': 'image/png',
            'gif': 'image/gif'
        }
        mime_type = mime_types.get(file_ext, 'application/octet-stream')

        js_script = """
            const dropZone = arguments[0];
            const fileData = arguments[1];
            const fileName = arguments[2];
            const mimeType = arguments[3];

            const binaryData = atob(fileData);
            const array = new Uint8Array(binaryData.length);
            for (let i = 0; i < binaryData.length; i++) {
                array[i] = binaryData.charCodeAt(i);
            }

            const file = new File([array], fileName, {type: mimeType});
            const dataTransfer = new DataTransfer();
            dataTransfer.items.add(file);

            const dropEvent = new DragEvent('drop', {
                dataTransfer: dataTransfer,
                bubbles: true,
                cancelable: true
            });

            dropZone.dispatchEvent(dropEvent);
            return true;
        """

        result = self.browser.execute_script(js_script, self.drag_drop_area, file_data, filename, mime_type)
        Logger.info(f"JS drag-and-drop результат: {result}")

        self.success_mark.wait_for_visible()
