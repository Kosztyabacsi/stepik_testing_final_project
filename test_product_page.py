import pytest
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.base_page import BasePage
import time

links = [
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"
]

@pytest.mark.parametrize("product", links)
def test_guest_can_add_product_to_basket(browser, product: str):

    link = product
    print(link)
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url
    page.open()                         # открываем страницу
    page.add_product_to_basket_with_quiz()


def test_guest_cant_see_success_message_after_adding_product_to_basket(browser): 
    # Открываем страницу товара 
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url
    page.open()                         # открываем страницу

    # Добавляем товар в корзину 
    page.add_product_to_basket()
    
    # Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser): 
    # Открываем страницу товара 
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url
    page.open()                         # открываем страницу

    # Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    page.should_not_be_success_message()

def test_message_disappeared_after_adding_product_to_basket(browser): 
    # Открываем страницу товара 
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url
    page.open()                         # открываем страницу

    # Добавляем товар в корзину 
    page.add_product_to_basket()
    # Проверяем, что нет сообщения об успехе с помощью is_disappeared
    page.should_be_disappeared_message()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    # Гость открывает страницу 
    page.open()
    # Переходит в корзину по кнопке в шапке сайта
    page.go_to_basket_page()
    # Ожидаем, что в корзине нет товаров
    page.should_be_not_items_in_basket()
    # Ожидаем, что есть текст о том что корзина пуста 
    page.should_be_message_basket_empty()

@pytest.mark.reg_test
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = BasePage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url
        page.open()                         # открываем страницу
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time())
        #        password = str(GeneratingPassword.get_random_password(6))
        login_page.register_new_user(email, password)

    def test_user_can_add_product_to_basket(self, browser):
        # Открываем страницу товара 
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url
        page.open()                         # открываем страницу
        page.add_product_to_basket()

    def test_user_cant_see_success_message(self, browser): 
        # Открываем страницу товара 
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url
        page.open()                         # открываем страницу
        # Проверяем, что нет сообщения об успехе с помощью is_not_element_present
        page.should_not_be_success_message()

