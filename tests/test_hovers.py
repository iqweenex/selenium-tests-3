from pages.hovers_page import HoversPage
from utils.logger import Logger


class TestHovers:

    def test_hovers_all_users(self, driver):
        Logger.info("Тест: Hovers")
        hovers_page = HoversPage(driver)
        hovers_page.open()

        user_count = len(hovers_page.get_avatars())
        Logger.info(f"Найдено пользователей: {user_count}")

        for i in range(user_count):
            Logger.info(f"--- Проверка пользователя {i + 1} ---")

            # Наводим курсор
            hovers_page.hover_over_avatar(i)

            # Получаем имя
            user_name = hovers_page.get_user_name_from_avatar(i)
            Logger.info(f"Отображаемое имя: {user_name}")

            expected_name = f"name: user{i + 1}"
            assert user_name == expected_name, \
                f"Ожидалось '{expected_name}', получено '{user_name}'"

            # Кликаем по ссылке
            hovers_page.click_view_profile(i)

            expected_url = f"https://the-internet.herokuapp.com/users/{i + 1}"
            current_url = driver.current_url
            Logger.info(f"Ожидаемый URL: {expected_url}")
            Logger.info(f"Фактический URL: {current_url}")

            assert current_url == expected_url, \
                f"Ожидался URL '{expected_url}', получен '{current_url}'"

            # Возвращаемся на главную страницу, если это не последний пользователь
            if i < user_count - 1:
                hovers_page.go_back()

        Logger.info("Тест Hovers успешно пройден")