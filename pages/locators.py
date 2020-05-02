from selenium.webdriver.common.by import By


class BasePageLocators:

    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BUTTON_OF_CART = (By.CSS_SELECTOR, ".header span > a.btn")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators:

    PRODUCT_LIST = (By.CSS_SELECTOR, ".row li .product_pod")


class LoginPageLocators:

    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.ID, "register_form")
    REGISTRATION_EMAIL_FIELD = (By.ID, "id_registration-email")
    REGISTRATION_PASSWORD_FIELD = (By.ID, "id_registration-password1")
    CONFIRM_PASSWORD_FIELD = (By.ID, "id_registration-password2")

    REGISTER_BUTTON = (By.CSS_SELECTOR, "#content_inner button[name='registration_submit']")


class ProductPageLocators:

    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form button")
    NAME_OF_PRODUCT = (By.CSS_SELECTOR, "#content_inner .product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "#content_inner .product_main .price_color")
    MESSAGE_WITH_PRODUCT_NAME = (By.CSS_SELECTOR, "#messages div.alert:nth-child(1) div.alertinner strong")
    MESSAGE_WITH_PRICE = (By.CSS_SELECTOR, "#messages div.alert:nth-child(3) p strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alert-success:nth-child(1)")


class BasketPageLocators:

    PRODUCT_LIST = (By.CSS_SELECTOR, "#basket_formset .basket-items")
    TEXT_ABOUT_EMPTY_CART = (By.CSS_SELECTOR, "#content_inner p")



