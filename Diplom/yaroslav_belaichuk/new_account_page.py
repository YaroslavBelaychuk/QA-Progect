from base_page import BasePage
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


add_an_account = By.CLASS_NAME, "dialog-add-bank--link"
choosing_a_bank = By.LINK_TEXT, "Беларусбанк"
balance = By.CSS_SELECTOR, 'div:nth-child(3) > div.col-b.vam.width300 > div > input'
save_new_account = By.CSS_SELECTOR, 'button[class="btn-green btn-size2"]'
name_bank = By.CSS_SELECTOR, 'div > div:nth-child(1) > div:nth-child(3) > a > span.s-text'
money_in_the_bank = By.CSS_SELECTOR, "div:nth-child(1) > div:nth-child(3) > a > span.s-sum"
button_transfer_from_bank_to_card = By.CSS_SELECTOR, "div:nth-child(3) > span.s-control > a.btn-plus.btn-plus-stack.dialog-link__account-transfer > span > i.fa.fa-exchange.fa-stack-1x.fa-inverse"
input_sum_transfer = By.CSS_SELECTOR, 'input[class="db font-21 inp-size__big inp-shadow shadow-grey input_amount-big"]'
select_an_account = By.CSS_SELECTOR, 'div:nth-child(3) > div.s-inp.chosen-select__big > span > span.selection > span'
specify_the_date = By.CSS_SELECTOR, 'div:nth-child(5) > div.dialog-count--day > div > label:nth-child(4)'
day_on_calendar = By.CSS_SELECTOR, 'div.datepicker-days > table > tbody > tr:nth-child(2) > td:nth-child(1)'
additional_settings = By.CLASS_NAME, "js-show_btn-caret"
description = By.CSS_SELECTOR, "div:nth-child(7) > div.dialog-count--bottom > div > div.col-b.width280 > span > textarea"
save_transfer = By.CSS_SELECTOR, 'button[class="btn-size2 mr3 btn-orange btn-submit"]'
money_on_card = By.CSS_SELECTOR, 'div:nth-child(2) > span.s-text > span > span'
sum_money_on_card = By.CSS_SELECTOR, 'div.scroll-pane > div > div > div > div > div:nth-child(2) > span.s-price'
date_on_calendar = By.CSS_SELECTOR, 'td:nth-child(1) > a > div > i.icon-st__green_d'
transfer_on_calendar = By.CSS_SELECTOR, 'div:nth-child(1) > span.b-day-card--incom > span.s-price'
transactions = By.CSS_SELECTOR, 'div > div > div > ul > li:nth-child(4) > a'
transaction_from_bank_to_card = By.CSS_SELECTOR, 'td:nth-child(5)'
settings_button = By.CSS_SELECTOR, 'input[class="btn-settings btn-orange"]'
accounts = By.CSS_SELECTOR, 'div.content-wrapper.dialog-border__dashed.mt0 > div > div > ul > li:nth-child(7) > a'
my_accounts = By.CSS_SELECTOR, 'span[class="select-item-custom-title"]'
delete_bank_account = By.CSS_SELECTOR, 'tr:nth-child(3) > td:nth-child(4) > a.account-delete_button.iconic-link > i'
delete_with_related_data = By.CSS_SELECTOR, 'button[class="btn-red btn-size2"]'
close_button = By.CSS_SELECTOR, 'a[class="dialog-close-btn"]'
name_accounts_in_setting = By.CSS_SELECTOR, 'input[class="db inp-size__normal inp-shadow shadow-grey"]'


class New_Account_Page(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def add_a_bank_account(self):
        self.find_element(add_an_account).click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(choosing_a_bank),
            message=f"Can't find element by locator"
                    f"{choosing_a_bank}")
        self.find_element(choosing_a_bank).click()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(0.5)
        self.find_element(balance).click()
        sleep(0.5)
        self.find_element(balance).send_keys("2000")
        self.find_element(save_new_account).click()
        sleep(3)
        return (self.find_element(name_bank).text, self.find_element(money_in_the_bank).text)

    def transfer_from_bank_to_card(self):
        self.find_element(name_bank).click()
        sleep(5)
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_all_elements_located(button_transfer_from_bank_to_card),
            message=f"Can't find element by locator"
                    f"{button_transfer_from_bank_to_card}")
        self.find_element(button_transfer_from_bank_to_card).click()
        self.find_element(input_sum_transfer).send_keys("500 + 500")
        self.find_element(select_an_account).click()
        ActionChains(self.driver).key_down(Keys.ARROW_DOWN).key_up(
            Keys.ARROW_DOWN
        ).perform()
        ActionChains(self.driver).key_down(Keys.ENTER).key_up(
            Keys.ENTER
        ).perform()
        self.find_element(specify_the_date).click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(day_on_calendar),
            message=f"Can't find element by locator"
                    f"{day_on_calendar}")
        self.find_element(day_on_calendar).click()
        self.find_element(additional_settings).click()
        self.find_element(description).click()
        self.find_element(description).send_keys("Перевод маме")
        self.find_element(save_transfer).click()
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element(sum_money_on_card, "2 000 BYN"),
            message=f"Can't find element by locator"
                    f"{sum_money_on_card}")
        return (self.find_element(money_on_card).text, self.find_element(sum_money_on_card).text)

    def date_on_calendar(self):
        self.find_element(name_bank).click()
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_all_elements_located(date_on_calendar),
            message=f"Can't find element by locator"
                    f"{date_on_calendar}")
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(0.5)
        return self.find_element(date_on_calendar)

    def transactions(self):
        self.find_element(name_bank).click()
        sleep(5)
        WebDriverWait(self.driver, 30).until(
            EC.visibility_of_all_elements_located(transactions),
            message=f"Can't find element by locator"
                    f"{transactions}")
        self.find_element(transactions).click()
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(transaction_from_bank_to_card),
            message=f"Can't find element by locator"
                    f"{transaction_from_bank_to_card}")
        elements = self.find_elements(transaction_from_bank_to_card)
        result = []
        for bank_account in elements:
            result.append(bank_account.text)
        return result

    def number_of_accounts(self):
        self.find_element(settings_button).click()
        WebDriverWait(self.driver, 10).until(
             EC.element_to_be_clickable(accounts),
             message=f"Can't find element by locator"
                     f"{accounts}")
        self.find_element(accounts).click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(my_accounts),
            message=f"Can't find element by locator"
                    f"{my_accounts}")
        return self.find_elements(my_accounts)

    def delete_new_bank_account(self):
        self.find_element(settings_button).click()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(accounts),
            message=f"Can't find element by locator"
                    f"{accounts}")
        self.find_element(accounts).click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(delete_bank_account),
            message=f"Can't find element by locator"
                    f"{delete_bank_account}")
        self.find_element(delete_bank_account).click()
        sleep(1)
        self.find_element(delete_with_related_data).click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(close_button),
            message=f"Can't find element by locator"
                    f"{close_button}")
        self.find_element(close_button).click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(settings_button),
            message=f"Can't find element by locator"
                    f"{settings_button}")
        self.find_element(settings_button).click()
        sleep(1)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(accounts),
            message=f"Can't find element by locator"
                    f"{accounts}")
        self.find_element(accounts).click()
        elements_accounts = self.find_elements(name_accounts_in_setting)
        result = []
        for account in elements_accounts:
            result.append(account.text)
        return result
















