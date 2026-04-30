import os
from pages.upload.upload_page import UploadPage
from pages.upload.uploaded_file_page import UploadedPage
from utils.logger import Logger


class TestUpload:
    URL = "http://the-internet.herokuapp.com/upload"
    FILE_PATH = "content/toji.jpg"

    def test_upload_file(self, browser):
        Logger.info("Тест: Upload File")

        file_path = os.path.abspath(self.FILE_PATH)

        assert os.path.exists(file_path), f"По пути {file_path} ничего не найдено"

        upload_page = UploadPage(browser)
        browser.get(self.URL)
        upload_page.wait_for_open()

        upload_page.upload_file(file_path)

        uploaded_page = UploadedPage(browser)
        uploaded_page.wait_for_open()

        expected_message = "File Uploaded!"
        uploaded_message = uploaded_page.get_uploaded_message()
        assert uploaded_message == expected_message, f"Ожидалось {expected_message}\n" \
                                                     f"Получено {uploaded_message}"

        uploaded_name = uploaded_page.get_uploaded_file_name()
        assert uploaded_name in file_path, f"Файл не был загружен или имя файла не удалось получить"

        Logger.info(f"Тест upload image завершен успешно")
