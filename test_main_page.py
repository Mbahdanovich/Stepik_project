import pytest
from selenium.webdriver.common.by import By
from .Pages.login_page import LoginPage
from .Pages.main_page import MainPage
from .Pages.locators import MainPageLocators
from .Pages.basket_page import BasketPage


@pytest.mark.skip
def go_to_login_page(self):
   link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
   link.click()
   alert = self.browser.switch_to.alert
   alert.accept()


@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, browser):
        link = MainPageLocators.MAIN_PAGE_LINK
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        link = MainPageLocators.MAIN_PAGE_LINK
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()


@pytest.mark.skip
def should_be_login_link(self):
    assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = MainPageLocators.MAIN_PAGE_LINK
    page = MainPage(browser, link)
    page.open()  # Гость открывает главную страницу
    page.basket_btn_is_present()
    page.see_the_basket()  # Переходит в корзину по кнопке в шапке сайта
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.is_the_basket_empty()
    basket_page.message_basket_empty_present()
