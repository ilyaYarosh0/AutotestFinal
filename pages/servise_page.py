import time

from .base_page import BasePage
from .locators import ServicePageLocators, CalcLocators

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ServisePage(BasePage):
    def send_text(self):
        text = self.browser.find_element(*ServicePageLocators.POST_FORM)
        text.send_keys("Hello from WebDriver")

    def send_text1(self):
        text = self.browser.find_element(*ServicePageLocators.POST_FORM)
        text1 = '''git config --global user.name  "New Sheriff in Town"
git reset $(git commit-tree HEAD^{tree} -m "Legacy code")
git push origin master --force'''
        text.send_keys(text1)

    def send_name(self):
        element = self.browser.find_element(*ServicePageLocators.POST_NAME)
        #self.browser.execute_script("return arguments[0].scrollIntoView(true);", element)
        element.send_keys("helloweb")

    def send_name1(self):
        element = self.browser.find_element(*ServicePageLocators.POST_NAME)
        #self.browser.execute_script("return arguments[0].scrollIntoView(true);", element)
        element.send_keys("how to gain dominance among developers")

    def choose_expiration(self):
        numb = self.browser.find_element(*ServicePageLocators.PASTE_EXPIRATION)
        #self.browser.execute_script("return arguments[0].scrollIntoView(true);", numb)
        numb.click()
        time.sleep(1)
        numb2 = self.browser.find_element(*ServicePageLocators.CHOOSE_NUMB)
        numb2.click()

    def choose_bash(self):
        numb = self.browser.find_element(*ServicePageLocators.SYNTAX)
        time.sleep(2)
        numb.click()
        time.sleep(1)
        numb2 = self.browser.find_element(*ServicePageLocators.CHOOSE_BASH)
        numb2.click()

    def click_button(self):
        btn = self.browser.find_element(*ServicePageLocators.BUTTON)
        #self.browser.execute_script("return arguments[0].scrollIntoView(true);", btn)
        btn.click()

    def should_be_right_titl(self):
        title = self.browser.find_element(*ServicePageLocators.TITLE)
        title_text = title.text
        print(title_text)
        assert title_text == "how to gain dominance among developers", \
            "Wrong title"
    def should_be_right_syntax(self):
        syntx = self.browser.find_element(*ServicePageLocators.BASH)
        element = syntx.get_attribute("class")
        assert element == "bash", \
            "Wrong syntax"
    def should_be_right_text(self):
        bash = self.browser.find_element(*ServicePageLocators.BASH)
        bash_text = bash.text
        text = '''git config --global user.name  "New Sheriff in Town"
git reset $(git commit-tree HEAD^{tree} -m "Legacy code")
git push origin master --force'''
        assert bash_text == text, \
            "Wrong text"
class CalcPage(BasePage):
    def open_calc(self):
        find = self.browser.find_element(*CalcLocators.FIND)
        find.click()
        search = self.browser.find_element(*CalcLocators.SEARCH)
        search.send_keys("google server calculator")
        search.send_keys(Keys.ENTER)
        time.sleep(5)
        open_link = self.browser.find_element(*CalcLocators.OPEN_LINK)
        open_link.click()

    def choose_right_value(self):
        time.sleep(2)
        iframe = self.browser.find_element(*CalcLocators.IFRAME)
        self.browser.switch_to.frame(iframe)
        # time.sleep(2000)

        iframe1 = self.browser.find_element(*CalcLocators.IFRAME1)
        self.browser.switch_to.frame(iframe1)
        number_instance = self.browser.find_element(*CalcLocators.NUMBER_OF_INSTANCE)
        number_instance.send_keys("4")
        time.sleep(3)
        #select_value = self.browser.find_element(*CalcLocators.SELECT_VALUE)
       # select_value.click()
       # select_free = self.browser.find_element(*CalcLocators.FREE)
        #select_free.click()

