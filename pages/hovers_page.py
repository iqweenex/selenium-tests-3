from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators.hovers_locators import HoversLocators
from utils.logger import Logger


class HoversPage(BasePage):

    def open(self):
        self.open_url("/hovers")
        Logger.info("Открыта страница Hovers")
        self.wait_for_page_load()

    def wait_for_page_load(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located(HoversLocators.AVATARS),
            message="Страница не загрузилась"
        )

    def get_avatars(self):
        """Возвращает список WebElement аватаров"""
        elements = self.wait_for_elements(HoversLocators.AVATARS, "Аватары", timeout=10)
        Logger.debug(f"Найдено аватаров: {len(elements)}")
        return elements

    def hover_over_avatar(self, avatar_index: int):
        """Наводит курсор на аватар и ждет появления имени"""
        # Ждем, что страница стабильна
        WebDriverWait(self.driver, 5).until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )

        avatars = self.get_avatars()
        if avatar_index >= len(avatars):
            raise IndexError(f"Аватар с индексом {avatar_index} не найден")

        avatar = avatars[avatar_index]

        # Прокручиваем к элементу
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", avatar)

        # Небольшая пауза для стабилизации
        import time
        time.sleep(0.3)

        # Наводим курсор
        actions = ActionChains(self.driver)
        actions.move_to_element(avatar).perform()

        Logger.info(f"Курсор наведен на аватар {avatar_index + 1}")

        # Ждем появления имени
        try:
            WebDriverWait(avatar, 5).until(
                EC.visibility_of_element_located(HoversLocators.USER_NAME),
                message=f"Имя не появилось для аватара {avatar_index + 1}"
            )
            Logger.debug(f"Имя появилось для аватара {avatar_index + 1}")
        except Exception as e:
            Logger.error(f"Ошибка при ожидании имени: {e}")
            raise

    def get_user_name_from_avatar(self, avatar_index: int) -> str:
        """Получает имя из конкретного аватара"""
        avatars = self.get_avatars()
        avatar = avatars[avatar_index]

        user_name_element = avatar.find_element(*HoversLocators.USER_NAME)
        name = user_name_element.text
        Logger.debug(f"Имя для аватара {avatar_index + 1}: {name}")
        return name

    def click_view_profile(self, avatar_index: int):
        """Нажимает ссылку внутри конкретного аватара"""
        avatars = self.get_avatars()
        avatar = avatars[avatar_index]

        profile_link = WebDriverWait(avatar, 5).until(
            EC.element_to_be_clickable(HoversLocators.PROFILE_LINK),
            message=f"Ссылка не кликабельна для аватара {avatar_index + 1}"
        )
        profile_link.click()

        Logger.info(f"Нажата ссылка для аватара {avatar_index + 1}")

    def go_back(self):
        """Возвращается на главную страницу через открытие URL"""
        # Вместо back() открываем страницу заново
        self.open_url("/hovers")
        self.wait_for_page_load()
        Logger.info("Вернулись на страницу Hovers")