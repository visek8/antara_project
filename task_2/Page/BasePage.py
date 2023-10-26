from selenium.common import NoSuchElementException, WebDriverException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def get_element_by_contains_class(self, selector):
        return self.driver.find_element(By.XPATH, f'//div[contains(@class,"{selector}")]')

    def get_locator_by_xpath(self, selector, item=0):
        return self.driver.find_elements(By.XPATH, selector)[item]

    def get_locator_by_contains(self, selector):
        return self.driver.find_element(By.XPATH, f'//div[contains(@class, "{selector}")]')

    def get_locator_by_contains_text(self, text):
        return self.driver.find_element(By.XPATH, f'//*[contains(text(), "{text}")]')

    def get_element(self, selector):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, selector)))

    def assert_that_element_is_selected(self, selector):
        return self.get_locator_by_xpath(selector).is_selected()

    def wait_for_element(self, selector):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, selector)))

    def assert_that_element_is_enabled(self, selector):
        return self.get_locator_by_xpath(selector).is_enabled()

    def assert_that_element_is_displayed(self, selector):
        return self.get_locator_by_xpath(selector).is_displayed()

    def assert_element_is_not_displayed(self, xpath):
        try:
            displayed = self.get_locator_by_xpath(xpath).is_displayed()
            assert not displayed, f"Text {xpath} displayed"
        except NoSuchElementException:
            print(f'Failed to find element. XPATH {xpath}')

    def wait_for_visible_by_hard(self, xpath, retry=5):
        element = None
        for _ in range(retry):
            try:
                element = self.get_locator_by_xpath(xpath)
                break
            except WebDriverException:
                print(f'Failed to find element, will try again. XPATH {xpath}')

        return element, f'Did not find element. XPATH {xpath}'

    def assert_that_attribute_present(self, xpath, attribute):
        element = self.wait_for_visible_by_hard(xpath)
        value = element.get_attribute(attribute)
        if value is not None:
            return True
        return False

    def assert_disable_attribute(self, xpath):
        """Check that element is blocked for editing"""
        assert self.assert_that_attribute_present(xpath, 'disabled'), f"Element '{xpath}' doesn't have attr disabled"

    def get_selector_by_xpath(self, text):
        return f'//*[class="{text}"'

    def fill_field(self, selector, text):
        element = self.get_locator_by_xpath(selector)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.clear()
        element.send_keys(text)

    def click(self, locator):
        return self.get_locator_by_xpath(locator).click()

    def click_text(self, locator):
        return self.get_locator_by_contains_text(locator).click()

    def current_url(self, url):
        return self.driver.current_url == url

    def press_enter(self, selector):
        element = self.get_locator_by_xpath(selector)
        element.driver.send_keys(Keys.ENTER)

    def assert_that_text_is_displayed(self, text):
        return self.get_locator_by_contains_text(text).is_displayed()

    def execute(self, selector):
        element = self.get_locator_by_xpath(selector)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def scroll(self, locator):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.get_locator_by_xpath(locator))

    def scroll_to_text(self, text):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.get_locator_by_contains_text(text))
