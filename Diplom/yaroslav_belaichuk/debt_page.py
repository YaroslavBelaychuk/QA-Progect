from base_page import BasePage
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

icon_debt = By.CSS_SELECTOR, 'div.window3 > a > span.icon-b > span'
button_add = By.CSS_SELECTOR, 'td.loan-side-wrapper.loan-side_credit > div > div.loan-side-content.loan-side-header > button'
add_a_counterparty = By.CSS_SELECTOR, '.mt10 > div:nth-child(1) > div > span.s-inp.chosen-select__big.account-add-btn_wrapper > a > i'
name_a_counterparty = By.CSS_SELECTOR, 'form > div:nth-child(1) > div.mt5 > input'
save_name_a_counterparty = By.CSS_SELECTOR, 'div.mt10.align-center > button > span.button-loading_content'
sum_debt = By.CSS_SELECTOR, 'input[class="db inp-size__big inp-shadow shadow-grey font_amount-big align-center"]'
field_select_an_account = By.CSS_SELECTOR, 'div:nth-child(4) > div > div > span.s-inp.chosen-select__big.account-add-btn_wrapper > span > span.selection > span'
specify_the_date_button = By.CSS_SELECTOR, 'div.dialog-count--day > div > label:nth-child(4)'
date_selection = By.CSS_SELECTOR, 'table > tbody > tr:nth-child(2) > td:nth-child(2)'
add_return_date = By.CSS_SELECTOR, "div.dialog-count--top.mt15 > div > div:nth-child(1) > label > input[type=checkbox]"
specify_the_date_return = By.CSS_SELECTOR, 'div.dib.vam.ml10 > div > div > div > a'
return_date = By.CSS_SELECTOR, 'table > tbody > tr:nth-child(3) > td:nth-child(4)'
description = By.CSS_SELECTOR, 'textarea[class="inp-shadow db shadow-grey inp-size__big height80"]'
save_debt = By.CSS_SELECTOR, 'span[class="button-loading_content"]'
name_a_counterparty_in_debds = By.CSS_SELECTOR, 'div[class="loan-agent_name"]'
cash_button = By.CSS_SELECTOR, 'div:nth-child(1) > div:nth-child(1) > a > span.s-text'
sum_cash = By.CSS_SELECTOR, 'div:nth-child(1) > div:nth-child(1) > a > span.s-text'
history_button = By.CSS_SELECTOR, 'i[class="fa fa-history"]'
delete_button = By.CSS_SELECTOR, 'i[class="fa fa-trash"]'
confirmation = By.CSS_SELECTOR, 'button[class="btn-size2 btn-orange"]'
close_form = By.CSS_SELECTOR, '#ui-id-108 > div > div > a'
debt_empty = By.CSS_SELECTOR, 'div.content-wrapper.dialog-border__dashed.mt0 > div > div:nth-child(5) > div'


class DebtPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def debt(self):
        self.find_element(icon_debt).click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(button_add),
            message=f"Can't find element by locator"
                    f"{button_add}")
        self.find_element(button_add).click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(add_a_counterparty),
            message=f"Can't find element by locator"
                    f"{add_a_counterparty}")
        self.find_element(add_a_counterparty).click()
        self.find_element(name_a_counterparty).send_keys("Игорь")
        self.find_element(save_name_a_counterparty).click()
        self.find_element(sum_debt).send_keys('100')
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(field_select_an_account),
            message=f"Can't find element by locator"
                    f"{field_select_an_account}")
        self.find_element(field_select_an_account).click()
        ActionChains(self.driver).key_down(Keys.ENTER).key_up(
            Keys.ENTER
        ).perform()
        self.find_element(specify_the_date_button).click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(date_selection),
            message=f"Can't find element by locator"
                    f"{date_selection}")
        self.find_element(date_selection).click()
        self.find_element(add_return_date).click()
        self.find_element(specify_the_date_return).click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(return_date),
            message=f"Can't find element by locator"
                    f"{return_date}")
        self.find_element(return_date).click()
        self.find_element(description).send_keys('Не верну - накажет')
        self.find_element(save_debt).click()
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element(name_a_counterparty_in_debds, "Игорь"),
            message=f"Can't find element by locator"
                    f"{name_a_counterparty_in_debds}")
        return self.find_element(name_a_counterparty_in_debds).text

    def cash(self):
        return (
            self.find_element(cash_button).text,
            self.find_element(sum_cash).text
        )

    def delete_a_debt(self):
        self.find_element(icon_debt).click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(history_button),
            message=f"Can't find element by locator"
                    f"{history_button}")
        self.find_element(history_button).click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(delete_button),
            message=f"Can't find element by locator"
                    f"{delete_button}")
        self.find_element(delete_button).click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(confirmation),
            message=f"Can't find element by locator"
                    f"{confirmation}")
        self.find_element(confirmation).click()
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element(debt_empty, "Ничего не найдено"),
            message=f"Can't find element by locator"
                    f"{debt_empty}")
        return self.find_element(debt_empty).text















