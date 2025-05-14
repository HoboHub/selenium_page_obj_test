from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.book_page import BookPage

def test_guest_can_go_to_login_page(browser):
    # link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    link = "http://selenium1py.pythonanywhere.com"
    # link = "https://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=midsummer"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()

    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

    # link = "https://selenium1py.pythonanywhere.com/ru/accounts/login/"
    # page = LoginPage(browser, link)
    # page.open()
    # page.should_be_login_page()

def test_can_add_book_to_cart(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    # page = MainPage(browser, link)
    page = BookPage(browser, link)
    page.open()

    page.add_to_cart()

    page.solve_quiz_and_get_code()
