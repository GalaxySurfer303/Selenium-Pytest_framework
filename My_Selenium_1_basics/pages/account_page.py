from selenium.webdriver.common.by import By
import time




class AccountPage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'https://magento.softwaretestingboard.com/'
        self.sign_in_navi_button = (By.XPATH, '/html/body/div[2]/header/div[1]/div/ul/li[2]/a')
        self.sign_in_email = (By.XPATH, '//*[@id="email"]')
        self.sign_in_password = (By.XPATH, '//*[@id="pass"]')
        self.sign_in_btn_cfrm = (By.XPATH, '//*[@id="send2"]')
        self.create_account_navi_button = (By.XPATH, '/html/body/div[2]/header/div[1]/div/ul/li[3]/a')
        self.first_name_field = (By.XPATH, '//*[@id="firstname"]')
        self.last_name_field = (By.XPATH, '//*[@id="lastname"]')
        self.email_field = (By.XPATH, '//*[@id="email_address"]')
        self.password_field = (By.XPATH, '//*[@id="password"]')
        self.password_confirm_field = (By.XPATH, '//*[@id="password-confirmation"]')
        self.create_account_submit_button = (By.XPATH, '//*[@id="form-validate"]/div/div[1]/button')
        self.account_welcome_btn = (By.XPATH, '/html/body/div[2]/header/div[1]/div/ul/li[2]/span/button')
        self.sign_out_popup = (By.XPATH, '/html/body/div[2]/header/div[1]/div/ul/li[2]/div/ul/li[3]/a')
        self.main_logo_img = (By.XPATH, '/html/body/div[2]/header/div[2]/a/img')

    def navigate_to_site(self):
        self.driver.get(self.base_url)

    def go_to_create_account(self):
        self.driver.find_element(*self.create_account_navi_button).click()

    def fill_account_form(self, first_name, last_name, email, password):
        self.driver.find_element(*self.first_name_field).send_keys(first_name)
        self.driver.find_element(*self.last_name_field).send_keys(last_name)
        self.driver.find_element(*self.email_field).send_keys(email)
        self.driver.find_element(*self.password_field).send_keys(password)
        self.driver.find_element(*self.password_confirm_field).send_keys(password)

    def submit_account(self):
        self.driver.find_element(*self.create_account_submit_button).click()

    def click_on_logo_img(self):
        self.driver.find_element(*self.main_logo_img).click()

    def account_welcome_btn_click(self):
        # Znajdź element
        element = self.driver.find_element(*self.account_welcome_btn)

        # Debugowanie - sprawdź, czy element istnieje i jego właściwości
        print("Typ elementu:", type(element))
        print("Czy element jest widoczny:", element.is_displayed())
        print("Czy element jest aktywny:", element.is_enabled())
        print("Tekst elementu:", element.text)

        # Kliknij w element
        element.click()

    def log_out(self):
        welcome_button = self.driver.find_element(*self.account_welcome_btn)
        welcome_button.click()
        self.driver.implicitly_wait(5)
        self.driver.find_element(*self.sign_out_popup).click()
        self.driver.implicitly_wait(5)

    def go_to_login_account(self):
        self.driver.find_element(*self.sign_in_navi_button).click()

    def login_user_account(self, email, password):
        self.driver.find_element(*self.sign_in_email).send_keys(email)
        self.driver.find_element(*self.sign_in_password).send_keys(password)
        self.driver.find_element(*self.sign_in_btn_cfrm).click()

