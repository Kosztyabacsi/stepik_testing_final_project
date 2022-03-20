from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url, 'Substring \"login\" not in URL'

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        input1 = self.browser.find_element(*LoginPageLocators.REG_FORM_MAIL)
        input1.send_keys(email)
        input2 = self.browser.find_element(*LoginPageLocators.REG_FORM_PASS1)
        input2.send_keys(password)
        input3 = self.browser.find_element(*LoginPageLocators.REG_FORM_PASS2)
        input3.send_keys(password)
        button = self.browser.find_element_by_name("registration_submit")
        button.click()
