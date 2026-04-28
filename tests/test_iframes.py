from pages.iframe.demoqa_main_page import DemoqaMainPage
from pages.iframe.alerts_frame_windows_page import AlertsFrameWindowsPage
from pages.iframe.nested_frames_page import NestedFramesPage
from pages.iframe.frames_page import FramesPage
from utils.logger import Logger


class TestIframe:
    URL_DEMOQA = "https://demoqa.com"

    def test_iframes(self, browser):
        Logger.info(f"Открываем главную страницу {self.URL_DEMOQA}")
        main_page = DemoqaMainPage(browser)
        browser.get(self.URL_DEMOQA)
        main_page.wait_for_open()
        Logger.info(f"Кликаем по карточке Alerts, Frame & Windows")
        main_page.alerts_card.click()
        alerts_page = AlertsFrameWindowsPage(browser)
        alerts_page.wait_for_open()

        self.nested_frames(browser, alerts_page)
        self.frames(browser, alerts_page)

    def nested_frames(self, browser, alerts_page: AlertsFrameWindowsPage):
        Logger.info("Тест: Nested Frames")

        alerts_page.ensure_menu_open()
        Logger.info(f"Кликаем Nested Frame")
        alerts_page.nested_frames_menu.click()

        nested_frames_page = NestedFramesPage(browser)
        nested_frames_page.wait_for_open()

        expected_parent_text = "Parent frame"
        expected_child_text = "Child Iframe"
        parent_text = nested_frames_page.get_parent_frame_text()
        child_text = nested_frames_page.get_child_frame_text()

        assert parent_text == "Parent frame", \
            f"Ожидался: '{expected_parent_text}\n" \
            f"Получен: '{parent_text}'"

        assert child_text == "Child Iframe", \
            f"Ожидался: {expected_child_text}\n" \
            f"Получен: '{child_text}'"

        Logger.info("Тест Nested Frames успешно пройден")

    def frames(self, browser, alerts_page: AlertsFrameWindowsPage):
        Logger.info("Тест: Frames")

        alerts_page.ensure_menu_open()
        alerts_page.frames_menu.click()

        frames_page = FramesPage(browser)
        frames_page.wait_for_open()

        frame1_text = frames_page.get_frame1_text()
        frame2_text = frames_page.get_frame2_text()

        expected_text = "This is a sample page"
        assert frame1_text == expected_text, \
            f"В frame1 ожидался '{expected_text}'\n" \
            f"Получен '{frame1_text}'"

        assert frame2_text == expected_text, \
            f"В frame2 ожидался '{expected_text}'\n" \
            f"Получен '{frame2_text}'"

        assert frame1_text == frame2_text, \
            "Текст в frame1 и frame2 не совпадает\n" \
            f"{frame1_text} != {frame2_text}"

        Logger.info("Тест Frames успешно пройден")
