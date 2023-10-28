from datetime import datetime
import allure
import pytest
from selenium import webdriver


@pytest.fixture
def browser_chrome():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)

    yield driver

    attach = driver.get_screenshot_as_png()
    allure.attach(attach, name=f'Screenshot {datetime.today()}', attachment_type=allure.attachment_type.PNG)

    driver.close()
    driver.quit()


@pytest.fixture
def open_page(browser_chrome):
    browser_chrome.get("https://www.kinopoisk.ru/s/")
    browser_chrome.maximize_window()
