import logging
import time
from utils.logger import Logger


class PyAutoGUIUtilities:
    _pyautogui = None
    _checked = False

    @classmethod
    def _ensure_pyautogui(cls):
        if cls._checked:
            return
        cls._checked = True
        try:
            import pyautogui as _pg
            cls._pyautogui = _pg
        except Exception as e:
            Logger.warning(f"pyautogui недоступен в этом окружении: {e}")

    @staticmethod
    def upload_file(file_path: str) -> None:
        PyAutoGUIUtilities._ensure_pyautogui()
        if PyAutoGUIUtilities._pyautogui is None:
            Logger.warning(f"pyautogui недоступен, пропускаем диалог загрузки: {file_path}")
            return

        Logger.info("Handle File Dialog for uploading file")
        time.sleep(5)

        logging.debug(f"Copy '{file_path}' to clipboard and paste")
        import pyperclip
        pyperclip.copy(file_path)
        PyAutoGUIUtilities._pyautogui.hotkey("ctrl", "v")
        time.sleep(1)
        logging.debug("Press enter")
        PyAutoGUIUtilities._pyautogui.hotkey("enter")

        time.sleep(5)