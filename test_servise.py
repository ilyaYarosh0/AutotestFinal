from pages.servise_page import ServisePage, CalcPage
import time

def test_servis1(browser):
    link = "https://pastebin.com"
    servise_page = ServisePage(browser, link)
    servise_page.open()
    servise_page.send_text()
    servise_page.scroll_down(600)
    servise_page.send_name()
    servise_page.choose_expiration()
    servise_page.scroll_down(800)
    servise_page.click_button()
    time.sleep(5)

def test_servis1(browser):
    link = "https://pastebin.com"
    servise_page = ServisePage(browser, link)
    servise_page.open()
    servise_page.send_text1()
    servise_page.scroll_down(600)
    servise_page.send_name1()
    servise_page.choose_expiration()
    servise_page.choose_bash()
    servise_page.scroll_down(800)
    servise_page.click_button()
    servise_page.should_be_right_titl()
    servise_page.should_be_right_syntax()
    servise_page.should_be_right_text()
    time.sleep(5)

def test_calc(browser):
    link = "https://cloud.google.com/"
    calc = CalcPage(browser,link)
    calc.open()
    calc.open_calc()
    calc.choose_right_value()

