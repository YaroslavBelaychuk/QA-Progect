from income_page import Income_Page
from new_account_page import New_Account_Page
from my_goals_page import MyGoalsPage
from debt_page import DebtPage
from new_category_page import CategoryPage


def test_income(driver, account):
    income_page = Income_Page(driver)
    assert "1 000 BYN" == income_page.my_income().text

def test_income_null(driver, account):
    income_page = Income_Page(driver)
    assert "0 BYN" == income_page.my_income_null().text

def test_income_plus_description(driver, account):
    income_page = Income_Page(driver)
    assert "Премия" == income_page.my_income_plus_description().text

def test_income_graph(driver, account):
    income_page = Income_Page(driver)
    assert income_page.my_income_graph().is_displayed()

def test_add_account(driver, account):
    new_account_page = New_Account_Page(driver)
    assert ("БЕЛАРУСБАНК", "2 000 BYN") == new_account_page.add_a_bank_account()

def test_transfer_from_bank_to_card(driver, account):
    new_account_page = New_Account_Page(driver)
    assert ("Карта", "2 000 BYN") == new_account_page.transfer_from_bank_to_card()

def test_transfer_on_calendar(driver, account):
    new_account_page = New_Account_Page(driver)
    assert new_account_page.date_on_calendar().is_displayed()

def test_transactions(driver, account):
    new_account_page = New_Account_Page(driver)
    assert "Беларусбанк → Карта" in new_account_page.transactions()

def test_number_of_accounts(driver, account):
    new_account_page = New_Account_Page(driver)
    assert (len(new_account_page.number_of_accounts())) == 3

def test_create_goal(driver, account):
    my_goals_page = MyGoalsPage(driver)
    assert "На новый автомобиль (Цели)" == my_goals_page.create_a_goal()

def test_picture_car(driver, account):
    my_goals_page = MyGoalsPage(driver)
    assert my_goals_page.picture().is_displayed()

def test_my_goal_in_accounts(driver, account):
    my_goals_page = MyGoalsPage(driver)
    assert "НА ГОЛЬФ" == my_goals_page.my_goal_in_my_accounts()

def test_delete_my_goals(driver, account):
    my_goals_page = MyGoalsPage(driver)
    assert "НА ГОЛЬФ" not in my_goals_page.delete_my_goal()

def test_delete_bank_account(driver, account):
    new_account_page = New_Account_Page(driver)
    assert "Беларусбанк" not in new_account_page.delete_new_bank_account()

def test_delete_my_income(driver, account):
    income_page = Income_Page(driver)
    assert "Мои доходы", "0 BYN" in income_page.delete_income()

def test_my_debt(driver, account):
    debt_page = DebtPage(driver)
    assert "Игорь" == debt_page.debt()

def test_sum_cash(driver, account):
    debt_page = DebtPage(driver)
    assert "Наличные деньги", "100 BYN" == debt_page.cash()

def test_delete_debt(driver, account):
    debt_page = DebtPage(driver)
    assert "Ничего не найдено" == debt_page.delete_a_debt()

def test_create_new_catogory_income(driver, account):
    new_category_page = CategoryPage(driver)
    assert "Подработка" == new_category_page.new_category()

def test_category_in_income(driver, account):
    new_category_page = CategoryPage(driver)
    assert "Подработка" == new_category_page.part_time_job_in_income()

def test_delete_category_in_income(driver, account):
    new_category_page = CategoryPage(driver)
    assert "Подработка" not in new_category_page.delete_new_category()

