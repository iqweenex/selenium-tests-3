import os
import pytest
from pages.upload.upload_page import UploadPage
from utils.logger import Logger


class TestDragAndDropUpload:
    """
    Тест ИИшный, не сработал, исправить не получилось
    Может текст получится загрузить, но jpg не получается,
    большой объем текста перегружает WebDriver (как я понял)
    """
    URL = "http://the-internet.herokuapp.com/upload"

    def test_drag_and_drop_upload(self, browser):
        Logger.info("Тест: Drag and Drop Upload")

        file_path = os.path.abspath("content/toji.jpg")
        expected_file_name = os.path.basename(file_path)

        assert os.path.exists(file_path), f"Файл {file_path} не найден"

        upload_page = UploadPage(browser)
        browser.get(self.URL)
        upload_page.wait_for_open()

        # Эмулируем drag-and-drop через JS
        upload_page.drag_and_drop_file_js(file_path)

        # Проверяем, что появилось имя файла
        file_name = upload_page.file_name.get_text()
        assert expected_file_name in file_name, \
            f"Ожидалось '{expected_file_name}', получено '{file_name}'"

        # Проверяем галочку
        success_mark = upload_page.success_mark.get_text()
        assert success_mark == "✔", \
            f"Ожидалась галочка '✔', получено '{success_mark}'"

        Logger.info("Тест Drag and Drop Upload успешно пройден")