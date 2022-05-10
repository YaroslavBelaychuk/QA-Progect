from base_page import BasePage
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


income = By.CSS_SELECTOR, "#header > div > div.h-house > div.h-house--window > div.window1 > a"
amount = By.CSS_SELECTOR, 'input[class="db inp-size__big inp-shadow shadow-grey font_amount-big align-center"]'
account = By.CSS_SELECTOR, 'span[class="select2-selection__rendered"]'
salary = By.CSS_SELECTOR, 'div[class="category-title"]'
save = By.CSS_SELECTOR, 'button[class="btn-size2 mr3 btn-orange btn-submit button-loading"]'
card = By.CSS_SELECTOR, '#accounts-block-widget > div > div > div > div:nth-child(2) > a > span.s-sum'
sum_button = By.CSS_SELECTOR, 'div.plate-b.plate-b-mirror.f-right > div.bottom-b > p.p-sum'
delete = By.CSS_SELECTOR, 'a[class="iconic-link transaction-del_link"]'
confirmation = By.CSS_SELECTOR, 'button[class="btn-size2 btn-orange"]'
close = By.CLASS_NAME, "dialog-close-btn"
description = By.CSS_SELECTOR, 'textarea[class="inp-shadow db shadow-grey inp-size__big height50"]'
save_with_description = By.CSS_SELECTOR, 'button[class="btn-size2 mr3 btn-orange btn-submit button-loading"]'
transaction_per_month_description = By.CSS_SELECTOR, 'td:nth-child(6)'
graph = By.CSS_SELECTOR, 'g:nth-child(2) > path.highcharts-3d-front'
transactions = By.CSS_SELECTOR, 'div > div > div > ul > li:nth-child(4) > a'
delete_income_salary = By.CSS_SELECTOR, 'td:nth-child(8) > span > a.iconic-link.transaction-del_link > i'
confirmation_delete_income = By.CSS_SELECTOR, 'button[class="btn-size2 btn-orange"]'
delete_transfer = By.CSS_SELECTOR, 'i[class="fa fa-trash"]'
confirmation_delete_transfer = By.CSS_SELECTOR, 'button[class="btn-size2 btn-orange"]'
close_button = By.CSS_SELECTOR, 'a[class="dialog-close-btn"]'
my_income_null = By.CSS_SELECTOR, 'a[data-main-dialog-tab="tabs-income"]'
digit_income = By.CSS_SELECTOR, 'div.plate-b.plate-b-mirror.f-right > div.bottom-b > p.p-sum > a > em'

class Income_Page(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    def my_income(self):
        self.find_element(income).click()
        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located(amount),
            message=f"Can't find element by locator"
                    f"{amount}")
        self.find_element(amount).send_keys("1000")
        self.find_element(account).click()
        ActionChains(self.driver).key_down(Keys.ARROW_DOWN).key_up(
            Keys.ARROW_DOWN
        ).perform()
        ActionChains(self.driver).key_down(Keys.ENTER).key_up(
            Keys.ENTER
        ).perform()
        self.find_element(salary).click()
        self.find_element(save).click()
        sleep(2)
        WebDriverWait(self.driver, 15).until(
            EC.text_to_be_present_in_element(card, "1 000 BYN"),
            message=f"Can't find element by locator"
                    f"{card}")
        return self.find_element(card)

    def my_income_null(self):
        WebDriverWait(self.driver, 15).until(
            EC.text_to_be_present_in_element(sum_button, "1 000 BYN"),
            message=f"Can't find element by locator"
                    f"{sum_button}")
        self.find_element(sum_button).click()
        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located(delete),
            message=f"Can't find element by locator"
                    f"{delete}")
        self.find_element(delete).click()
        sleep(0.5)
        self.find_element(confirmation).click()
        self.find_element(close).click()
        sleep(3)
        return self.find_element(sum_button)

    def my_income_plus_description(self):
        self.find_element(income).click()
        self.find_element(amount).send_keys("1000")
        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located(account),
            message=f"Can't find element by locator"
                    f"{account}")
        self.find_element(account).click()
        sleep(0.5)
        ActionChains(self.driver).key_down(Keys.ARROW_DOWN).key_up(
            Keys.ARROW_DOWN
        ).perform()
        sleep(0.5)
        ActionChains(self.driver).key_down(Keys.ENTER).key_up(
            Keys.ENTER
        ).perform()
        sleep(1)
        self.find_element(salary).click()
        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located(description),
            message=f"Can't find element by locator"
                    f"{description}")
        self.find_element(description).send_keys("Премия")
        self.find_element(save_with_description).click()
        WebDriverWait(self.driver, 15).until(
            EC.text_to_be_present_in_element(sum_button, "1 000 BYN"),
            message=f"Can't find element by locator"
                    f"{sum_button}")
        self.find_element(sum_button).click()
        return self.find_element(transaction_per_month_description)

    def my_income_graph(self):
        WebDriverWait(self.driver, 15).until(
            EC.text_to_be_present_in_element(sum_button, "1 000 BYN"),
            message=f"Can't find element by locator"
                    f"{sum_button}")
        self.find_element(sum_button).click()
        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located(graph),
            message=f"Can't find element by locator"
                    f"{graph}")
        return self.find_element(graph)


    def delete_income(self):
        self.find_element(card).click()
        sleep(5)
        WebDriverWait(self.driver, 30).until(
            EC.visibility_of_all_elements_located(transactions),
            message=f"Can't find element by locator"
                    f"{transactions}")
        self.find_element(transactions).click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(delete_income_salary),
            message=f"Can't find element by locator"
                    f"{delete_income_salary}")
        self.find_element(delete_income_salary).click()
        self.find_element(confirmation_delete_income).click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(delete_transfer),
            message=f"Can't find element by locator"
                    f"{delete_transfer}")
        self.find_element(delete_transfer).click()
        self.find_element(confirmation_delete_transfer).click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(close_button),
            message=f"Can't find element by locator"
                    f"{close_button}")
        self.find_element(close_button).click()
        sleep(1)
        return (self.find_element(my_income_null).text, self.find_element(digit_income).text)














