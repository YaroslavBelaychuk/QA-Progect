from base_page import BasePage
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

button_plus = By.CLASS_NAME, "icon-st__plus-big"
name_goal = By.CSS_SELECTOR, 'input[class="inp-shadow shadow-grey inp-size__big db align-center"]'
change_your_avatar_button = By.CSS_SELECTOR, 'input[type="file"]'
field_sum = By.CSS_SELECTOR, 'input[class="inp-shadow shadow-grey inp-size__big db align-center font-21"]'
field_start_date = By.CSS_SELECTOR, 'a[class="link-like-input inp-shadow shadow-grey inp-size__big db"]'
date = By.CSS_SELECTOR, 'table > tbody > tr:nth-child(3) > td:nth-child(7)'
select_an_account = By.CSS_SELECTOR, 'div.col-b.width260.align-left > span > span > span.selection > span'
field_saving = By.CSS_SELECTOR, 'input[class="inp-shadow shadow-grey inp-size__big db"]'
create_new_account_label = By.CSS_SELECTOR, 'label:nth-child(2) > input[type=radio]'
account_name_for_the_goal = By.CSS_SELECTOR, 'div.col-b.width300.align-left > input'
save_goal = By.CLASS_NAME, "button-loading_content"
scheduled_transactions = By.CLASS_NAME, "text-overflow-fadeout"
my_goals = By.CSS_SELECTOR, "div > div.right-col > div > div.title-b > p > a"
picture = By.CSS_SELECTOR, 'div.list-elem-row.clearfix > div.img-b > a > img'
slide_accounts = By.CLASS_NAME, "hidden-slide--btn"
name_accounts = By.CSS_SELECTOR, "div.hidden-slide > div > a > span.s-text"
settings_button = By.CSS_SELECTOR, 'input[class="btn-settings btn-orange"]'
accounts = By.CSS_SELECTOR, 'div.content-wrapper.dialog-border__dashed.mt0 > div > div > ul > li:nth-child(7) > a'
delete_button = By.CSS_SELECTOR, 'tr:nth-child(4) > td:nth-child(4) > a.account-delete_button.iconic-link > i'
delete_with_related_data = By.CSS_SELECTOR, 'button[class="btn-red btn-size2"]'
close_button = By.CSS_SELECTOR, 'a[class="dialog-close-btn"]'
name_accounts_in_setting = By.CSS_SELECTOR, 'input[class="db inp-size__normal inp-shadow shadow-grey"]'

class MyGoalsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    def create_a_goal(self):
        self.find_element(button_plus).click()
        self.find_element(name_goal).send_keys("На новый автомобиль")
        self.find_element(change_your_avatar_button).send_keys("E:/Фото/golf-7-3.jpg")
        self.find_element(field_sum).send_keys("30000")
        self.find_element(field_start_date).click()
        self.find_element(date).click()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.find_element(select_an_account).click()
        ActionChains(self.driver).key_down(Keys.ARROW_DOWN).key_up(
            Keys.ARROW_DOWN
        ).perform()
        ActionChains(self.driver).key_down(Keys.ENTER).key_up(
            Keys.ENTER
        ).perform()
        sleep(0.5)
        self.find_element(field_saving).send_keys("100")
        self.find_element(create_new_account_label).click()
        sleep(0.5)
        self.find_element(account_name_for_the_goal).send_keys("На Гольф")
        self.find_element(save_goal).click()
        sleep(0.5)
        return self.find_element(scheduled_transactions).text

    def picture(self):
        self.find_element(my_goals).click()
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(picture),
            message=f"Can't find element by locator"
                    f"{picture}")
        return self.find_element(picture)

    def my_goal_in_my_accounts(self):
        self.find_element(slide_accounts).click()
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element(name_accounts, "НА ГОЛЬФ"),
            message=f"Can't find element by locator"
                    f"{name_accounts}")
        return self.find_element(name_accounts).text

    def delete_my_goal(self):
        self.find_element(settings_button).click()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(accounts),
            message=f"Can't find element by locator"
                    f"{accounts}")
        self.find_element(accounts).click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(delete_button),
            message=f"Can't find element by locator"
                    f"{delete_button}")
        self.find_element(delete_button).click()
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





















