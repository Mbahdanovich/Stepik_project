from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_product_to_basket(self):
        add_to_basket_link = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_to_basket_link.click()

    def should_be_add_to_basket_link(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET), "Add to basket button is not presented"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
       "Success message is presented, but should not be"

    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
       "Success message is not disappeared, but should"

    #def should_be_message_add_product(self):
        #assert self.is_element_present(*ProductPageLocators.MESSAGE_ADD_PRODUCT), "No message about add product"

    def should_be_name_product_basket_match_product_name_on_page(self):
        product_in_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_IN_BASKET)
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        assert product_name.text == product_in_basket.text, "Product name in basket has another name"

    #def should_be_message_product_price(self):
        #assert self.is_element_present(*ProductPageLocators.MESSAGE_PRICE_PRODUCT), "Message about price product is not presented"

    def should_be_price_basket_match_price_product(self):
        price_basket = self.browser.find_element(*ProductPageLocators.PRICE_IN_BASKET)
        price_on_page = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        assert price_on_page.text == price_basket.text, "Price are different"
