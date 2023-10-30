from .Pages.product_page import ProductPage
from .Pages.locators import ProductPageLocators

def test_guest_can_add_product_to_basket(browser):
    link = ProductPageLocators.PRODUCT_PAGE_PROMO
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
