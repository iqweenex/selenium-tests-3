import os
from pages.upload.upload_page import UploadPage
from pages.upload.uploaded_file_page import UploadedPage
from utils.logger import Logger
from utils.pyautogui_utils import PyAutoGUIUtilities
from selenium.webdriver.support.wait import WebDriverWait


class TestFileDialogUpload:
    URL = "http://the-internet.herokuapp.com/upload"

    def test_file_dialog_upload(self, browser):
        Logger.info("Тест File Dialog Upload")

        file_path = os.path.abspath("content/toji.jpg")

        assert os.path.exists(file_path), f"Файл {file_path} не найден"

        upload_page = UploadPage(browser)
        browser.get(self.URL)
        upload_page.wait_for_open()

        upload_page.file_dialog_upload(file_path)

        file_name = upload_page.file_name.get_text()
        expected_file_name = file_path.split('\\')[-1]

        assert file_name == expected_file_name, f"Ожидалось {expected_file_name}\n" \
                                                f"Получено {file_name}"

        expected_mark = "✔"
        success_mark = upload_page.success_mark.get_text()

        assert expected_mark == success_mark, f"Ожидалось {expected_mark}\n" \
                                              f"Получено {success_mark}"
