from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), \
            "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), \
            "Register form is not presented"

    def register_new_user(self, email, password):
        self.should_be_register_form()
        self.enter_registration_email(email)
        self.enter_registration_password(password)
        self.enter_confirm_password(password)
        self.click_on_register_button()

    def enter_string_in_field(self, locator, string_for_field):
        field = self.browser.find_element(*locator)
        field.click()
        field.send_keys(string_for_field)

    def enter_registration_email(self, email):
        self.enter_string_in_field(LoginPageLocators.REGISTRATION_EMAIL_FIELD, email)

    def enter_registration_password(self, password):
        self.enter_string_in_field(LoginPageLocators.REGISTRATION_PASSWORD_FIELD, password)

    def enter_confirm_password(self, password):
        self.enter_string_in_field(LoginPageLocators.CONFIRM_PASSWORD_FIELD, password)

    def click_on_register_button(self):
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register_button.click()


