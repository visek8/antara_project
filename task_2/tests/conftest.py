from datetime import datetime
import functools
from distutils.command.config import config
from pathlib import Path
from typing import Callable

import allure
import wrapt as wrapt
from allure import attachment_type
from slugify import slugify
import pytest
from selenium import webdriver
import sys

from allure_commons.utils import func_parameters, represent
from allure_commons._allure import StepContext


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
