import os
import sys
import pytest
from pages.upload.upload_page import UploadPage
from utils.logger import Logger


class TestFileDialogUpload:
    URL = "http://the-internet.herokuapp.com/upload"

    @pytest.mark.skipif(
        sys.platform != "win32",
        reason="Работает только на Windows в head режиме"
    )
    def test_file_dialog_upload(self, browser):
        Logger.info("Тест File Dialog Upload")

        file_path = os.path.abspath("content/toji.jpg")

        assert os.path.exists(file_path), f"Файл {file_path} не найден"

        upload_page = UploadPage(browser)
        browser.get(self.URL)
        upload_page.wait_for_open()

        upload_page.file_dialog_upload(file_path)

        file_name = upload_page.get_filename_text()
        expected_file_name = file_path.split('\\')[-1]

        assert file_name == expected_file_name, f"Ожидалось {expected_file_name}\n" \
                                                f"Получено {file_name}"

        expected_mark = "✔"
        success_mark = upload_page.get_success_mark_text()

        assert expected_mark == success_mark, f"Ожидалось {expected_mark}\n" \
                                              f"Получено {success_mark}"