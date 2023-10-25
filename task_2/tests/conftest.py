from pathlib import Path
import allure
from allure import attachment_type
from slugify import slugify
import pytest
from selenium import webdriver


@pytest.fixture
def browser_chrome():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)

    yield driver

    driver.close()
    driver.quit()


@pytest.fixture
def open_page(browser_chrome):
    browser_chrome.get("https://www.kinopoisk.ru/s/")
    browser_chrome.maximize_window()
