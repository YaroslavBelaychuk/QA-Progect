from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

begin = By.CSS_SELECTOR, "#header > div.header-upper > div > div.nav-outer > div.outer-box"
enter = By.LINK_TEXT, 'Войти через браузер'
email = By.CSS_SELECTOR, "#loginform-username"
password = By.CSS_SELECTOR, '#loginform-password'
sign_in = By.CLASS_NAME, "button-loading-content"
another_version = By.CSS_SELECTOR, "#popup-container_1 > header > div.PageHeader_toolbarLarge__OXhVD > div > button > svg"
another_version_of_the_site = By.CSS_SELECTOR, "#popup-container_1 > header > div.PageHeader_toolbarLarge__OXhVD > div > div > div > nav > button:nth-child(1)"
end_of_subscription = By.LINK_TEXT, "Закрыть"

class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open(self):
        raise NotImplementedError

    def open_home_page(self):
        self.driver.get('https://www.cubux.net/ru/')

    def find_element(self, *args):
        by, val = args[0]
        return self.driver.find_element(by, val)

    def find_elements(self, *args):
        by, val = args[0]
        return self.driver.find_elements(by, val)


    def to_begin(self):
        self.find_element(begin).click()

    def enter(self):
        self.find_element(enter).click()

    def login_and_password(self):
        self.find_element(email).send_keys("jaroslav.belaychuk@gmail.com")
        self.find_element(password).send_keys("Jarikello505155")
        self.find_element(sign_in).click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(another_version),
            message=f"Can't find element by locator"
                    f"{another_version}")
        self.find_element(another_version).click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(another_version_of_the_site),
            message=f"Can't find element by locator"
                    f"{another_version_of_the_site}")
        self.find_element(another_version_of_the_site).click()




