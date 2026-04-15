from pages.hovers_page import HoversPage
from utils.logger import Logger


class TestHovers:
    BASE_URL_HOVER_PAGE = "https://the-internet.herokuapp.com/"
    URL_FOR_OPEN = BASE_URL_HOVER_PAGE+"hovers"
    URL_FOR_USERS = BASE_URL_HOVER_PAGE + "users/"

    def test_hovers_all_users(self, browser):
        Logger.info("Тест: Hovers")
        hovers_page = HoversPage(browser)
        Logger.info(f"Открываем страницу {hovers_page.page_name}")
        browser.get(self.URL_FOR_OPEN)
        hovers_page.wait_for_open()

        user_count = hovers_page.get_avatars_count()
        Logger.info(f"Найдено пользователей: {user_count}")

        for i in range(user_count):
            Logger.info(f"Проверка пользователя {i + 1}")

            user_name = hovers_page.get_user_name(i)
            Logger.info(f"Отображаемое имя: {user_name}")
            expected_name = f"name: user{i + 1}"
            assert user_name == expected_name, \
                f"Ожидалось: {expected_name}\n" \
                f"Получено: {user_name}"

            hovers_page.click_view_profile(i)

            expected_url = f"{self.URL_FOR_USERS}{i + 1}"
            current_url = browser.driver.current_url
            Logger.info(f"Ожидаемый URL: {expected_url}")
            Logger.info(f"Фактический URL: {current_url}")

            assert current_url == expected_url, \
                f"Ожидался URL: {expected_url}\n" \
                f"Получен: {current_url}"

            if i < user_count - 1:
                hovers_page.open(self.URL_FOR_OPEN)

        Logger.info("Тест Hovers успешно пройден")
