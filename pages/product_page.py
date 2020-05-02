from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_cart(self):
        button_add_to_cart = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button_add_to_cart.click()

    def should_match_product_name_in_message(self):
        product_name = self.browser.find_element(*ProductPageLocators.NAME_OF_PRODUCT).text
        product_name_in_message = self.browser.find_element(*ProductPageLocators.MESSAGE_WITH_PRODUCT_NAME).text
        assert product_name == product_name_in_message,\
            f"Product name:\"{product_name}\" - does not match the name in the message:\"{product_name_in_message}\""

    def should_match_price_in_message(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        product_price_in_message = self.browser.find_element(*ProductPageLocators.MESSAGE_WITH_PRICE).text
        assert product_price == product_price_in_message,\
            f"Product price:\"{product_price}\" - does not match the price in the message:\"{product_price_in_message}\""

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not disappeared, but should disappeared"


