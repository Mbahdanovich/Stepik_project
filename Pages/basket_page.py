from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def is_the_basket_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_PRODUCT), "There is product in the basket, but shouldn't"

    def message_basket_empty_present(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), " EMPTY_BASKET_MESSAGE is not presented"
