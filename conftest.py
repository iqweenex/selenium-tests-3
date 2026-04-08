import pytest
from utils.logger import Logger
from browser.browser_factory import BrowserFactory
from browser.browser import Browser


@pytest.fixture(scope="function")
def browser():
    Logger.info("Запуск браузера Chrome")
    driver = BrowserFactory.get_driver()
    driver.maximize_window()
    browser_instance = Browser(driver)

    yield browser_instance

    Logger.info("Закрытие браузера")
    browser_instance.quit()
