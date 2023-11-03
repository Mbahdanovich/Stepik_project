from selenium.webdriver.common.by import By


class MainPageLocators():
    MAIN_PAGE_LINK = "https://selenium1py.pythonanywhere.com/ru/catalogue/"
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_PAGE_LINK = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    REGISTRATION_EMAIL = (By.ID, "id_registration-email")
    REGISTRATION_PASSWORD1 = (By.ID, "id_registration-password1")
    REGISTRATION_PASSWORD2 = (By.ID, "id_registration-password2")
    REGISTRATION_BUTTON = (By.NAME, "registration_submit")
    REGISTRATION_MESSAGE = (By.CSS_SELECTOR, "div.alertinner.wicon")

class ProductPageLocators():
    PRODUCT_LINK = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    PRODUCT_PAGE_PROMO2 = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    PRODUCT_PAGE_PROMO = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    PRODUCT_PAGE = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    ADD_TO_BASKET = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div")
    #MESSAGE_PRICE_PRODUCT = (By.CSS_SELECTOR, "#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div")
    PRODUCT_NAME = (By.TAG_NAME, "h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")
    PRODUCT_IN_BASKET = (By.CSS_SELECTOR, "#messages div:nth-child(1) strong")
    PRICE_IN_BASKET = (By.CSS_SELECTOR, "#messages div:nth-child(3) strong")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    SEE_BASKET_BTN = (By.CSS_SELECTOR, "span.btn-group > a.btn.btn-default")
    #SEE_BASKET_BTN_INV = (By.CSS_SELECTOR, "span.btn-group > a.btn.btn-default_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
class BasketPageLocators():
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner > p")
    BASKET_PRODUCT = (By.CSS_SELECTOR, "div.basket-items")
