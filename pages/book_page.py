from .base_page import BasePage
from .locators import BookPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BookPage(BasePage):
    def add_to_cart(self):
        self.should_be_add_to_cart_btn()
        self.should_be_clickable_add_to_cart_btn()

        button = self.browser.find_element(*BookPageLocators.ADD_TO_CART_BUTTON)
        button.click()

    
    def should_be_add_to_cart_btn(self):
        assert self.is_element_present(*BookPageLocators.ADD_TO_CART_BUTTON), "'Add to cart' button is not presented"
    
    def should_be_clickable_add_to_cart_btn(self):
        assert self.is_element_clickable(BookPageLocators.ADD_TO_CART_BUTTON), "'Add to cart' button is not clickable"
