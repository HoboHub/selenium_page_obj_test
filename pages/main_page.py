from .base_page import BasePage
from .locators import MainPageLocators

from selenium.webdriver.common.by import By

class MainPage(BasePage):
    def go_to_login_page(self):        
        login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        login_link.click() 

        #    alert = self.browser.switch_to.alert
        #    alert.accept()

        # # return LoginPage(browser=self.browser, url=self.browser.current_url) 
        
        # login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)

    def should_be_login_link(self):
        assert self.is_element_present(By.CSS_SELECTOR, "#login_link_invalid"), "Login link is not presented"
        # assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"