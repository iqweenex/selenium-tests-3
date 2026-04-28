from pages.hovers.hovers_page import HoversPage
from pages.hovers.user_profile_page import UserProfilePage
from utils.logger import Logger


class TestHovers:
    URL_HOVERS = "https://the-internet.herokuapp.com/hovers"

    def test_hovers_all_users(self, browser):
        Logger.info("Тест: Hovers")
        hovers_page = HoversPage(browser)

        browser.get(self.URL_HOVERS)
        hovers_page.wait_for_open()

        user_count = hovers_page.get_avatars_count()
        Logger.info(f"Найдено пользователей: {user_count}")

        for i in range(user_count):
            Logger.info(f"Проверка пользователя {i + 1}")

            user_name = hovers_page.get_user_name(i)
            expected_name = f"name: user{i + 1}"
            assert user_name == expected_name, f"Ожидалось: {expected_name}, Получено: {user_name}"
            Logger.info(f"Отображаемое имя: {user_name}")

            hovers_page.click_view_profile(i)

            # Проверяем страницу профиля
            profile_page = UserProfilePage(browser)
            profile_page.wait_for_open()

            expected_url = f"https://the-internet.herokuapp.com/users/{i + 1}"
            current_url = browser.driver.current_url
            Logger.info(f"Ожидаемый URL: {expected_url}")
            Logger.info(f"Фактический URL: {current_url}")

            assert current_url == expected_url, f"Ожидался URL: {expected_url}, Получен: {current_url}"

            # Возвращаемся на главную страницу (кроме последней итерации)
            if i < user_count - 1:
                browser.get(self.URL_HOVERS)
                hovers_page.wait_for_open()

        Logger.info("Тест Hovers успешно пройден")