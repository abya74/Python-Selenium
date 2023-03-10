import time

from selenium.webdriver.common.by import By

class RegisterPage:

    #URL
    URL = "https://www.reserved.com/ro/ro/customer/account/login/#register"

    #locators
    EMAIL_FIELD = (By.ID, "email_id")
    FIRSTNAME_FIELD = (By.ID, "firstname_id")
    LASTNAME_FIELD = (By.ID, "lastname_id")
    PASSWORD_FIELD = (By.ID, "password_id")
    CREATE_ACCOUNT_BUTTON = (By.CSS_SELECTOR, "button[data-selen='create-account-submit']")
    ACCEPT_COOKIES_BUTTON = (By.ID, 'cookiebotDialogOkButton')

    def __init__(self, browser):
        self.browser = browser

    def load_page(self):
        self.browser.get(self.URL)
        self.browser.find_element(*self.ACCEPT_COOKIES_BUTTON).click()

    def type_email(self, email):
        self.browser.find_element(*self.EMAIL_FIELD).send_keys(email)

    def type_firstname(self, firstname):
        self.browser.find_element(*self.FIRSTNAME_FIELD).send_keys(firstname)

    def type_lastname(self, lastname):
        self.browser.find_element(*self.LASTNAME_FIELD).send_keys(lastname)

    def type_password(self, password):
        self.browser.find_element(*self.PASSWORD_FIELD).send_keys(password)

    def click_create_account_button(self):
        self.browser.find_element(*self.CREATE_ACCOUNT_BUTTON).click()
        time.sleep(12)