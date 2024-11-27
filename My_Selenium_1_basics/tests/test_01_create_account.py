import time

from click import password_option

from pages.account_page import AccountPage
import random
import string
#import time
import pytest

def generate_random_email():
    return f'galaxy-{"".join(random.choices(string.ascii_lowercase, k=6))}@email.com'

def generate_random_first_name(length=3): # Używamy liter alfabetu (małe i duże)
    letters = string.ascii_letters  # 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'  # Generujemy losowy ciąg
    random_string = ''.join(random.choices(letters, k=length))
    return random_string.title()

#@pytest.fixture(scope="session")
def test_create_account(driver):
    account_page = AccountPage(driver)
    account_page.navigate_to_site()
    account_page.go_to_create_account()
    account_page.fill_account_form(
        first_name="Galaxy",
        last_name=f'Surferro {generate_random_first_name()}',
        email=generate_random_email(),
        password="Jestemzdrowy1"
    )
    account_page.submit_account()
    time.sleep(5)
    # Tutaj dodaj asercje np. sprawdzenie, czy użytkownik został poprawnie zarejestrowany
    account_page.click_on_logo_img()
    account_page.log_out()
    time.sleep(5)
# def test_click_on_img_logo(driver):
#     account_page = AccountPage(driver)
#     account_page.click_on_logo_img()

#@pytest.mark.skip(reason="Ten test jest tymczasowo wyłączony")
# def test_logout(driver):
#     account_page = AccountPage(driver)
#
#     # Wyloguj się
#     account_page.log_out()

def test_log_in(driver):
    account_page = AccountPage(driver)
    #account_page.navigate_to_site()
    account_page.go_to_login_account()
    account_page.login_user_account(email='galaxy.surfer@email.com', password='Jestemzdrowy1')
    time.sleep(10)


