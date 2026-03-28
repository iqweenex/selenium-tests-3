import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from utils.logger import Logger


@pytest.fixture
def driver():
    Logger.info("Запуск браузера Chrome")
    service = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service)
    browser.maximize_window()
    yield browser
    Logger.info("Закрытие браузера\n")
    browser.quit()
