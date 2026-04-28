from utils.logger import Logger


class WindowManager:
    def __init__(self, browser):
        self.browser = browser
        self.main_handle = None
        self.opened_handles = []

    def save_main_handle(self):
        self.main_handle = self.browser.get_current_window_handle()
        Logger.info(f"Сохранена главная вкладка: {self.main_handle}")
        return self.main_handle

    def open_new_window_and_switch(self, action) -> str:
        handles_before = set(self.browser.get_window_handles())
        action()
        handles_after = set(self.browser.get_window_handles())
        new_handle = list(handles_after - handles_before)[0]
        self.browser.switch_to_window(new_handle)
        Logger.info(f"Открытие новой вкладки: {new_handle}")
        self.opened_handles.append(new_handle)
        return new_handle

    def close_all_opened_windows(self):
        Logger.info("Закрытие всех доп вкладок и возврат на главную")
        for handle in self.opened_handles:
            self.browser.switch_to_window(handle)
            self.browser.close()
        self.opened_handles.clear()
        self.browser.switch_to_window(self.main_handle)

    def switch_to_main(self):
        self.browser.switch_to_window(self.main_handle)