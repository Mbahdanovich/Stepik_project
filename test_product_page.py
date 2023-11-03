import pytest
from .Pages.product_page import ProductPage
from .Pages.locators import ProductPageLocators
from .Pages.basket_page import BasketPage
from .Pages.locators import LoginPageLocators
from .Pages.login_page import LoginPage


class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser, timeout=5):
        link = LoginPageLocators.LOGIN_PAGE_LINK  # ссылка на страницу логина\регистрации
        self.browser = browser
        # неявное ожидание
        self.browser.implicitly_wait(timeout)
        # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page = LoginPage(browser, link)  # открываем нужную страницу
        page.open()
        email, password = page.make_email_and_pass()  # генерим тестовую почту, задаем пароль
        page.register_new_user(email, password)  # регистрируем нового пользователя
        # проверяем, что пользователь авторизован
        page.should_be_authorized_user()  # на деле такие проверки лучше не делать (setup не для этого)

    def test_user_cant_see_success_message(self, browser):
        link = ProductPageLocators.PRODUCT_PAGE_PROMO2
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = ProductPageLocators.PRODUCT_PAGE_PROMO
        page = ProductPage(browser, link)
        page.open()
        page.add_product_to_basket()
        page.solve_quiz_and_get_code()
        page.should_be_name_product_basket_match_product_name_on_page()
        page.should_be_price_basket_match_price_product()


@pytest.mark.parametrize('links', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, links):
    link = f"{links}"
    # link = ProductPageLocators.PRODUCT_PAGE_PROMO
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_name_product_basket_match_product_name_on_page()
    page.should_be_price_basket_match_price_product()


@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    link = ProductPageLocators.PRODUCT_PAGE_PROMO
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_name_product_basket_match_product_name_on_page()
    page.should_be_price_basket_match_price_product()


def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = ProductPageLocators.PRODUCT_PAGE_PROMO2
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_not_be_success_message()


def test_message_disappeared_after_adding_product_to_basket(browser):
    link = ProductPageLocators.PRODUCT_PAGE_PROMO2
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_disappear_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    link = ProductPageLocators.PRODUCT_PAGE
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = ProductPageLocators.PRODUCT_PAGE
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = ProductPageLocators.PRODUCT_PAGE
    page = ProductPage(browser, link)
    page.open()  # Гость открывает страницу товара
    page.basket_btn_is_present()
    page.see_the_basket()  # Переходит в корзину по кнопке в шапке
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.is_the_basket_empty()  # Ожидаем, что в корзине нет товаров
    basket_page.message_basket_empty_present()  # Ожидаем, что есть текст о том что корзина пуста
