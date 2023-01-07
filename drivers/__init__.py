import time
from selenium import webdriver
from config import CHROME_DRIVER_LOCATION

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(executable_path=CHROME_DRIVER_LOCATION, chrome_options=options)
driver.maximize_window()


def setup_package():
    print('setup_package: setUp Method called')


def teardown_package():
    try:
        driver.quit()
    except Exception as e:
        print(f'teardown_package: Teardown Method failed {e}')


class CustomWebDriver:
    def enter_value_using_id(self, timeout, id, keys):
        time.sleep(timeout)
        element_selector = driver.find_element_by_id(id)
        element_selector.send_keys(keys)

    def click_on_element_using_id(self, timeout, id):
        time.sleep(timeout)
        element_selector = driver.find_element_by_id(id)
        element_selector.click()

    def click_on_element_using_xpath(self, timeout, xpath):
        time.sleep(timeout)
        element_selector = driver.find_element_by_xpath(xpath)
        element_selector.click()

    def enter_value_using_xpath(self, timeout, xpath, keys):
        time.sleep(timeout)
        element_selector = driver.find_element_by_xpath(xpath)
        element_selector.clear()
        element_selector.send_keys(keys)
