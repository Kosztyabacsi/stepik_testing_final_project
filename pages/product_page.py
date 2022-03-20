from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time

class ProductPage(BasePage):
    def add_product_to_basket(self):
        book_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        book_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        WebDriverWait(self.browser, 5).until(
            ec.element_to_be_clickable(ProductPageLocators.ADD_TO_BASKET)).click()

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_disappeared_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not disappeared, but should not be"

    def add_product_to_basket_with_quiz(self):
        book_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        book_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

        WebDriverWait(self.browser, 5).until(
            ec.element_to_be_clickable(ProductPageLocators.ADD_TO_BASKET)).click()
        self.solve_quiz_and_get_code()
