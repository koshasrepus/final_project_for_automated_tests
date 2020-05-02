from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_cart_is_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_LIST), \
            "The products are in the cart, but they should not be"

    def should_be_message_about_empty_cart(self):
        assert self.is_element_present(*BasketPageLocators.TEXT_ABOUT_EMPTY_CART), \
            "There is no message that the cart is empty"
