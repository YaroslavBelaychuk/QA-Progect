from base_page import BasePage
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

settings_button = By.CSS_SELECTOR, 'input[class="btn-settings btn-orange"]'
category_button = By.CSS_SELECTOR, 'div.content-wrapper.dialog-border__dashed.mt0 > div > div > ul > li:nth-child(8) > a'
income_tab = By.CSS_SELECTOR, 'div.content-wrapper.dialog-border__dashed.mt0 > div > div > div > div > div > ul > li:nth-child(2)'
field_add_category = By.CSS_SELECTOR, 'div.content-wrapper.dialog-border__dashed.mt0 > div > div > div > div > div > div > div > form > input'
ok_button = By.CSS_SELECTOR, 'div.content-wrapper.dialog-border__dashed.mt0 > div > div > div > div > div > div > div > form > button'
category_part_time_job = By.CSS_SELECTOR, 'div:nth-child(6) > div.settings-categories_item-head.clearfix > span.settings-categories_item_info > span'
income = By.CSS_SELECTOR, "#header > div > div.h-house > div.h-house--window > div.window1 > a"
part_time_job_in_income = By.CSS_SELECTOR, 'li:nth-child(2) > div.category-itself.category-root > div.category-title'
delete_category = By.CSS_SELECTOR, 'div:nth-child(6) > div.settings-categories_item-head.clearfix > span.settings-categories_item-controls > a:nth-child(3) > i'
confirmation_delete_category = By.CSS_SELECTOR, 'button[class="btn-size2 btn-orange"]'
close = By.CSS_SELECTOR, 'a[class="dialog-close-btn"]'
income_categories = By.CSS_SELECTOR, 'div[class="category-title"]'


class CategoryPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    def new_category(self):
        self.find_element(settings_button).click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(category_button),
            message=f"Can't find element by locator"
                    f"{category_button}")
        self.find_element(category_button).click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(income_tab),
            message=f"Can't find element by locator"
                    f"{income_tab}")
        self.find_element(income_tab).click()
        self.find_element(field_add_category).send_keys("Подработка")
        self.find_element(ok_button).click()
        return self.find_element(category_part_time_job).text

    def part_time_job_in_income(self):
        self.find_element(income).click()
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element(part_time_job_in_income, "Подработка"),
            message=f"Can't find element by locator"
                    f"{part_time_job_in_income}")
        return self.find_element(part_time_job_in_income).text

    def delete_new_category(self):
        self.find_element(settings_button).click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(category_button),
            message=f"Can't find element by locator"
                    f"{category_button}")
        self.find_element(category_button).click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(income_tab),
            message=f"Can't find element by locator"
                    f"{income_tab}")
        self.find_element(income_tab).click()
        sleep(0.5)
        self.find_element(delete_category).click()
        self.find_element(confirmation_delete_category).click()
        sleep(1)
        self.find_element(close).click()
        sleep(0.5)
        self.find_element(income).click()
        sleep(1)
        elements = self.find_elements(income_categories)
        result = []
        for categories in elements:
            result.append(categories)
        return result







