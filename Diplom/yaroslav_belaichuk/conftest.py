from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest
from base_page import BasePage
from time import sleep


@pytest.fixture(scope='function')
def driver():
    options = Options()
    options.add_argument('start-maximized')
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def account(driver):
    login_page = BasePage(driver)
    login_page.open_home_page()
    login_page.to_begin()
    login_page.enter()
    tabs = driver.window_handles
    driver.switch_to.window(tabs[1])
    login_page.login_and_password()

