from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#registration_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REG_FORM_MAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REG_FORM_PASS1 = (By.CSS_SELECTOR, "#id_registration-password1")
    REG_FORM_PASS2 = (By.CSS_SELECTOR, "#id_registration-password2")

class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".price_color")
    PRODUCT_NAME_BASKET = (By.CSS_SELECTOR, ".alertinner strong")
    PRODUCT_PRICE_BASKET = (By.CSS_SELECTOR, ".alertinner p strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alertinner p strong")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini a.btn-default")
    BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner p")
    RU_MESSAGE_EMPTY_BASKET = (By.XPATH, "//p[text()=' Ваша корзина пуста ']")
    FULL_PRICE_OF_BASKET = (By.CSS_SELECTOR, "#basket_totals .total.align-right h3.price_color")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


