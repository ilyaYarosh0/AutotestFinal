from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class BasePage:

    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def scroll_down(self, offset=0):
        """ Scroll the page down. """

        if offset:
            self.browser.execute_script('window.scrollTo(0, {0});'.format(offset))
        else:
            self.browser.execute_script('window.scrollTo(0, document.body.scrollHeight);')




